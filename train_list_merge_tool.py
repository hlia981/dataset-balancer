# author: Benedict Liang
# Dataset imbalance solver
import random


def copy_unique_lines_and_append(file_a_path, file_b_path, file_c_path, output_path):
    with open(file_a_path, 'r') as file_a:
        lines_a = set(file_a.readlines())

    with open(file_b_path, 'r') as file_b:
        lines_b = set(file_b.readlines())

    unique_lines = lines_a - lines_b

    with open(file_c_path, 'r') as file_c:
        lines_c = file_c.readlines()

    lines_to_append = [line for line in lines_c if line.strip() != '']

    # Append lines from file C randomly to the unique lines from file A
    combined_lines = list(unique_lines) + lines_to_append
    random.shuffle(combined_lines)  # shuffle the entire txt

    with open(output_path, 'w') as output_file:
        output_file.writelines(combined_lines)


# file path a: original b: discard c:need to add
file_a_path = 'train_list_video_test.txt'
file_b_path = 'discard_name_book.txt'
file_c_path = 'need_to_add_name_book.txt'
output_path = 'output_file.txt'

copy_unique_lines_and_append(file_a_path, file_b_path, file_c_path, output_path)
