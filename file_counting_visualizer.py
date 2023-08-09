# author: Benedict Liang
# Dataset imbalance solver
import os
import matplotlib.pyplot as plt


def count_files_in_subfolders(folder_path):
    subfolder_counts = {}

    for root, dirs, files in os.walk(folder_path):
        subfolder_name = os.path.relpath(root, folder_path)
        if subfolder_name == '.':
            continue
        file_count = len(files)
        subfolder_counts[subfolder_name] = file_count

    return subfolder_counts


def start_visualize(folder_path):
    subfolder_counts = count_files_in_subfolders(folder_path)

    if subfolder_counts:
        subfolder_names = list(subfolder_counts.keys())
        file_counts = list(subfolder_counts.values())

        plt.figure(figsize=(8, 8))
        plt.pie(file_counts, labels=subfolder_names, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title("File Counts in Each Sub-Folder")
        plt.show()
    else:
        print("No sub-folders found.")


if __name__ == "__main__":
    folder_path = r"D:\view0_lh_pt\videos_train"
    start_visualize(folder_path)
