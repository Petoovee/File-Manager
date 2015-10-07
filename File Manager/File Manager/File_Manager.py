# Imports
import os
import re
os.system('cls')

# Variables
SourceFolder = input("\nFrom which folder do you wish me to move the files?\n")
TargetFolder = input("\nTo which folder do you wish me to move the files?\n")
MaxSize = int(input("\nMinimum size (MB) of file to move? \n")) *1048576
SourceFiles = "a"
TargetFiles = "b"
MovedCounter = 0
TargetCounter = 0

# Move file
def Junction (SourceFile, TargetFile):
    MovedCounter + 1
    os.system('move "' +SourceFile +'" "' +TargetFile +'"')
    print(TargetFile +" was moved")
    os.system('mklink "' +SourceFile +'" "' +TargetFile +'"')
    return(MovedCounter)

# Finds the files to be moved, and finds where to put them
def FileFinder (SourceFolder, TargetFolder, MaxSize):
    Folders = [SourceFolder]
    print(SourceFolder)
    for Folder in Folders:
        print("Looking in " +Folder)
        try:
            for File in os.listdir(Folder):
                try:
                    if os.path.isfile(Folder +"\\" +File) is True:
                        try:
                            if (os.path.getsize(Folder +"\\" +File)>MaxSize):
                                try:
                                    # This way the folder is only made in case the file is actually getting moved
                                    # and if it already exists it will only error out and continue
                                    Folder_Copy = Folder
                                    SourceFolder_Copy = SourceFolder
                                    TargetFolder_Copy = TargetFolder
                                    MakeDir = Folder_Copy.Replace(SourceFolder_Copy, TargetFolder_Copy)
                                    os.system('mkdir "' +MakeDir +'"')
                                except:
                                    continue
                                TargetFile = TargetFolder +"\\" +File
                                SourceFile = Folder +"\\" +File
                                Junction(SourceFile, TargetFile)
                                print(os.path.getsize(SourceFolder +"\\" +File))
                        except:
                            continue
                    else:
                        Folders.extend([Folder +"\\" +File])
                        print("Folder " +File +" was added to queue!")
                except:
                    continue
        except:
            continue
    return(MovedCounter)

FileFinder(SourceFolder, TargetFolder, MaxSize)
print(str(MovedCounter) +" files were moved!")