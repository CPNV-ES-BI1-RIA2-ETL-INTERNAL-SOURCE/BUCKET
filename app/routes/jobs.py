from fastapi import APIRouter, HTTPException
from app.cloud_provider.cloud_provider_factory import CloudProviderFactory
from app.schemas.requests.job_request import JobRequest
from app.schemas.responses.job_response import JobResponse

router = APIRouter()

@router.post('/job', response_model=str)
def job(request: JobRequest):
    try:
        provider = CloudProviderFactory().get_cloud_provider(request.dataDestination)

        provider.connect()

        url = provider.load(data=request.data)

        return url

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")