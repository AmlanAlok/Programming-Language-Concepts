/**
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   java 16.0.2 2021-07-20
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
 */

/**
Code Explanation
----------------
If no path is mentioned then the current directory is explored for its contents.
If the item is a file then its size is stored and if it is directory the 
same function is called with the directory's path.
This recursion stops when all directories have been explored and file sizes stored.
The final size is returned.
 */
 
import java.nio.file.Path;
import java.io.File;

class TotalSize {

    public int getTotalSize(String path){

        int totalSize = 0;

        if (path == "") {
            path = Path.of("").toAbsolutePath().toString();
        }

        File directory = new File(path);
        File[] dir_contents = directory.listFiles();

        if (dir_contents != null) {
            for (File itemName: dir_contents) {
                if (itemName.isFile()){
                      System.out.println("File = " + itemName + " has size = " + itemName.length() + " Bytes");
                      totalSize += itemName.length();
                }
                else if (itemName.isDirectory()) {
                    System.out.println("Directory = " + itemName);
                    totalSize += getTotalSize(itemName.toString());
                    System.out.println("------------------------");
                }
            }
        }

        return totalSize;
    }

    public static void main(String[] args) {
        TotalSize totalSize = new TotalSize();
        int totalSizeValue = totalSize.getTotalSize("");
        System.out.println("*****************************");
        System.out.println("Total Size = " + totalSizeValue + " Bytes");
        System.out.println("*****************************");
    }
}