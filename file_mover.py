# author: Benedict Liang
# Dataset imbalance solver
import os
import shutil
import random
import math
import file_counting_visualizer as fcv

label_dict = {'ibacb': '0', 'ibscb': '1', 'icbbs': '2', 'icbck': '3', 'icccb': '4', 'iccck': '5', 'ickcb': '6',
              'ickcc': '7', 'iftgl': '8', 'iglft': '9', 'igsft': '10', 'iibn2': '11', 'iirn1': '12', 'iplft': '13',
              'ipsft': '14', 'isbn3': '15', 'ishc1': '16', 'ishc2': '17', 'ishc3': '18', 'ishc4': '19', 'ishck': '20',
              'ispg3': '21', 'ispgw': '22', 'ispn4': '23', 'iusn6': '24', 'lck': '25', 'llb': '26', 'null': '27',
              'pbabs': '28', 'pbsba': '29', 'pbsbx': '30', 'pbscc': '31', 'pbx': '32', 'pcbbx': '33', 'pcc': '34',
              'pck': '35', 'pckbx': '36', 'pckcb': '37', 'pcsbx': '38', 'pgwbx': '39', 'pplgl': '40', 'rgw': '41',
              'rhd': '42', 'rhq': '43', 'rhw': '44', 'scbcc': '45', 'scccb': '46', 'sftg1': '47', 'sftg1ws': '48',
              'sftg2': '49', 'sftg2ws': '50', 'sntft': '51', 'sntftwn': '52', 'sntn5': '53', 'sntn5wn': '54',
              'sntsb': '55', 'sntsbwn': '56', 'ssbnt': '57', 'sshc1': '58', 'sshc1dh': '59', 'sshc1dp': '60',
              'sshc2': '61', 'sshc2dh': '62', 'sshc2dp': '63', 'sshc3': '64', 'sshc3dh': '65', 'sshc3dp': '66',
              'sshc4': '67', 'sshc4dh': '68', 'sshc4dp': '69', 'sspg3': '70', 'sspg3dp': '71', 'sspn4': '72',
              'sspn4dp': '73', 'w': '74'}


def check_file_count_(folder_path, mean_file_count):
    for root, dirs, files in os.walk(folder_path):
        folder_files = len(files)
        if folder_files == 0:
            continue

        difference = mean_file_count - folder_files
        if folder_files > mean_file_count:
            print(f"Files count in sub-folder '{root}' is greater than mean by {int(difference)}")
        else:

            print(f"Files count in sub-folder '{root}' is lower than mean. Difference: {int(difference)}")


def move_file_wrt_file_count(folder_path, mean_file_count, threshold=200):
    os.makedirs('temp_videos', exist_ok=True)
    temp_folder = os.path.abspath("temp_videos")
    for root, dirs, files in os.walk(folder_path):
        folder_files = len(files)
        if folder_files == 0:
            continue
        difference = mean_file_count - folder_files
        difference = math.ceil(difference)
        if difference > 0:
            print("difference: ", difference)
            # print(files)
            selected_files = random.choices(files, k=difference)
            subfolder_name = os.path.relpath(root, folder_path)

            for index, selected_file in enumerate(selected_files):
                src_path = os.path.join(root, selected_file)
                new_file_name = f"{subfolder_name}_{index}.mp4"
                dst_path = os.path.join(root, new_file_name)
                shutil.copy(src_path, dst_path)
                print(f"Duplicated: '{selected_file}' as '{new_file_name}'")
                with open("need_to_add_name_book.txt", 'a') as f:
                    f.write(f'{subfolder_name}/{new_file_name} {label_dict[subfolder_name]}\n')

        if difference < -threshold:
            print("difference: ", difference)
            selected_files = random.sample(files, k=threshold)
            subfolder_name = os.path.relpath(root, folder_path)
            for index, selected_file in enumerate(selected_files):
                src_path = os.path.join(root, selected_file)
                dst_path = os.path.join(temp_folder, selected_file)
                shutil.move(src_path, dst_path)
                print(f"Moved: '{selected_file}'")
                with open("discard_name_book.txt", 'a') as f:
                    f.write(f'{subfolder_name}/{selected_file} {label_dict[subfolder_name]}\n')


def count_files_in_subfolders(folder_path):
    subfolder_counts = {}

    for root, dirs, files in os.walk(folder_path):
        subfolder_name = os.path.relpath(root, folder_path)
        if subfolder_name == '.':
            continue
        file_count = len(files)
        subfolder_counts[subfolder_name] = file_count

    return subfolder_counts


def main(folder_path):
    subfolder_counts = count_files_in_subfolders(folder_path)

    total_files = sum(subfolder_counts.values())
    total_subfolders = len(subfolder_counts)

    if total_subfolders > 0:
        mean_file_count = total_files / total_subfolders
        print(f"Mean file count: {mean_file_count:.2f}")
        move_file_wrt_file_count(folder_path, mean_file_count)
    else:
        print("No sub-folders found.")


if __name__ == "__main__":
    folder_path = r"D:\view0_lh_pt\videos_train"
    fcv.start_visualize(folder_path)
    main(folder_path)
    fcv.start_visualize(folder_path)
