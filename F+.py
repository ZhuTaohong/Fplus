import subprocess
import os
import auto_AFL
import get_trace
import gpt_anlayze_trace
import argparse
import verification



# def run_gpt_instrument():
#     command = ['python', 'gpt_instrument.py']
#
#     process = subprocess.Popen(command)
#
#     process.wait()

def repeatFix(args, bugNo):
    print("need fix again")
    print("Getting crash trace")
    get_trace.get_trace(args.code_path)
    print("Done")
    print("Analyze with GPT")
    gpt_anlayze_trace.crash_analyze(args.code_path)
    if verification.verification(args.code_path):
        start(args, bugNo)
    else:
        repeatFix(args, bugNo)

def start(args, bugNo):
    auto_AFL.get_crash(args.code_path)
    bugNo += 1
    print("Num of bug: ", bugNo)
    print("Getting crash trace")
    get_trace.get_trace(args.code_path)
    print("Done")
    print("Analyze with GPT")
    gpt_anlayze_trace.crash_analyze(args.code_path)
    if verification.verification(args.code_path):
        start(args, bugNo)
    else:
        repeatFix(args, bugNo)



def main():
    parser = argparse.ArgumentParser(description='auto fixing')
    parser.add_argument(
        '--code_path', dest='code_path', default='bucketsort.py', help='source code path')

    args = parser.parse_args()

    bugNO = 0

    start(args, bugNO)




if __name__ == "__main__":
    main()

