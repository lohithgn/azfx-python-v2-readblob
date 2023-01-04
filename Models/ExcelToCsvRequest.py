from dataclasses import dataclass

@dataclass
class ExcelToCsvRequest:
    SourceStorageAccountName:str
    SourceContainerName:str
    TargetStorageAccountName:str
    TargetContainerName:str
    Pivot:bool = False
    NonPivotColumns:str = ""
    PivotColumnName:str = ""
    PivotValueColumnName:str = ""