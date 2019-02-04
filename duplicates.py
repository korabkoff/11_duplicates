import argparse
import sys
import os
from os.path import getsize, join
from collections import Counter


def readable_dir(prospective_dir):
    if not os.path.isdir(prospective_dir):
        raise argparse.ArgumentTypeError("'{0}' is not a valid path".format(prospective_dir))

    elif os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise argparse.ArgumentTypeError("'{0}' is not a readable dir".format(prospective_dir))


def parse_args(args):
    parser = argparse.ArgumentParser(description='Show duplicates of files in given folder and subfolders')
    parser.add_argument('filepath', help='File path to folder', type=readable_dir, default=None)
    return parser.parse_args(args)


def get_list_of_files(root_folder_path):
    if not root_folder_path:
        return None

    list_of_dir_name_size = list()

    # get all files in subdirectories
    for root, folders, files in os.walk(root_folder_path):
        for filename in files:
            dir_name_size = (root, filename, str(getsize(join(root, filename))))
            list_of_dir_name_size.append(dir_name_size)

    return list_of_dir_name_size


def get_duplicates(list_of_dir_name_size):
    list_namesize = ['{}{}'.format(item[1], item[2]) for item in list_of_dir_name_size]
    dict_filesize_n_count = Counter(list_namesize)

    dubs = []
    for filesize, count in dict_filesize_n_count.items():
        if count > 1:
            for dir_name_size in list_of_dir_name_size:
                if dir_name_size[1] + dir_name_size[2] == filesize:
                    dubs.append('{}/{}'.format(dir_name_size[0], dir_name_size[1]))
    return dubs


if __name__ == '__main__':

    try:
        parser = parse_args(sys.argv[1:])
        filepath = parser.filepath
    except OSError as e:
        print(e)
        exit()

    list_of_dir_name_size = (get_list_of_files(filepath))
    dubs = get_duplicates(list_of_dir_name_size)
    for dub in dubs:
        print(dub)

