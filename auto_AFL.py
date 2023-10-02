import subprocess
import os
import time
import pyinotify
import queue
import signal
import psutil

# commands = ["mkdir build", "CC=/AFLplusplus/afl-clang-fast CXX=/AFLplusplus/afl-clang-fast++ cmake -B ./build",
#             "make -C ./build"]
#
# executable_path = os.getcwd() + "/build/AirplaneApp"

seeds_path = os.path.join(os.getcwd(), "seeds_kth_hanoi")

# crashes_folder = os.path.join(os.getcwd(), "out", "default", "crashes")


# def add_AFL_compiler(commands):
#     for command in commands:
#         try:
#             subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#
#         except subprocess.CalledProcessError as e:
#             print(f"error：\n{e.stderr}")


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

        # if os.path.exists(crashes_folder):
        #     files_in_folder = os.listdir(crashes_folder)
        #
        #     found = False
        #     for file_name in files_in_folder:
        #         if file_name.startswith("id"):
        #             found = True
        #             break
        #
        # if found:
        #     try:
        #         subprocess.run(['killall', 'afl-fuzz'])
        #         print("afl++ is paused")
        #
        #     except subprocess.CalledProcessError:
        #         print("can not pause afl++")


