from __future__ import annotations
from pathlib import PurePosixPath, Path

class account_path(PurePosixPath):
    def __init__(self, x: str = None):
        if x is None:
            x = ""
        if len(x) > 0 and x[0] == "/":
            x = x[1:]
        #self.path = x
        #self.parts = x.split("/")[1:]
        #self.root = self.parts[0]
        #self.folder = self.parts[1 if not self.is_singleton else 0]
        #self.name = self.parts[-1]
        
    @property
    def is_singleton(self):
        return len(self.parts) == 1
    
    @property
    def root_folder(self):
        return self.parts[0]

    def get_child(self) -> account_path:
        return account_path('/'.join(self.parts[1:]))

