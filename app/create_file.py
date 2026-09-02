import datetime
import os
import sys

input_data = sys.argv

if "-d" in input_data and "-f" not in input_data:
    d_index = input_data.index("-d")
    os.makedirs(os.path.join(*input_data[d_index + 1:]))

if "-f" in input_data and "-d" not in input_data:
    f_index = input_data.index("-f")
    if os.path.isfile(input_data[f_index + 1]):
        work_file = open(input_data[f_index + 1], "a")
        work_file.write("\n")
    else:
        work_file = open(input_data[f_index + 1], "w")
    current_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    count = 1

    work_file.write(current_date)
    work_file.write("\n")

    while True:

        input_text = input("Enter content line: ")
        if input_text == "stop":
            work_file.close()
            break

        work_file.write(f"{count} {input_text}\n")
        count += 1

if "-d" in input_data and "-f" in input_data:
    f_index = input_data.index("-f")
    d_index = input_data.index("-d")
    if f_index > d_index:
        os.makedirs(os.path.join(*input_data[2:f_index]))
        dir_path = os.path.join(*input_data[2:f_index])
        file_path = os.path.join(dir_path, input_data[f_index + 1])
    else:
        os.makedirs(os.path.join(*input_data[d_index + 1:]))
        dir_path = os.path.join(*input_data[d_index + 1:])
        file_path = os.path.join(dir_path, input_data[f_index + 1])

    current_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    count = 1

    with open(file_path, "a") as work_file:
        work_file.write(current_date)
        work_file.write("\n")
        while True:

            input_text = input("Enter content line: ")
            if input_text == "stop":
                break

            work_file.write(f"{count} {input_text}\n")
            count += 1
