import subprocess
import os
import time
import pyinotify
import queue
import signal
import psutil

seeds_path = os.path.join(os.getcwd(), "seeds_kth_hanoi")

def run_aflplusplus(code_path):
    afl_cmd = ["py-afl-fuzz", "-i", seeds_path, "-o", "out", "--", "python", code_path]
    afl_process = subprocess.Popen(afl_cmd)

    return afl_process


def run_monitor():
    print("running monitor")

    command = ['python', 'monitor.py']

    process = subprocess.Popen(command)


def check_afl_fuzz_process():
    for proc in psutil.process_iter(['pid', 'name']):
        # print(proc.info['name'])
        if proc.info['name'] == 'afl-fuzz':
            return True
    return False


def get_crash(code_path):
    # print("Adding afl compiler")
    # add_AFL_compiler(commands)

    run_monitor()

    time.sleep(5)

    print("Running AFL++")

    afl_process = run_aflplusplus(code_path)
    afl_process.wait()

    while True:
        if not check_afl_fuzz_process():
            break



