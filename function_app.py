import azure.functions as func

#Import functions
from Functions.ExcelToSimpleCsvFunction import bp as excelToSimpleCsvFunction
from Functions.ExcelToPivotCsvFunction import bp as excelToPivotCsvFunction

# Create function app
app = func.FunctionApp()

# register functions with the function app
app.register_functions(excelToSimpleCsvFunction)
app.register_functions(excelToPivotCsvFunction)



























# @app.function_name(name="ExcelToSimpleCsvFunction")
# @app.route(route="simplecsv", auth_level=func.AuthLevel.FUNCTION, methods=["Post"])
# def excelToSimpleCsvFunction(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('ExcelToSimpleCsvFunction function processed a request.')

#     logging.info('Parsing payload')
    
#     # Parse payload
#     request = ParseSimpleCsvPayload(req)    

#     # Read excel, transform to simple csv    
#     orchestrator = ExcelToCsvOrchestrator()
#     response = orchestrator.ToSimpleCsv(request)

#     # Prepare response payload
#     jsonData = json.dumps(humps.camelize(response.dict()))
#     return func.HttpResponse(body=jsonData,mimetype="application/json")

# https://<funcappname>.azurewebsites.net/api/pivotcsv
# @app.function_name(name="ExcelToPivotCsvFunction")
# @app.route(route="pivotcsv", auth_level=func.AuthLevel.FUNCTION, methods=["Post"])
# def excelToPivotCsvFunction(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('ExcelToPivotCsvFunction function processed a request.')

#     logging.info('Parsing payload')
    
#     # Parse payload
#     request = ParsePivotCsvPayload(req)    

#     # Read excel, transform to simple csv    
#     orchestrator = ExcelToCsvOrchestrator()
#     response = orchestrator.ToPivotCsv(request)

#     # Prepare response payload
#     jsonData = json.dumps(humps.camelize(response.dict()))
#     return func.HttpResponse(body=jsonData,mimetype="application/json")

# def ParseSimpleCsvPayload(req:func.HttpRequest) -> ExcelToCsvRequest:
#     payload = req.get_json()
#     return ExcelToCsvRequest(
#         SourceStorageAccountName=payload.get("sourceStorageAccountName"),
#         SourceContainerName=payload.get("sourceContainerName"),
#         TargetStorageAccountName=payload.get("targetStorageAccountName"),
#         TargetContainerName=payload.get("targetContainerName")
#     )

# def ParsePivotCsvPayload(req:func.HttpRequest) -> ExcelToCsvRequest:
#     payload = req.get_json()
#     return ExcelToCsvRequest(
#         SourceStorageAccountName=payload.get("sourceStorageAccountName"),
#         SourceContainerName=payload.get("sourceContainerName"),
#         TargetStorageAccountName=payload.get("targetStorageAccountName"),
#         TargetContainerName=payload.get("targetContainerName"),
#         Pivot=payload.get("pivot"),
#         NonPivotColumns=payload.get("nonPivotColumns"),
#         PivotColumnName=payload.get("pivotColumnName"),
#         PivotValueColumnName=payload.get("pivotValueColumnName")
#     )
