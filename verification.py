import subprocess
import os
import time
import pyinotify
import queue
import signal
import psutil

def verification(code_path):
    print("start the verification")
    # add_AFL_compiler(commands)

    crashes_folder = os.path.join(os.getcwd(), "out", "default", "crashes")

    if os.path.exists(crashes_folder):
        crash_path = \
            [os.path.join(crashes_folder, file) for file in os.listdir(crashes_folder) if file.startswith("id")][0]

    try:
        # Run the C program and capture the output
        output = subprocess.check_output("python " + code_path + " < " + crash_path, shell=True, stderr=subprocess.STDOUT, text=True)

        del_commands = ["rm -rf out"]

        for command in del_commands:
            subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

        print("Bug fixed, start fuzzing again")

        return True

    except subprocess.CalledProcessError as e:
        # If an error occurs, return the captured output before the error
        print("still crash")

        return False



