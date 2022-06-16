/**
Instruction 10
Name        :   Amlan Alok
UTA ID      :   1001855861
Lang Version:   java 16.0.2 2021-07-20
OS          :   macOS Big Sur Version 11.5.1 (M1 Chip)
 */

import java.nio.file.Path;
import java.io.File;
//import java.nio.file.Files;

class TotalSize {

    public int getTotalSize(String path){

//         Path path = FileSystems.getDefault().getPath(".");

        String cwd = Path.of("").toAbsolutePath().toString();
        System.out.println(cwd);
        if (path == "") {
            path = cwd;
        }

        File directory = new File(path);
        File[] dir_contents = directory.listFiles();

        if (dir_contents != null) {
            for (File itemName: dir_contents) {
                if (itemName.isFile()){
                      System.out.println("File = " + itemName + " has size = " + itemName.length() + " Bytes");
                }
                else if (itemName.isDirectory()) {
                    System.out.println("Directory = " + itemName);
                }
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        System.out.println("Hello, World!");
        TotalSize totalSize = new TotalSize();
        totalSize.getTotalSize("");
    }
}