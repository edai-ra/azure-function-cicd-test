import logging
import os
import azure.functions as func
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core import Workspace
from azureml.pipeline.core.pipeline_endpoint import PipelineEndpoint

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
