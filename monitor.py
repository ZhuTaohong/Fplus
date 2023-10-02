import subprocess
import os
import time
import pyinotify
import queue

crashes_folder = os.path.join(os.getcwd(), "out", "default", "crashes")

out_folder = os.getcwd()


class CrashesEventHandler(pyinotify.ProcessEvent):

    def process_IN_CREATE(self, event):
        if os.path.basename(event.pathname).startswith('id'):
            print(f"Detected new crash: {event.pathname}")
            pause_afl()


def pause_afl():
    try:
        subprocess.run(['killall', 'afl-fuzz'])
        print("afl++ is paused")

    except subprocess.CalledProcessError:
        print("can not pause afl++")

class OutEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        if os.path.basename(event.pathname).startswith('out'):
            print(f"Detected afl output folder: {event.pathname}")
            wm = pyinotify.WatchManager()
            mask = pyinotify.IN_CREATE
            handler = CrashesEventHandler()
            notifier = pyinotify.Notifier(wm, handler)
            time.sleep(0.1)
            wm.add_watch(crashes_folder, mask, rec=False)
            print("monitoring new crashes")
            notifier.loop()


def main():

    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, OutEventHandler())


    mask = pyinotify.IN_CREATE


    wdd = wm.add_watch(out_folder, mask, rec=True)


    print(f"start monitoring crashes folder ：{crashes_folder}")
    notifier.loop()


if __name__ == "__main__":
    main()
