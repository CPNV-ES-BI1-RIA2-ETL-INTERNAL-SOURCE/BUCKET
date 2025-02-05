# Chosen technologies

This document explain why each technology has been used. 

---
# Python

Python is used cause :
- Large Ecosystem of Libraries and Tools
- Flexibility and integration with various systems
- Active community
- Support for Cloud Environments

---
# Libs 

## pytest and unittest 
Although `unittest` is the standard test framework supplied with Python, `pytest` was also chosen because : 
- Fixture support
- Parameterization
- Rich plugin architecture
- Concise syntax

And unittest.mock is used to mock services.

>It is known for its simplicity, scalability, and ability to handle complex test scenarios while significantly reducing the boilerplate code required for testing.
> --- <cite>[jetbrains][1]</cite>


[1] : https://blog.jetbrains.com/pycharm/2024/03/pytest-vs-unittest/

## fastapi
Very popular Python for developing fast, modern web APIs.
- Simplicity
- Intuitive 
- Native asynchronous support

[Official doc](https://fastapi.tiangolo.com/)

Using routes : 
Explanation of changes
Router (routes.py):

We've moved the /load route into an APIRouter to better organize routes and avoid overloading the Server class.
The router now contains the /load route, and this approach allows for better scalability.
Server (server.py):

Server now includes the router with self.app.include_router(router), making it easy to add new routes in the future.
The Server class remains responsible for managing the FastAPI instance, as well as connecting and disconnecting the cloud service.

## google-cloud-storage
Official library to connect to google cloud storage.

[Official doc](https://cloud.google.com/storage/docs/reference/libraries)

## boto3
Chosen because it is the official library for python.

> Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. You can find the latest, most up to date, documentation at our doc site, including a list of services that are supported.
> -- <cite>[Amazon][2]


[2] : https://github.com/boto/boto3


## Uvicorn
Uvicorn is a lightweight, high-performance ASGI (Asynchronous Server Gateway Interface) server designed to run modern Python applications such as FastAPI or Starlette. 

Finally, I use fastapi directly, which will itself create a server without needing Unicorn.