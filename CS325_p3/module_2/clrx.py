# clrx_module: Clorox Module

    # Input: Takes in Raw User String Data or python obj

    # Output: Clean/parsed/serialized String Data, Ready to Use

    # Usage: Clean User Srings (URL page parse, File Extension Parse, unicode to ASCII and back) or Get Sanitized Serialized Python Objects

# Dependencies
    # Standard Module(s)
import re
    # Installed Module(s)
import jsonpickle
    # Local Module(s)

###### ###### ###### ###### ######
###### Interface For clrx   ######
###### ###### ###### ###### ######

# Parse file name and remove extension
def RemoveFileExt(filename: str) -> str:
    if extSnip := re.sub(r".[a-zA-Z0-9]+$", "", filename):
        return extSnip
    else:
        return filename

# Encode Unicode Text
def SanitizeText(text: str) -> str:
    #newText = re.sub(r"&#[0-9a-zA-Z]+;", "", text)
    newText = text.encode("ascii", "ignore")
    return str(newText)

# Revert Unicode Encoding
def UnSanitizeText(text: str) -> str:
    newText = text.decode("ascii", "ignore")
    return str(newText)

# Parse url for the page name
def GetURLPage(url: str) -> str:
    if protoSnip := re.sub(r"^https{0,1}|://|www.|reddit|.com|/r/|/|/$", "", url):
        return protoSnip
    else:
        return url

# Parse FileName for ID
def GetFileID(fileName: str) -> str:
    if idSnip := re.sub(r"^post-|-comments|-sentiments|.[a-zA-Z0-9]+$", "", fileName):
        return idSnip

# Convert any python class object to a properly Sanitized and Serialized JSON String
def ToJSON(obj, isIndented: bool = True) -> str:
    try:
        jsonpickle.set_encoder_options('json')
        if isIndented:
            return jsonpickle.encode(obj, keys = True, indent=4, separators=(',', ': '))
        else:
            return jsonpickle.encode(obj, keys = True)
    except Exception as e:
        print("Redder ran into unexpected issues encoding python object to JSON!")
        raise e