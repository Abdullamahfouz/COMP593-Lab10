import requests
import image_lib
import os
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
# Test out the get_pokemon_into() function
# Use breakpoints to view returned dictionary


def main():
    
    
    
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
        



 
def get_pokemon_names(offest=0, limit=100000):

  quer_str_params= {
      'offset': offest,
      'limit' : limit
    }


  resp_msg = requests.get(POKE_API_URL, params=quer_str_params)
  
  if resp_msg.status_code == requests.codes.ok:
      pokemon_dict = resp_msg.json()
      
      poke_names_list = [p['names'] for p in pokemon_dict['results']]
      
      return poke_names_list
  else:
      print('failure')
      print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
      return
def get_pokemon_image(pokemon_name, save_dir):
    
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info is None :
        return
    artwork_url = pokemon_info['sprites']['other']['official-artwork']['front_default']
    
    image_bytes = image_lib.download_image(artwork_url)
    if image_bytes is None:
        return
    file_ext = artwork_url.split('.')[-1]
    image_path = os.path.join(save_dir, f'{pokemon_name}.{file_ext}' )
    
    image_lib.save_image_file(image_bytes, image_path )
   
   
    return
if __name__ == '__main__':
    main()