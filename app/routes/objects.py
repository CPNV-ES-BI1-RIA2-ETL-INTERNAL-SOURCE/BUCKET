from fastapi import APIRouter, HTTPException, Query, File, UploadFile
from app.cloud_provider.cloud_provider_factory import CloudProviderFactory
from app.schemas.requests.load_request import LoadRequest
from app.schemas.responses.load_response import LoadResponse
from app.schemas.responses.list_response import ListResponse
from app.exceptions.destination_not_found_exception import DestinationNotFoundException
from app.services.environement_variables import get_env_variables

router = APIRouter()

@router.post('/objects', response_model=LoadResponse)
async def load_object(destination: str, file: UploadFile = File(...)):
    try:
        variables = get_env_variables(variables=["PROVIDER"])
        provider = CloudProviderFactory().get_cloud_provider(variables["PROVIDER"])
        provider.connect()

        file_content = await file.read()

        url = provider.load(data=file_content, destination=destination)

        return LoadResponse(url=url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")

@router.get('/objects', response_model=ListResponse)
def list_objects(
    recurse: bool = Query(False, description="Whether to list objects recursively")
):
    try:
        variables = get_env_variables(variables=["PROVIDER"])

        provider = CloudProviderFactory().get_cloud_provider(variables["PROVIDER"])
        provider.connect()
        objects = provider.list(recurse=recurse)
        return ListResponse(objects=objects)
    except DestinationNotFoundException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")