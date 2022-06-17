/**
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   Apple clang version 12.0.5
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
 */

// # include <stdio.h>

// int main() {
//    // printf() displays the string inside quotation
//    printf("Hello, World!");
//    return 0;
// }


#include <stdio.h>
#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int isDir(const char* fileName)
{
    struct stat path;

    stat(fileName, &path);

    return S_ISREG(path.st_mode);
}

int is_regular_file(const char *path)
{
    struct stat path_stat;
    stat(path, &path_stat);
    return S_ISREG(path_stat.st_mode);
}
  
int main(void)
{
   struct dirent *de;  // Pointer for directory entry

   // opendir() returns a pointer of DIR type. 
   DIR *dr = opendir(".");

   if (dr == NULL)  // opendir returns NULL if couldn't open directory
   {
      printf("Could not open current directory" );
      return 0;
   }

   int ret = -1;
   int y = -1;

   // Refer http://pubs.opengroup.org/onlinepubs/7990989775/xsh/readdir.html
   // for readdir()
   while ((de = readdir(dr)) != NULL)
         printf("%s\n", de->d_name);

         ret = isDir(de->d_name);
         if (ret == 0)
            printf("Directory\n");

         y = is_regular_file(de->d_name);

         printf("%d", y);
         

   closedir(dr);    
   return 0;
}