/**
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   Apple clang version 12.0.5
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
 */

#include<stdio.h>
#include<string>
#include<dirent.h>
#include<sys/stat.h>
#include <unistd.h>
#define GetCurrentDir getcwd
#include<iostream>

// This function returns the path of current working directory (CWD)
std::string getCurrentWorkingDir(void) {
  char buff[FILENAME_MAX];
  GetCurrentDir( buff, FILENAME_MAX );
  std::string current_working_dir(buff);
  return current_working_dir;
}

int getTotalSize(char path[])
{
  int totalSize = 0;
  char filePath[2000];
  // fetches the current working directory (CWD)
  std::string cwd = getCurrentWorkingDir();
  struct dirent *item;
  struct stat file;

  // if path is empty then it will use the CWD
 if (strcmp(path, "") == 0){
    path = const_cast<char*>(cwd.c_str());
 }

  DIR *directory = opendir(path); // opens directory stream

  while ((item=readdir(directory))!=NULL) 
  {
    // "." is a hardlink to its containing directory. Hence, skipped.
    // ".." means parent directory. Hence, skipped.
    if(strcmp(item->d_name,".")==0 || strcmp(item->d_name,"..")==0)
    {
      continue;
    }
    strcpy(filePath,path);
    strcat(filePath,"/");
    strcat(filePath,item->d_name); // creating full path for item
    stat(filePath,&file);
    
    if(S_ISREG(file.st_mode))
    {
      FILE *fpoint = fopen(filePath,"r");
      fseek(fpoint,0L,SEEK_END);
      int res = ftell(fpoint);
      totalSize += res;
      fclose(fpoint);
    }
    else if (S_ISDIR(file.st_mode))
    {
      totalSize += getTotalSize(filePath); // recursion call
    }
    else {
        printf("Neither a file nor a directory");
    }
  }
  return totalSize;

}

int main()
{
  int totalSize = getTotalSize("");
  printf("\n******************");
  printf("\n Total size = %d Bytes",totalSize);
  printf("\n******************");

  return 0;
}






// #include <sys/stat.h>
// #include <cstdio>
// #include <cstdlib>

// #include <iostream>

// int main (int argc, char *argv[])
// {
//   if (argc < 2) {
//     std::cerr << "Usage: " << argv[0] << " path\n";
//     return 1;
//   }
//   std::string path(argv[1]);

//   struct stat s;
//   if ( lstat(path.c_str(), &s) == 0 ) {
//     if ( S_ISDIR(s.st_mode) ) {
//       // it's a directory
//       std::cout << path << " is a dir.\n";
//     } else if (S_ISREG(s.st_mode)) {
//       // it's a file
//       std::cout << path << " is a file.\n";
//     } else if (S_ISLNK(s.st_mode)) {
//       // it's a symlink
//       std::cout << path << " is a symbolic link.\n";
//     } else {
//       //something else
//       std::cout << path << " type is not recognized by this program.\n";
//     }
//   } else {
//     //error
//     std::cerr << "stat() return !0 value\n";
//     return 1;
//   }
//   return 0;
// }
