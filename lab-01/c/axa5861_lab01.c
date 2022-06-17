
#include<stdio.h>
#include<string.h>
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
    
    if(S_ISREG(file.st_mode)) // returns True if a file
    {
      FILE *fpoint = fopen(filePath,"r");
      fseek(fpoint,0L,SEEK_END);
      int res = ftell(fpoint);
      totalSize += res;
      fclose(fpoint);
    }
    else if (S_ISDIR(file.st_mode)) // returns True if a directory
    {
      totalSize += getTotalSize(filePath);
    }
    else {
        printf("Neither a File nor a Directory")
    }
  }
  return totalSize;

}

int main()
{
  int totalSize = getTotalSize("");
  printf("\n******************");
  printf("\n%d",totalSize);
  printf("\n******************");
  return 0;
}