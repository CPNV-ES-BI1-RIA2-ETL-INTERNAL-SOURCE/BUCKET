import os
from dotenv import load_dotenv, find_dotenv

from app.exceptions.environement_varriables_exception import EnvironmentVariableException


def get_env_variables(file=".env", variables=None):
    """
    Loads environment variables from an .env file and checks that all required variables are present.

    :param file: The path of the .env file (default “.env”).
    :param variables: A list of required environment variable names.
    :return: Dictionary of loaded environment variables.
    :raises ValueError: If one of the required variables is missing.
    """

    dotenv_path = find_dotenv(file)
    if not dotenv_path:
        raise EnvironmentVariableException(f"The file {file} has not been found.")

    load_dotenv(dotenv_path)

    if variables is None:
        variables = []

    variables_missing = []

    for var in variables:
        if not os.getenv(var):
            variables_missing.append(var)

    if variables_missing:
        raise EnvironmentVariableException(
            f"Theses following variables ar missing in the {file} file : {', '.join(variables_missing)}")


    return {var: os.getenv(var) for var in variables}