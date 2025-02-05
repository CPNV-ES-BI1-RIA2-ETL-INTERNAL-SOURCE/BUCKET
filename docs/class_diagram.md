````mermaid
classDiagram
    class CloudProvider {
        <<Interface>>        
        + connect() void
        + disconect() void
        + load(source : string) void
    }
    
    class CloudProviderFactory {
        + getCloudProvider(url : string) CloudProvider
    }
    
    CloudProvider <|-- AwsProvider
    class AwsProvider {
        - connectionString : string
        - destinationName : string
        - accessKey : string
        - secretKey : string
        - bucket : string
        - region_name : string
        - connection : boto3

        + AwsProvider(accessKey : string, secretKey : string, bucket : string, region : string, destination: string)
        + connect() void 
        + disconect() void
        + load(source : string) void        
    }
    
    DestinationNotFoundException <-- CloudProvider
    class DestinationNotFoundException {
        DestinationNotFoundException()
    }
    
    ObjectAlreadyExistException <-- CloudProvider
    class ObjectAlreadyExistException {
        ObjectAlreadyExistException()
    }
    
    AuthenticationFailedException <-- CloudProvider
    class AuthenticationFailedException {
        AuthenticationFailedException()
    }
    
    EnvironmentVariableException <-- CloudProvider
    class EnvironmentVariableException {
        EnvironmentVariableException()
    }

    AwsProvider --> boto3
    
    
    JobRequest <|-- BaseModel
    class JobRequest {
    + data: str
    + dataDestination: str
    }
    
    JobResponse <|-- BaseModel
    class JobResponse {
    + url: str
    }
    
````