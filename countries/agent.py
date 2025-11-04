from strands import Agent, tool
from strands_tools import calculator, current_time
import requests

@tool
def get_country_info(country: str) -> str:
    """
    Get information about a country.

    Args:
        country (str): The name of the country to get information about

    Returns:
        name: dictionary containing:
            common: str
            official: str
            nativeName: dictionary containing:
                [language]: dictionary containing:
                    common: str
                    official: str
    """
    response = requests.get(f"https://restcountries.com/v3.1/name/{country}")
    return response.json()[0]

@tool
def list_by_region(region: str) -> list:
    """
    List all the countries in a region.

    Args:
        region (str): The name of the region to list all the countries from

    Returns:
        list of dictionaries containing:
            name: dictionary containing:
                common: str
                official: str
            nativeName: dictionary containing:
                [language]: dictionary containing:
                    common: str
                    official: str
    """
    response = requests.get(f"https://restcountries.com/v3.1/region/{region}")
    return response.json()

agent = Agent(tools=[get_country_info, list_by_region])

message = """
I have 2 requests:

1. What is the capital of France?
2. List the countries in the region of South America
"""
agent(message)
