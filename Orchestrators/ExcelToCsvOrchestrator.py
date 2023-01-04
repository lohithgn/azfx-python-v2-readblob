import logging
from Brokers.AuthenticationBrokers import AzureAuthenticator
from Brokers.StorageBrokers import AzureStorageBroker
from Brokers.FileBrokers import ExcelBroker
from Models.ExcelToCsvRequest import ExcelToCsvRequest
from Models.ExcelToCsvResponse import ExcelToCsvResponse

class ExcelToCsvOrchestrator(object):
    def ToSimpleCsv(self,request: ExcelToCsvRequest) -> ExcelToCsvResponse:
        # Authenticate with SP & get token
        logging.info('Authenticating default credentials')
        credential = AzureAuthenticator().Authenticate()
        
        # Get Blobs on container, grab first one
        logging.info('Get source blob')
        sourceStorage = AzureStorageBroker(credential,request.SourceStorageAccountName,request.SourceContainerName)
        blob = sourceStorage.GetBlob() #type: ignore
        
        # Read excel - sheet 0, convert to csv bytes
        logging.info('Read excel & convert to Csv')
        excelFileBroker = ExcelBroker()
        csvBytes = excelFileBroker.ReadAndTransformToCsv(blob.Data)

        # Upload csv to target container as blob
        logging.info('Upload csv to Target')
        targetStorage = AzureStorageBroker(credential,request.TargetStorageAccountName,request.TargetContainerName)
        targetBlobName = targetStorage.UploadBlob(blobName=blob.Name, blobBytes=csvBytes) #type: ignore
        
        return ExcelToCsvResponse(Source=blob.Name, Target=targetBlobName, Transformed=True)

    def ToPivotCsv(self,request: ExcelToCsvRequest) -> ExcelToCsvResponse:
            # Authenticate with SP & get token
            logging.info('Authenticating default credentials')
            credential = AzureAuthenticator().Authenticate()
            
            # Get Blobs on container, grab first one
            logging.info('Get source blob')
            sourceStorage = AzureStorageBroker(credential,request.SourceStorageAccountName,request.SourceContainerName)
            blob = sourceStorage.GetBlob() #type: ignore
            
            # Read excel - sheet 0, convert to csv bytes
            logging.info('Read excel & convert to Csv')
            excelFileBroker = ExcelBroker()
            csvBytes = excelFileBroker.ReadAndTransformToPivotCsv(blob.Data, request.NonPivotColumns, request.PivotColumnName, request.PivotValueColumnName)

            # Upload csv to target container as blob
            logging.info('Upload csv to Target')
            targetStorage = AzureStorageBroker(credential,request.TargetStorageAccountName,request.TargetContainerName)
            targetBlobName = targetStorage.UploadBlob(blobName=blob.Name, blobBytes=csvBytes) #type: ignore
            
            return ExcelToCsvResponse(Source=blob.Name, Target=targetBlobName, Transformed=True)