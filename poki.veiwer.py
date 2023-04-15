import poki_api
from tkinter import *
from tkinter import ttk
import os
import ctypes
from image_lib import set_desktop_background_image


#gets the path of the script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

image_cahe_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cahe_dir):
    os.makedirs(image_cahe_dir)

# Creates window
root = Tk()
root.title("Pokemon Image Viewer")
root.minsize(700, 700)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# sets the pokemon weindow icon
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
icon_path = os.path.join(script_dir, 'Great-Ball.ico')
root.iconbitmap(icon_path)

#creats the frame
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
    image_path = poki_api.get_pokemon_image(pokemon_name, image_cahe_dir)
    
    #enable the button when an image is slected
    if image_path is not None:
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

cbox_poke_names.bind('<<ComboboxSelected>>', handle_pokemon_sel)

#sets the images to background
def set_background():
    global image_path
    set_desktop_background_image(image_path)
    
# sets a button that sets the background
btn_set_desktop = ttk.Button(frame, text= ' Set as Desktop Image', command=set_background, state=DISABLED)
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)

# GUI loop
root.mainloop()







