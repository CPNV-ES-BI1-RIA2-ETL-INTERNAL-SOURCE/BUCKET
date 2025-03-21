import os
from dotenv import load_dotenv, find_dotenv

from app.exceptions.environement_variables_exception import EnvironmentVariableException


def get_env_variables(file=".env", variables=None):
    """
    Loads environment variables from the system or an .env file and checks that all required variables are present.

    :param file: The path of the .env file (default “.env”).
    :param variables: A list of required environment variable names.
    :return: Dictionary of loaded environment variables.
    :raises ValueError: If one of the required variables is missing.
    """

    dotenv_path = find_dotenv(file)
    if dotenv_path:
        load_dotenv(dotenv_path)

    if variables is None:
        variables = []

    variables_missing = []

    env_variables = {}
    for var in variables:
        value = os.getenv(var)
        if value:
            env_variables[var] = value
        else:
            variables_missing.append(var)

    if variables_missing:
        raise EnvironmentVariableException(
            f"The following variables are missing: {', '.join(variables_missing)}"
        )

    return env_variables