"""
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   Python 3.9.7 64-bit
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
"""

"""
Code Explanation
----------------
If no path is mentioned then the current directory is explored for its contents.
If the item is a file then its size is stored and if it is directory the 
same function is called with the directory's path.
This recursion stops when all directories have been explored and file sizes stored.
The final size is returned.
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



"""
Answer the following questions in comments in one of the source files or in the submission text area on Canvas:

1) Was one language easier or faster to write the code for this? 
If so, describe in detail why, as in what about the language made that the case.

I did the Lab in Python, Java and C++. 
For this task, using Python was the easiest and fastest approach for me. 
Having said that, Java was a close competition.
C++ took the most time.

In Python, the presence of the os library which provides all the required in-built functions made the task easy.

--------------------------------------------------------------------
2) Even though a language may not (e.g. FORTRAN) does not support recursion, 
describe how you could write a program to produce the same results without using recursion. 
Would that approach have any limitations and if so, what would they be?

1. We can start by accessing a given path and fetching its contents
2. These contents can be stored in an array of strings (file/directory paths)
3. If the item is a file, then we store its size.
4. If the item is a directory, then we can access its contents and add to our array we used earlier.
5. This happens for every directory until all directories are accessed.
6. The program must run in loop until the entire array containing paths has been traversed.

Limitations

1. The space complexity of this program will can be large as we are storing all the file/ directory paths.
2. It can be more hard to understand compared to the recursive approach.
"""