import json
import azure.functions as func
import logging
from Models.ExcelToCsvRequest import ExcelToCsvRequest
from Orchestrators.ExcelToCsvOrchestrator import ExcelToCsvOrchestrator
import humps

bp = func.Blueprint()

# Define HttpTriggered function ExcelToSimpleCsvFunction
# Route: https://<funcappname>.azurewebsites.net/api/pivotcsv
@bp.function_name(name="ExcelToPivotCsvFunction")
@bp.route(route="pivotcsv", auth_level=func.AuthLevel.FUNCTION, methods=["Post"])
def excelToPivotCsvFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('ExcelToPivotCsvFunction function processed a request.')
    
    # Parse payload
    logging.info('Parsing payload')
    request = ParsePivotCsvPayload(req)    

    # Read excel, transform to pivotted csv    
    orchestrator = ExcelToCsvOrchestrator()
    response = orchestrator.ToPivotCsv(request)

    # Prepare response payload
    jsonData = json.dumps(humps.camelize(response.dict()))
    return func.HttpResponse(body=jsonData,mimetype="application/json")

def ParsePivotCsvPayload(req:func.HttpRequest) -> ExcelToCsvRequest:
    payload = req.get_json()
    return ExcelToCsvRequest(
        SourceStorageAccountName=payload.get("sourceStorageAccountName"),
        SourceContainerName=payload.get("sourceContainerName"),
        TargetStorageAccountName=payload.get("targetStorageAccountName"),
        TargetContainerName=payload.get("targetContainerName"),
        Pivot=payload.get("pivot"),
        NonPivotColumns=payload.get("nonPivotColumns"),
        PivotColumnName=payload.get("pivotColumnName"),
        PivotValueColumnName=payload.get("pivotValueColumnName")
    )