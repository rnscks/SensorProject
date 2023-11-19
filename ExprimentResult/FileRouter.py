import util
import os
from typing import Optional

class FileRouter:
    def __init__(self) -> None:
        self.FileName:str = "ExprimentReuslt"
        self.Numbering: int = 1
        self.MaxNumbering: int = 16
        pass
    
    def GetFilePath(self) -> Optional[str]:
        if (self.Numbering > self.MaxNumbering):
            return None
        currentLocation = os.path.abspath(__file__)
        currentDirName = os.path.dirname(currentLocation)
        filePath = os.path.join(currentDirName, str(self.Numbering)+self.FileName + '.xlsx')
        self.Numbering += 1
        
        return filePath
