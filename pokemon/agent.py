from strands import Agent, tool
from strands_tools import calculator, current_time
import requests

@tool
def get_pokemon_info(name: str) -> dict:
    """
    Get information about a Pokémon.

    Args:
        name (str): The name of the Pokémon to get information about

    Returns:
        dictionary with the Pokémon information
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    return response.json()

@tool
def get_ability_info(ability: str) -> dict:
    """
    Get information about a Pokémon ability.

    Args:
        ability (str): The name of the Pokémon ability to get information about

    Returns:
        dictionary with the Pokémon ability information
    """
    response = requests.get(f"https://pokeapi.co/api/v2/ability/{ability}")
    return response.json()

@tool
def get_species_info(pokemon_id: int) -> dict:
    """
    A Pokémon Species forms the basis for at least one Pokémon. Attributes of a Pokémon species are shared across all varieties of Pokémon within the species.

    Args:
        pokemon_id (int): The ID of the Pokémon to get information about

    Returns:
        dictionary with the Pokémon species information
    """
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}")
    return response.json()

@tool
def get_evolution_chain(chain: int) -> dict:
    """
    Get information about a Pokémon evolution chain.

    Args:
        chain (int): The ID of the Pokémon evolution chain to get information about

    Returns:
        dictionary with the Pokémon evolution chain information
    """
    response = requests.get(f"https://pokeapi.co/api/v2/evolution-chain/{chain}")
    return response.json()

agent = Agent(tools=[get_pokemon_info, get_ability_info, get_species_info, get_evolution_chain])

# Ask the agent a question that uses the available tools
message = """
I have 2 request:

1. List the evolution chain of Xerneas
2. Get information about all the abilities of the Pokémon Whirlipede
"""
agent(message)