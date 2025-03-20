````mermaid
classDiagram
    class CloudProvider {
        <<Interface>>        
        + connect() void
        + disconnect() void
        + load(source : string, destination : string) void
        + list(recurse : bool) string[]
    }
    
    class CloudProviderFactory {
        + getCloudProvider(url : string) CloudProvider
    }
    
    CloudProvider <|-- AwsProvider
    class AwsProvider {
        - connectionString : string
        - accessKey : string
        - secretKey : string
        - bucket : string
        - region_name : string
        - connection : boto3

        + AwsProvider(accessKey : string, secretKey : string, bucket : string, region : string, destination: string)
        + connect() void 
        + disconnect() void
        + load(source : string, destination: string) string
        + list(recurse : bool) string[]
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
    
    
    LoadRequest <|-- BaseModel
    class LoadRequest {
    + data: string
    + uri: string
    }
    
    LoadResponse <|-- BaseModel
    class LoadResponse {
    + url: string
    }
    
    ListResponse <|-- BaseModel
    class ListResponse {
    + objects: string[]
    }
````