import os
import subprocess
import textwrap

def read_code_from_file(code_file_path):
    with open(code_file_path, "r") as code_file:
        code = code_file.read()
    return code


def insert_code_into_template(template_path, code_to_insert):
    with open(template_path, "r") as template_file:
        template = template_file.read()

    indented_code = textwrap.indent(code_to_insert, "    ")

    full_code = template.replace("# filling the code", indented_code)
    return full_code


def get_trace(code_path):
    code = read_code_from_file(code_path)

    final_code = insert_code_into_template("template.py", code)

    with open("trace_code.py", "w") as output_file:
        output_file.write(final_code)

    crashes_folder = os.path.join(os.getcwd(), "out", "default", "crashes")

    if os.path.exists(crashes_folder):
        crash_path = \
            [os.path.join(crashes_folder, file) for file in os.listdir(crashes_folder) if file.startswith("id")][0]

        commands = "python trace_code.py" + ' < ' + crash_path

        process = subprocess.Popen(commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        output, error = process.communicate()

        with open("trace.txt", 'r') as file:
            lines = file.readlines()

        filtered_lines = [line for line in lines if not line.strip().startswith('File')]

        with open("trace.txt", 'w') as file:
            file.writelines(filtered_lines)



