import io
import pandas as pd

class ExcelBroker(object):
    def ReadAndTransformToCsv(self,data:bytes) -> bytes:
        df = pd.read_excel(data,sheet_name=0)
        return bytes(df.to_csv(index=False), encoding='utf-8')

    def ReadAndTransformToPivotCsv(self,data:bytes,nonPivotColumns:str,pivotColumnName:str,pivotValueColumnName:str) -> bytes:
        df = pd.read_excel(data,sheet_name=0)
        nonPivotedColumnsList = list(nonPivotColumns.split(",")) 
        pivotedDf=df.melt(id_vars=(nonPivotedColumnsList),var_name=pivotColumnName , value_name=pivotValueColumnName)
        return bytes(pivotedDf.to_csv(index=False), encoding='utf-8')