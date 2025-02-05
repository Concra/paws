from requests import Response, post, get, request
from requests.auth import HTTPBasicAuth

from config.constants import BLIZZARD_API_BASE_TOKEN_URL


def get_blizz_bearer_token(client_id: str, client_secret: str) -> Response:
    """Get a bearer token from the Blizzard API.
    
    Args:
        client_id (str): The client ID for the Blizzard API.
        client_secret (str): The client secret for the Blizzard API.

    Returns:
        str: The bearer token.

    """
    url = BLIZZARD_API_BASE_TOKEN_URL
    data = {
        "grant_type": "client_credentials"
    }
    response = post(url, auth=HTTPBasicAuth(client_id, client_secret), data=data)
    return response