from __future__ import annotations
from pathlib import PurePosixPath, Path

class account_path(PurePosixPath):
    def __init__(self, x: str = ""):
        if len(x) > 0 and x[0] == "/":
            raise ValueError(f"Do not use a / at the beginning: {x}")

    @property
    def is_empty(self):
        return len(self.parts) == 0

    @property
    def is_singleton(self):
        return len(self.parts) == 1
    
    @property
    def root_folder(self):
        if self.is_empty:
            return None
        return self.parts[0]

    def get_child(self) -> account_path:
        return account_path('/'.join(self.parts[1:]))

