from fastapi import APIRouter, HTTPException, Query
from app.cloud_provider.cloud_provider_factory import CloudProviderFactory
from app.schemas.requests.load_request import LoadRequest
from app.schemas.responses.load_response import LoadResponse
from app.schemas.responses.list_response import ListResponse
from app.exceptions.destination_not_found_exception import DestinationNotFoundException

router = APIRouter()
apiPrefix = "/api/v2"

@router.post(apiPrefix + '/objects', response_model=LoadResponse)
def load_object(request: LoadRequest):
    try:
        provider = CloudProviderFactory().get_cloud_provider(request.uri)

        provider.connect()
        url = provider.load(data=request.data)

        return LoadResponse(url=url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")