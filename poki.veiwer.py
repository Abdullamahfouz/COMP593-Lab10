
import poki_api
from tkinter import *
from tkinter import ttk
import os
import ctypes
from image_lib import set_desktop_background_image

def get_background ():
    background = set_desktop_background_image(image_path)
    return background

#gets the path of the script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cahe_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cahe_dir):
    os.makedirs(image_cahe_dir)
# makes the path
root = Tk()
root.title("Pokemon Image Viewer")
root.minsize(700, 700)

# sets the pokemon weindow icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
icon_path = os.path.join(script_dir, 'Great-Ball.ico')
root.iconbitmap(icon_path)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#creats the fra,e
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10 , pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure (0, weight=1)

#Adds Image to frame
img_poke = PhotoImage(file=os.path.join(script_dir, 'pokemon_logo.png'))
lbl_poke_image = ttk.Label(frame, image=img_poke)
lbl_poke_image.grid(row=0, column=0)

# Add the Pokemon names pull-down list to the frame
pokemon_name_list = sorted(poki_api.get_pokemon_names())
cbox_poke_names = ttk.Combobox(frame, values=pokemon_name_list, state='readonly')
cbox_poke_names.set("Select a Pokemon")
cbox_poke_names.grid(row=1, column=0, padx=10, pady=10)

def handle_pokemon_sel(event):
    # Get the name of the selected Pokemon
    pokemon_name = cbox_poke_names.get()
   
    # Download and save the artwork for the selected Pokemon
    global image_path
    image_path = poki_api.get_pokemon_info(pokemon_name, image_cahe_dir )
    
    
    if image_path is not None :
        img_poke['file'] = img_poke
        
cbox_poke_names.bind('<<CombobxSelected>>', handle_pokemon_sel)


# sets a button
btn_set_desktop = ttk.Button(frame, text= ' Set as Desktop Image')
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)






root.mainloop()





