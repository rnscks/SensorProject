
import os
from typing import Optional

class FileRouter:
    def __init__(self, folderName) -> None:
        self.FolderName:str = folderName
        self.FileName:str = "ExprimentReuslt"
        self.Numbering: int = 1
        self.MaxNumbering: int = 16
        pass
    
    def GetFilePath(self) -> Optional[str]:
        if (self.Numbering > self.MaxNumbering):
            return None
        currentLocation = os.path.abspath(__file__)
        currentDirName = os.path.dirname(currentLocation)
        folderPath = os.path.join(currentDirName, self.FolderName)
        filePath = os.path.join(folderPath, str(self.Numbering)+self.FileName + '.xlsx')
        self.Numbering += 1
        
        return filePath
