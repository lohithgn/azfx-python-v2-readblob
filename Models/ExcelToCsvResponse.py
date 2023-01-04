from dataclasses import dataclass

@dataclass
class ExcelToCsvResponse:
    Source:str
    Target:str
    Transformed:bool

    def dict(self):
        return self.__dict__