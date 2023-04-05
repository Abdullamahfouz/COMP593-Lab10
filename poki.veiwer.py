
import poki_api
from tkinter import *
from tkinter import ttk
import os
import ctypes

def main():
    return


script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
image_cahe_dir = os.path(script_dir, 'images')
if not os.path.isdir(image_cahe_dir):
    os.makedirs(image_cahe_dir)

root = Tk()
root.title("Pokemon Image Viewer")
root.minsize(600, 700)


ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('COMP593.PokeImageViewer')
icon_path = os.path.join(script_dir, 'Great-Ball.ico')
root.iconbitmap(icon_path)

frame = ttk.Frame(root, relief='ridge')
frame.grid(row=0, column=0, padx=10 , pady=10, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure (0, weight=1)

img_poke = PhotoImage(file=os.path.join(script_dir))
lbl_poke_image = ttk.Label(frame, image=img_poke)
lbl_poke_image.grid(row=0, column=0)

pokemon_name_list = poki_api.get_pokemon_names()
cbox_poke_names = ttk.Label(frame, values=pokemon_name_list, state='readonly')
cbox_poke_names.set("Select a Pokemon")
cbox_poke_names.grid(row=2, column=0, padx=10, pady=10)

def handle_pokemon_sel(event):
    
    pokemon_name = cbox_poke_names.get()
    global image_path
    image_path = poki_api.get_pokemon_info(pokemon_name, image_cahe_dir )
    
    
    if image_path is not None :
        img_poke['file'] = img_poke
        






btn_set_desktop = ttk.Button(frame, text= ' Set as Desktop Image')
btn_set_desktop.grid(row=2, column=0, padx=10, pady=10)


root.mainloop()





if __name__ == '__main__':
    main()
