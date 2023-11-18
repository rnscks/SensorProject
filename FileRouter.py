import os
from typing import Optional

class FileRouter:
    def __init__(self, folderName) -> None:
        """
        Initializes a new instance of the FileRouter class.

        Args:
        folderName (str): The name of the folder where the file will be saved.
        """
        self.FolderName:str = folderName
        self.FileName:str = "ExprimentReuslt"
        self.Numbering: int = 1
        self.MaxNumbering: int = 16
        pass
    
    def GetFilePath(self) -> Optional[str]:
        """
        Gets the file path for the next file to be saved.

        Returns:
        Optional[str]: The file path for the next file to be saved, or None if the maximum number of files has been reached.
        """
        if (self.Numbering > self.MaxNumbering):
            return None
        currentLocation = os.path.abspath(__file__)
        currentDirName = os.path.dirname(currentLocation)
        folderPath = os.path.join(currentDirName, self.FolderName)
        filePath = os.path.join(folderPath, str(self.Numbering)+self.FileName + '.xlsx')
        self.Numbering += 1
        
        return filePath
