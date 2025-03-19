````mermaid
sequenceDiagram
    Actor API
    API ->>+ main : 
    main ->>+ CloudProviderFactory : get_cloud_provider()
    activate CloudProviderFactory
    CloudProviderFactory -->>- main : provider response CloudProvider
    
    main ->>+ AwsProvider : connect()
    activate AwsProvider
    main ->>- AwsProvider : load(string)
    AwsProvider ->>+ boto3 : put_object(string)
    activate boto3
    boto3 -->>- AwsProvider : sdk response
    AwsProvider -->> main : response
    

    activate main
    main ->>+ AwsProvider : connect()
    activate AwsProvider
    main ->>- AwsProvider : list(bool)
    AwsProvider ->>+ boto3 : list_objects_v2()
    activate boto3
    boto3 -->>- AwsProvider : sdk response (list of objects)
    AwsProvider -->> main : response (list of objects)
````