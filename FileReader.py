
import pandas as pd
from typing import Optional
from FileRouter import FileRouter



class FileReader:
    def __init__(self) -> None:
        self.file_router = FileRouter("ExprimentResult")
        pass
    
    def ReadFile(self) -> Optional[pd.DataFrame]:
        
        filePath:str = self.file_router.GetFilePath()
        
        if (filePath == None):
            return None
        
        return pd.read_excel(filePath, header=0)
            
    
if (__name__ =="__main__"):
    fr = FileReader()
    
    result = fr.ReadFile()
    result = fr.ReadFile()

        