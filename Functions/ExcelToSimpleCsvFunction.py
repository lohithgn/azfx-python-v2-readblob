import json
import azure.functions as func
import logging
from Models.ExcelToCsvRequest import ExcelToCsvRequest
from Orchestrators.ExcelToCsvOrchestrator import ExcelToCsvOrchestrator
import humps

#Create blueprint
bp = func.Blueprint()

# Define HttpTriggered function ExcelToSimpleCsvFunction
# Route: https://<funcappname>.azurewebsites.net/api/simplecsv
@bp.function_name(name="ExcelToSimpleCsvFunction")
@bp.route(route="simplecsv", auth_level=func.AuthLevel.ANONYMOUS, methods=["Post"])
def excelToSimpleCsvFunction(req: func.HttpRequest) -> func.HttpResponse:
    
    logging.info('ExcelToSimpleCsvFunction function processed a request.')
    
    # Parse payload
    logging.info('Parsing payload')
    request = ParseSimpleCsvPayload(req)    

    # Read excel, transform to simple csv    
    orchestrator = ExcelToCsvOrchestrator()
    response = orchestrator.ToSimpleCsv(request)

    # Prepare response payload
    jsonData = json.dumps(humps.camelize(response.dict()))
    return func.HttpResponse(body=jsonData,mimetype="application/json")

def ParseSimpleCsvPayload(req:func.HttpRequest) -> ExcelToCsvRequest:
    payload = req.get_json()
    return ExcelToCsvRequest(
        SourceStorageAccountName=payload.get("sourceStorageAccountName"),
        SourceContainerName=payload.get("sourceContainerName"),
        TargetStorageAccountName=payload.get("targetStorageAccountName"),
        TargetContainerName=payload.get("targetContainerName")
    )