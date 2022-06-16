"""
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   Python 3.9.7 64-bit
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
"""

# Helps with OS dependent functionality
import os


def get_total_size(path=''):

    total_size = 0      # this variable will store the size

    if path == '':      # if path is empty then it will access the current directory
        current_directory = os.getcwd()
    else:
        current_directory = path

    # list of all the contents in the given directory
    list_of_contents = os.listdir(current_directory)

    for item_name in list_of_contents:
        # gives the full path of the item
        full_path = os.path.join(current_directory, item_name)

        if os.path.isfile(full_path):       # isfile func returns True if the path is a File
            print('File = ' + item_name + ' has size = ' + str(os.path.getsize(full_path)) + ' Bytes')
            total_size += os.path.getsize(full_path)

        elif os.path.isdir(full_path):      # isdir func returns True if the path is a Directory
            print('Directory found -> ' + item_name)
            total_size += get_total_size(full_path) # recursion to access sub-directories
            print('----------------')
        else:
            exception_msg = 'Item = ' + item_name + ' is not a file or directory'
            print(exception_msg)

    return total_size


def main():
    total_size = get_total_size()
    print('*********************************')
    print('Total Size = ' + str(total_size) + ' Bytes')
    print('*********************************')


if __name__ == '__main__':
    main()



