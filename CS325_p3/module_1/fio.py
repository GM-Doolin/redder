# fio_module: File-Input-Ouput Module

    # Input: Takes in File Name String Data

    # Output: Write File or Return Read File Data

    # Usage: Easily Read and Write Local Files For Redder

# Dependencies
    # Standard Module(s)
import csv
import os
    # Installed Module(s)
    
    # Local Module(s)

###### ###### ###### ###### ######
###### Interface For fio    ######
###### ###### ###### ###### ######

# Write file "redder\CS325_p3\Data\subFolder\filename.fileExt"
def WriteDataFile(fileName: str, dta: str, subfolder: str, fileExt: str = "json") -> None:
    try:
        file = open("Data\\" + subfolder + "\\" + fileName + "." + fileExt, "w", encoding = "utf-8")
        file.write(dta)
        file.close()
    except Exception as e:
        raise e

# Write file "redder\CS325_p3\Data\subFolder\filename.fileExt" in CSV format
def WriteCSVFile(fileName: str, list: [], subfolder: str, fileExt: str = "txt") -> None:
    try:
        file = open("Data\\" + subfolder + "\\" + fileName + "." + fileExt, "w", encoding = "utf-8")
        sentimentWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for item in list:
            sentimentWriter.writerow(item)
        file.close()
    except Exception as e:
        raise e
    
# Read file "redder\CS325_p3\Data\subFolder\fileName.fileExt", return str
def ReadDataFile(fileName: str, subfolder: str, fileExt: str = "json") -> str:
    try:
        file = open("Data\\" + subfolder + "\\" + fileName + "." + fileExt, "r", encoding = "utf-8")
        dta = file.read()
        file.close()
        return dta
    except Exception as e:
        raise e

# Read Local System File, return str
def ReadFile(fileName: str) -> str:
    try:
        file = open(fileName, "r", encoding = "utf-8")
        dta = file.read()
        file.close()
        return dta
    except Exception as e:
        raise e

# Retrieve list of data file names (str) from of redder's data subfolder located in "redder\CS325_p3\Data\subfolder\"
def GetDataFiles(subfolder: str) -> []:
    try:
        files = []
        dir = "Data\\" + subfolder + "\\"
        for file in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, file)):
                files.append(file)
        return files
    except Exception as e:
        raise e
