# Dependencies
    # Standard Lib(s)
import re
    # Installed Lib(s)
    # Local Module(s)

###### ###### ###### ###### ######
###### Interface For clrx   ######
###### ###### ###### ###### ######

# Helper class for cleaning/parsing string data
class clrx:

    # Encode Unicode Text
    @staticmethod
    def SanitizeText(text: str) -> str:
        #newText = re.sub(r"&#[0-9a-zA-Z]+;", "", text)
        newText = text.encode("ascii", "ignore")
        return str(newText)

    # Revert Unicode Encoding
    @staticmethod
    def UnSanitizeText(text: str) -> str:
        newText = text.decode("ascii", "ignore")
        return str(newText)
        
    @staticmethod
    def IsParentId(id: str) -> bool:
        if parentMatch := re.match(r"t1_", id):
            return True
        else:
            return False
