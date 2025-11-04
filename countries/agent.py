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
        dictionary with the country information
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
        list of dictionaries
    """
    response = requests.get(f"https://restcountries.com/v3.1/region/{region}")
    return response.json()

@tool
def list_by_language(language: str) -> list:
    """
    List all the countries that have a specific language as an official language.

    Args:
        language (str): The name of the language to list all the countries that have as an official language

    Returns:
        list of dictionaries
    """
    response = requests.get(f"https://restcountries.com/v3.1/lang/{language}")
    return response.json()

agent = Agent(tools=[get_country_info, list_by_region, list_by_language])

message = """
I have 4 requests:

1. What is the capital of France?
2. List the countries in the region of South America
3. What is the population of Brazil?
4. List all the countries that have Spanish as an official language
"""
agent(message)
