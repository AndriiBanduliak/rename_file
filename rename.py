import os

DIRECTORY = r"***********" #the path to the folder where you want to rename the files


def rename(find_dir):
    for root, dirs, files in os.walk(find_dir):
        for name in files:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = get_valid_name(name)
    old = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    os.rename(old, new_file)


def get_valid_name(name):
    name = name.replace("1", "2") #from what name(1) to what name(2) you need to rename the files
    return name


if __name__ == '__main__':
    rename(DIRECTORY)