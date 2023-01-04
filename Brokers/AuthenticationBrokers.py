from azure.identity import DefaultAzureCredential

class AzureAuthenticator(object):
    
    def Authenticate(self):
        # In Prod - Use Managed Identity & DefaultCredential
        return DefaultAzureCredential()