# fio_module: File-Input-Ouput Module

    # Input: Takes in File Name String Data

    # Output: Write File or Return Read File Data

    # Usage: Easily Read and Write Local Files For Redder

###### ###### ###### ###### ######
###### Interface For fio    ######
###### ###### ###### ###### ######

# Write file "Data\subFolder\filename.fileExt"
def WriteDataFile(fileName: str, dta: str, subFolder: str, fileExt: str = "json") -> None:
    try:
        file = open("Data\\" + subFolder + "\\" + fileName + "." + fileExt, "w", encoding = "utf-8")
        file.write(dta)
        file.close()
    except Exception as e:
        raise e
    
# Read file "Data\subFolder\fileName.fileExt", return str
def ReadDataFile(fileName: str, subFolder: str, fileExt: str = "json") -> str:
    try:
        file = open("Data\\" + subFolder + "\\" + fileName + "." + fileExt, "r", encoding = "utf-8")
        dta = file.read()
        file.close()
        return dta
    except Exception as e:
        raise e