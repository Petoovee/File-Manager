# Imports
import os, re
os.system('cls')

# Variables
SourceFolder = input("\nFrom which folder do you wish me to move the files?\n")
TargetFolder = input("\nTo which folder do you wish me to move the files?\n")
MaxSize = int(input("\nMinimum size (MB) of file to move? \n")) *1048576
SourceFiles = "a"
TargetFiles = "b"
MovedCounter = int(0)
TargetCounter = 0

# Move file
def Junction (SourceFile, TargetFile):
    global MovedCounter
    MovedCounter = MovedCounter + 1
    os.system('move "' +SourceFile +'" "' +TargetFile +'"')
    print(TargetFile +" was moved")
    os.system('mklink "' +SourceFile +'" "' +TargetFile +'"')

# Finds the files to be moved, and finds where to put them
def FileFinder (SourceFolder, TargetFolder, MaxSize):
    Folders = [SourceFolder]
    print(SourceFolder)
    for Folder in Folders:
        # print("Looking in " +Folder)
        for File in os.listdir(Folder):
            if os.path.isfile(Folder +"\\" +File) is True:
                if os.path.islink(Folder +"\\" +File) is False:
                    if (os.path.getsize(Folder +"\\" +File)>MaxSize):
                        # This way the folder is only made in case the file is actually getting moved
                        # and if it already exists it will only error out and continue
                        Folder_Copy = Folder
                        SourceFolder_Copy = SourceFolder
                        TargetFolder_Copy = TargetFolder
                        MakeDir = Folder_Copy.replace(SourceFolder_Copy, TargetFolder_Copy)
                        # print(MakeDir)
                        os.system('mkdir "' +MakeDir +'"')
                        TargetFile = MakeDir +"\\" +File
                        SourceFile = Folder +"\\" +File
                        Junction(SourceFile, TargetFile)
                else:
                    print("Skipping .symlink")
            else:
                Folders.extend([Folder +"\\" +File])
                # print("Folder " +Folder +"\\" +File +" was added to queue!")

FileFinder(SourceFolder, TargetFolder, MaxSize)
print(MovedCounter, " files were moved!")