from datetime import datetime
from azure.identity import ClientSecretCredential
from Models.AzureBlob import AzureBlob

class AzureStorageBroker(object):
    
    def __init__(
            self, 
            # credential:ClientSecretCredential,
            credential,
            storageAccount:str, 
            container:str
        ) -> None:
        self.credential = credential
        self.storageAccount = storageAccount
        self.container = container
        self.accountUrl = "https://{0}.blob.core.windows.net".format(storageAccount)


    # def GetBlobs(self,):
    #     from azure.storage.blob import BlobServiceClient
    #     blob_service_client = BlobServiceClient(account_url=self.accountUrl, credential=self.credential)
    #     container_client = blob_service_client.get_container_client(container=self.container)
    #     return container_client.list_blobs()

    def GetBlob(self) -> AzureBlob:
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=self.accountUrl, credential=self.credential)
        container_client = blob_service_client.get_container_client(container=self.container)
        blobs = container_client.list_blobs()
        blob = blobs.next()
        blobClient = blob_service_client.get_blob_client(container=self.container,blob=blob.name) #type: ignore
        return AzureBlob(blob.name, blobClient.download_blob().content_as_bytes()) #type: ignore

    def UploadBlob(self, blobName: str, blobBytes:bytes) -> str:
        today = datetime.now() 
        newBlobName = "{0}.{1}.csv".format(blobName,today.strftime("%Y%m%d%H%M%S"))
        from azure.storage.blob import BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=self.accountUrl, credential=self.credential)
        blobClient = blob_service_client.get_blob_client(container=self.container,blob=newBlobName)
        blobClient.upload_blob(blobBytes)
        return newBlobName