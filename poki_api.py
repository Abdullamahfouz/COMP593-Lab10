import requests
import image_lib
import os
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
# Test out the get_pokemon_into() function
# Use breakpoints to view returned dictionary


def main():
    
 names = get_pokemon_names()
    
    # testing function
 get_pokemon_image('dugtrio',
      r'C:\Users\Abdullah\OneDrive\Desktop\New Computer\COMP593-Lab10' )
 return
    
def get_pokemon_info(pokemon_name):

    """Gets information about a specified Pokemon from the PokeAPI.
 
      Args:
        pokemon_name (str): Pokemon name (or Pokedex number)
 
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    # Clean the Pokemon name parameter by:
    # - Converting to a string object, 
    # - Removing leading and trailing whitespace, and
    # - Converting to all lowercase letters
    pokemon_name = str(pokemon_name).strip().lower()
 
    # Build the clean URL for the GET request
    url = POKE_API_URL + pokemon_name
 
    # Send GET request for Pokemon info
    print(f'Getting information for {pokemon_name}...', end='')
    resp_msg = requests.get(url)
 
    # Check if request was successful
    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')   
        return None      
        
def get_pokemon_names(offest=0, limit=100000):
    """Sends a GET request to the PokeAPI to get a list of all Pokemon names.

    Args:
        offset : The starting index of the results to return starting from 0.
        limit : The maximum number of results to return to is 100000.

    Returns:
        list: A list of Pokemon names.
        Returns None if the GET request fails.
    """
    
    quer_str_params= {
      'offset': offest,
      'limit' : limit
      }
    print("getting poke names")

    # Send a request to the PokeAPI
    resp_msg = requests.get(POKE_API_URL, params=quer_str_params)
  
    # JSON response and return the list of names
    if resp_msg.status_code == requests.codes.ok:
        print('success ')
        pokemon_dict = resp_msg.json()
        poke_names_list = [p['name'] for p in pokemon_dict['results']]
        return poke_names_list
   # if Failure it will print the status code and return None
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return

def get_pokemon_image(pokemon_name, save_dir):
    """
    Uses the PokeAPI to get the  image for a specified Pokemon, downloads the image,
    and saves it to a directory.

    Args:
        pokemon_name (str): The name of the Pokemon to retrieve the image.
        save_dir (str): The directory to save the downloaded image to.

    Returns:
        str: The file path of the saved image, if the image was downloaded and saved successfully. Returns None
        if the GET request or image download fails.
    """
  
  #Get all info for the specified pokemon
    pokemon_info = get_pokemon_info(pokemon_name)
    
    # Pokemon not found it will return None.
    if pokemon_info is None :
        return
    
     #Get the url of the official artwork image for the pokemon
    artwork_url = pokemon_info['sprites']['other']['official-artwork']['front_default']
    
    # Download the image and save it to a file
    image_bytes = image_lib.download_image(artwork_url)
    
    # Image not found it will return None.
    if image_bytes is None:
        return
    # Get the file extension of the image
    file_ext = artwork_url.split('.')[-1]
    # the file path to save the image to
    image_path = os.path.join(save_dir, f'{pokemon_name}.{file_ext}' )
   
    
    # Save the image file and return the file path if successful
    if image_lib.save_image_file(image_bytes, image_path ):
        return image_path

if __name__ == '__main__':
    main()