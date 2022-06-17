// Your First C++ Program


#include<stdio.h>
#include<string>
#include<dirent.h>
#include<sys/stat.h>
#include <unistd.h>
#define GetCurrentDir getcwd
#include<iostream>

std::string GetCurrentWorkingDir( void ) {
  char buff[FILENAME_MAX];
  GetCurrentDir( buff, FILENAME_MAX );
  std::string current_working_dir(buff);
  return current_working_dir;
}

int gds(char p[])
{
  int t = 0;
  char df[2000];
  std::string cwd = GetCurrentWorkingDir();
  struct dirent *dp;
  struct stat file;

 if (strcmp(p, "") == 0){
    p = const_cast<char*>(cwd.c_str());
 }

  DIR *ditory = opendir(p);

  while ((dp=readdir(ditory))!=NULL) 
  {
    if(strcmp(dp->d_name,".")==0 || strcmp(dp->d_name,"..")==0)
    {
      continue;
    }
    strcpy(df,p);
    strcat(df,"/");
    strcat(df,dp->d_name);
    stat(df,&file);
    
    if(S_ISREG(file.st_mode))
    {
      FILE *fpoint = fopen(df,"r");
      fseek(fpoint,0L,SEEK_END);
      int res = ftell(fpoint);
      t += res;
      fclose(fpoint);
    }
    else
    {
      t += gds(df);
    }
  }
  return t;

}

int main()
{
  int totalSize = gds("");
  printf("\n******************");
  printf("\n%d",totalSize);
  printf("\n******************");

  return 0;
}


//--------

// #include <stdio.h>  /* defines FILENAME_MAX */
// // #define WINDOWS  /* uncomment this line to use it for windows.*/ 
// // #ifdef WINDOWS
// // #include <direct.h>
// // #define GetCurrentDir _getcwd
// // #else
// #include <unistd.h>
// #define GetCurrentDir getcwd
// // #endif
// #include<iostream>

// std::string GetCurrentWorkingDir( void ) {
//   char buff[FILENAME_MAX];
//   GetCurrentDir( buff, FILENAME_MAX );
//   std::string current_working_dir(buff);
//   return current_working_dir;
// }

// int main(){
//   std::cout << GetCurrentWorkingDir() << std::endl;
//   return 1;
// }

//--------





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

// #include <iostream>
// #include <string>
// #include <filesystem>
// #include <unistd.h>

// using std::cout; using std::cin;
// using std::endl; using std::string;
// using std::filesystem::current_path;

// int main() {
//     char tmp[256];
//     getcwd(tmp, 256);
//     cout << "Current working directory: " << tmp << endl;

//     return EXIT_SUCCESS;
// }

// #include <iostream>
// #include <filesystem>
// namespace fs = std::filesystem;
// int main()
// {
//     std::cout << "Current path is " << fs::current_path() << '\n'; // (1)
//     fs::current_path(fs::temp_directory_path()); // (3)
//     std::cout << "Current path is " << fs::current_path() << '\n';
// }