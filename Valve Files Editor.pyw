import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import subprocess
import os
from PIL import Image
import glob

window = tk.Tk()
window.title("Valve Files Generator")
window.geometry("400x400")
window.resizable(False, False)



tabControl = ttk.Notebook(window, takefocus=0)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='‎‎‎‎   .vmt✓   ')
tabControl.add(tab2, text ='   .qc (in progress)   ')
tabControl.add(tab3, text ='   .kv✓   ')
tabControl.add(tab4, text ='‎‎‎‎   .vtf✓   ')
tabControl.add(tab5, text ='Settings')
tabControl.pack(expand = 1, fill ="both")

entry_setup = Entry(tab5, takefocus=0)
entry_setup.pack()
entry_setup.place(x=5, y=30, height=23, width=270)

def Y():
    try:
        f = open("path_save.txt", "r")
        g = f.read()
        entry_setup.insert(0, g)
    except FileNotFoundError:
        print("error")

Y()

def Vtf_folder():

    try:
        with open("path_save.txt", "r") as f:
            g = f.read()
            f.close()
        folder = Path(filedialog.askdirectory())
        for png_path in folder.glob('*.png'):
            tga_path = png_path.with_suffix('.tga')
            Image.open(png_path).save(tga_path)
            print(png_path)
            print(tga_path)
            vtex_path = '"'+g+'/bin/vtex" -quiet -nopause -mkdir -outdir "Exported VTF" -game "'+g+'/csgo" "'+str(png_path)+'"'
            subprocess.call(vtex_path)
        if (check_vmt.instate(['selected']) == True):
            textures = entry_textures.get()
            with open('Exporte VTF/'+png_path) as fil: 
                fil.write('VertexlitGeneric\n')
                fil.write('{\n')
                fil.write('	      $basetexture'+textures+'\n')
                fil.write('}')
                Exported()
    except FileNotFoundError:
        vtex = entry_setup.get()
        save = open("path_save.txt", "w")
        save.write(vtex)
        save.close()

def Vtf_file():

    try:
        with open("path_save.txt", "r") as f:
            g = f.read()
            f.close()
        file = filedialog.askopenfilename()
        file_name = Path(file).stem
        Image.open(file).save(file_name+'.tga')
        vtex_path = '"'+g+'/bin/vtex" -quiet -nopause -mkdir -outdir "Exported VTF" -game "'+g+'/csgo" "'+str(png_path)+'"'
        subprocess.call(vtex_path)
        if (check_vmt.instate(['selected']) == True):
            textures = entry_textures.get()
            with open('Exporte VTF/'+png_path) as fil: 
                fil.write('VertexlitGeneric\n')
                fil.write('{\n')
                fil.write('	      $basetexture'+textures+'\n')
                fil.write('}')
                Exported()
    except FileNotFoundError:
        vtex = entry_setup.get()
        save = open("path_save.txt", "w")
        save.write(vtex)
        save.close()
       

def config():
    vtex = entry_setup.get()
    if (vtex != ""):
     save = open("path_save.txt","w")
     save.write(vtex)
     save.close()  
    else:
        Error()
 
def help():
    messagebox.showinfo('Help', 'For use all functions, config your Counter-Strike Global Offensive folder. You can contact Avocado 🥑#8351 for additional help')


def Correct_folder():
   path = filedialog.askdirectory()
   list_of_files = glob.glob(path + '/*.vmt') #500 files
   to_replace = entry_to_replace.get()
   replace_by = entry_replace_with.get()

   for file_name in list_of_files:
       print(file_name)
       with open(file_name, 'r') as f:
            data = f.read()
       with open(file_name, 'w') as f:
            f.write(data.replace(to_replace,replace_by))

def Correct_file():
    file = filedialog.askopenfilename()
    to_replace = entry_to_replace.get()
    replace_by = entry_replace_with.get()

    with open(file, 'r') as f:
        data = f.read()
    with open(file, 'w') as f:
        f.write(data.replace(to_replace,replace_by))

def QC():

    model = entry_mdl_name.get()
    smd = entry_smd_name.get()
    materials = entry_textures.get()
    directory = "Exported QC/" + model + ".qc"
    os.makedirs(os.path.dirname(directory), exist_ok=True)
    with open(directory, "w") as fil:
      fil.write('$modelname "' + model+'.mdl"\n')
      fil.write('$model "Body" "'+smd+'.smd"\n')
      fil.write('\n')
      if (check_static.instate(['selected']) == True):  
        fil.write('$staticprop\n')
      elif (check_dynamic.instate(['selected']) == True): 
        fil.write('$dynamicprop\n')       
      fil.write('$cdmaterials "'+materials+'"\n')              
      fil.write('\n')       
      fil.write('$sequence "idle" "'+smd+'"\n')
      if (check_collisions.instate(['selected']) == True):  
        fil.write('$collisionmodel "'+smd+'.smd" { $concave }')
      with open("path_save.txt", "r") as f:
        g = f.read()
        f.close()
      studiomdl_path = '"'+g+'/bin/studiomdl" -quiet -game "'+g+'/csgo" -i "'+str(directory)+'"'
      subprocess.call(studiomdl_path)     
      Exported()

def Compile():
    Error()
    file = filedialog.askopenfilename()
    exec_path = 'E:\\Gamess\\steamapps\\common\\Half-Life 2\\bin\\studiomdl.exe'
    txt_input_path = 'E:\\Gamess\\steamapps\\common\\Half-Life 2\\ep2\\materialsrc\\skybox\\sky_default\\sky_default_tga_src\\sky_defaultbk.txt'
    subprocess.call(exec_path, '-quiet', '-nomkdir', txt_input_path )



def KV():
    map_name = entry_map_name.get()	
    directory = "Exported KV/" + map_name + ".kv"
    os.makedirs(os.path.dirname(directory), exist_ok=True)
    try:
        ct
        with open(directory, "w") as fil:
          fil.write('"'+map_name+'"\n' )
          fil.write('{ \n' )
          fil.write('   "name" "'+map_name+'"\n')
          fil.write('   "t_arms" "models/weapons/t_arms_'+t+'".mdl"\n')        
          fil.write('   "ct_arms" "models/weapons/ct_arms_'+ct+'.mdl"\n')        
          fil.write('   "t_models"\n')         
          fil.write('   {\n')        
          fil.write('      "tm_'+t+'" ""\n')        
          fil.write('      "tm_'+t+'_variantA" ""\n')        
          fil.write('      "tm_'+t+'_variantB" ""\n')         
          fil.write('      "tm_'+t+'_variantC" ""\n')
          fil.write('      "tm_'+t+'_variantD" ""\n')
          fil.write('   }')  	  
          fil.write('   "ct_models"\n')
          fil.write('   {') 
          fil.write('      "ctm_'+ct+'" ""\n') 
          fil.write('      "ctm_'+ct+'_variantA" ""\n')
          fil.write('      "ctm_'+ct+'_variantB" ""\n')
          fil.write('      "ctm_'+ct+'_variantC" ""\n')
          fil.write('      "ctm_'+ct+'_variantD" ""\n')
          fil.write('   }\n')
          fil.write('}\n')
          Exported()
    except:
        ct_c = entry_custom_ct.get() 
        t_c = entry_custom_t.get()
        with open(directory, "w") as fil:
          fil.write('"'+map_name+'"\n' )
          fil.write('{ \n' )
          fil.write('   "name" "'+map_name+'"\n')
          fil.write('   "t_arms" "models/weapons/t_arms_'+t_c+'".mdl"\n')        
          fil.write('   "ct_arms" "models/weapons/ct_arms_'+ct_c+'.mdl"\n')        
          fil.write('   "t_models"\n')         
          fil.write('   {\n')        
          fil.write('      "'+t_c+'" ""\n')        
          fil.write('      "'+t_c+'" ""\n')        
          fil.write('      "'+t_c+'" ""\n')         
          fil.write('      "'+t_c+'" ""\n')
          fil.write('      "'+t_c+'s" ""\n')
          fil.write('   }')  	  
          fil.write('   "ct_models"\n')
          fil.write('   {') 
          fil.write('      "'+ct_c+'" ""\n') 
          fil.write('      "'+ct_c+'" ""\n')
          fil.write('      "'+ct_c+'" ""\n')
          fil.write('      "'+ct_c+'" ""\n')
          fil.write('      "'+ct_c+'" ""\n')
          fil.write('   }\n')
          fil.write('}\n')
          Exported()	 	  

def setup_changed(event):
    msg = f'You selected {month_cb.get()}'
    showinfo(title='Result', message=msg)

def qc_type_changed(event):
    qc = qc_type_cb.get()
    print(qc)	

def t_agents_changed(event):
    global t
    t = t_agents_cb.get()
    entry_custom_ct.config(state="disabled")
    entry_custom_t.config(state="disabled")
    print(t)
    if (t == ''):
        entry_custom_ct.config(state="normal")
        entry_custom_t.config(state="normal")

def ct_agents_changed(event):
    global ct
    ct = ct_agents_cb.get()
    entry_custom_ct.config(state="disabled")
    entry_custom_t.config(state="disabled")
    print(ct)
    if (ct == ''):
        entry_custom_ct.config(state="normal")
        entry_custom_t.config(state="normal")
	
def Click():     
  
      messagebox.showinfo("Info", "Choose the game(s) to export file")
	  
def Exported():     
  
      messagebox.showinfo("Info", "File exported!")

def Error():
    messagebox.showinfo("Error", "Missing information")
	  
def File():     
	  
      global file_path
      file_path = filedialog.askopenfilename(initialdir="G:/Documents",  filetypes =(("PNG Files", "*.png"),("JPEG Files","*.jpeg"),("TIG Files","*.tig"),("TGA Files","*.tga"),("All Files","*")), title = "Choose a file.")
      global file_name
      file_name = Path(file_path).stem
      Vmt()
    
def File():
   path = filedialog.askdirectory()
   list_of_files = glob.glob(path + '/*.vtf') #500 files


# loop through all file names
   for file_name in list_of_files:
    # print the name of file
       print(file_name)
       with open(file_name, 'r') as f:
         data = f.read()
         y = Path(file_name).stem
       with open(y + ".vmt", 'w') as f: 
         f.write('VertexLitGeneric \n' )
         f.write('{ \n' )
         f.write('        $basetexture "codww2/' + y + '" \n')
         f.write('        $bumpmap "codww2/' + y + 'a"\n')
         f.write('        $surfaceprop Wood_furniture \n')
         f.write('         \n')
         f.write('        $phong 1 \n')
         f.write('        $phongexponenttexture "codww2/' + y + '_g"\n')
         f.write('        $phongfresnelranges "[0.5 0.75 1]" \n')
         f.write('         \n')
         f.write('        $selfillum 1 \n')
         f.write('        $selfillumtint "[0 0 0]" \n')
         f.write('} \n' )
   else:
    Exported()
	  	  	       

#lists				   
setups = ('Normal', 'Kitbash 3D', 'CoD WW2', 'Source Games')
qc_type = ('Prop')
t_agents = ('', 'anarchist', 'balkan', 'leet', 'phoenix', 'pirate', 'professional')
ct_agents = ('', 'fbi', 'gign', 'gsg9', 'idf', 'sas', 'swat', 'st6')

label = ttk.Label(tab1, text="Select game setup :")
label.pack(fill='x', padx=5, pady=5)

label = ttk.Label(tab1, text="Path :")
label.pack(fill='x', padx=5, pady=5)
label.place(x=5, y=120)

label = ttk.Label(tab1, text="VMT Replace :")
label.pack(fill='x', padx=5, pady=5)
label.place(x=5, y=190)

label = ttk.Label(tab1, text="Text to replace :")
label.pack(fill='x', padx=5, pady=5)
label.place(x=5, y=230)

label = ttk.Label(tab1, text="Replace with :")
label.pack(fill='x', padx=5, pady=5)
label.place(x=5, y=270)

label3 = ttk.Label(text="v.0.0.9                                                                                     Made by Avocado")
label3.pack(fill='x', padx=5, pady=5)
label3.place(x=5, y=380)

label4 = ttk.Label(tab3, text="Name of map :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=5)

label4 = ttk.Label(tab3, text="CT :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=60)

label4 = ttk.Label(tab3, text="T :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=115)

label4 = ttk.Label(tab3, text="CT Custom :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=170)

label4 = ttk.Label(tab3, text="T Custom :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=225)

label4 = ttk.Label(tab2, text="Choose .qc file type :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=5)

label4 = ttk.Label(tab2, text="Model name in .smd :                                                     Options :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=60)

label4 = ttk.Label(tab2, text="Model name :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=115)

label4 = ttk.Label(tab2, text="Materials :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=170)

label4 = ttk.Label(tab2, text="Anims (optional) :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=225)

label4 = ttk.Label(tab4, text="Working sizes :\n \n64x64\n128x128\n256x256\n512x512\n1024x1024\n2048x2048")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=250, y=5)

label4 = ttk.Label(tab4, text="Options .vmt :")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=90)

label4 = ttk.Label(tab5, text="Past Counter-Strike Global Offensive path")
label4.pack(fill='x', padx=5, pady=5)
label4.place(x=5, y=5)



my_entry = Entry(tab1)
my_entry.pack()
my_entry.place(x=5, y=90, height=23, width=240)

entry_materials = Entry(tab1)
entry_materials.pack()
entry_materials.place(x=5, y=140, height=23, width=240)

entry_to_replace = Entry(tab1)
entry_to_replace.pack()
entry_to_replace.place(x=130, y=230, height=23, width=240)

entry_replace_with = Entry(tab1)
entry_replace_with.pack()
entry_replace_with.place(x=130, y=270, height=23, width=240)

entry_map_name = Entry(tab3)
entry_map_name.pack()
entry_map_name.place(x=5, y=30, height=23, width=240)

entry_custom_ct = Entry(tab3)
entry_custom_ct.pack()
entry_custom_ct.place(x=5, y=195, height=23, width=240)

entry_custom_t = Entry(tab3)
entry_custom_t.pack()
entry_custom_t.place(x=5, y=250, height=23, width=240)

entry_smd_name = Entry(tab2)
entry_smd_name.pack()
entry_smd_name.place(x=5, y=85, height=23, width=240)

entry_mdl_name = Entry(tab2)
entry_mdl_name.pack()
entry_mdl_name.place(x=5, y=140, height=23, width=240)

entry_textures = Entry(tab2)
entry_textures.pack()
entry_textures.place(x=5, y=195, height=23, width=240)

entry_anims = Entry(tab2)
entry_anims.pack()
entry_anims.place(x=5, y=250, height=23, width=240)



#combobox
selected_setup = tk.StringVar()

month_cb = ttk.Combobox(tab1, textvariable=selected_setup, width=50, takefocus=0)
month_cb['values'] = setups
month_cb['state'] = 'readonly'  # normal
month_cb.pack(fill='x', padx=5, pady=5)
month_cb.place(x=5, y=40)

selected_qc_type = tk.StringVar()

qc_type_cb = ttk.Combobox(tab2, textvariable=selected_qc_type, width=50, takefocus=0)
qc_type_cb['values'] = qc_type
qc_type_cb['state'] = 'readonly'  # normal
qc_type_cb.pack(fill='x', padx=5, pady=5)
qc_type_cb.place(x=5, y=30)

selected_t_agents = tk.StringVar()

t_agents_cb = ttk.Combobox(tab3, textvariable=selected_t_agents, width=36, takefocus=0)
t_agents_cb['values'] = t_agents
t_agents_cb['state'] = 'readonly'  # normal
t_agents_cb.pack(fill='x', padx=5, pady=5)
t_agents_cb.place(x=5, y=140)

selected_ct_agents = tk.StringVar()

ct_agents_cb = ttk.Combobox(tab3, textvariable=selected_ct_agents, width=36, takefocus=0)
ct_agents_cb['values'] = ct_agents
ct_agents_cb['state'] = 'readonly'  # normal
ct_agents_cb.pack(fill='x', padx=5, pady=5)
ct_agents_cb.place(x=5, y=85)

#buttons
button = ttk.Button(tab1, text="...", command=Y, width=3, takefocus=0)
button.place(x=335, y=39)

button2 = ttk.Button(tab1, text="Select file", command=File, width=15, takefocus=0)
button2.place(x=262, y=89)

button2 = ttk.Button(tab1, text="Replace folder", command=Correct_folder, width=15, takefocus=0)
button2.place(x=50, y=310)

button2 = ttk.Button(tab1, text="Replace file", command=Correct_file, width=15, takefocus=0)
button2.place(x=250, y=310)

button3 = ttk.Button(tab2, text="Generate .qc", command=QC, width=15, takefocus=0)
button3.place(x=50, y=300)

button3 = ttk.Button(tab2, text="Compile", command=Compile, width=15, takefocus=0)
button3.place(x=250, y=300)

button3 = ttk.Button(tab3, text="Generate .kv", command=KV, width=15, takefocus=0)
button3.place(x=150, y=300)

button = ttk.Button(tab2, text="...", command=Click, width=3, takefocus=0)
button.place(x=335, y=29)

button4 = ttk.Button(tab4, text="Convert File", command=Vtf_file, width=15, takefocus=0)
button4.place(x=5, y=5)

button4 = ttk.Button(tab4, text="Convert Folder", command=Vtf_folder, width=15, takefocus=0)
button4.place(x=5, y=40)

button4 = ttk.Button(tab5, text="Config", command=config, width=15, takefocus=0)
button4.place(x=285, y=29)

button4 = ttk.Button(tab5, text="Help", command=help, width=15, takefocus=0)
button4.place(x=280, y=300)


check_static = ttk.Checkbutton(tab2, text="Prop Static", takefocus=0)
check_static.invoke()
check_static.invoke()
check_static.place(x=280, y=85)

check_dynamic = ttk.Checkbutton(tab2, text="Prop Dynamic", takefocus=0)
check_dynamic.place(x=280, y=105)
check_dynamic.invoke()
check_dynamic.invoke()

check_collisions = ttk.Checkbutton(tab2, text="Collisions", takefocus=0)
check_collisions.place(x=280, y=125)
check_collisions.invoke()

check_compile = ttk.Checkbutton(tab2, text="Compile to mdl", takefocus=0)
check_compile.place(x=280, y=145)
check_compile.invoke()
check_compile.invoke()

check_vmt = ttk.Checkbutton(tab4, text="Create .vmt", takefocus=0)
check_vmt.place(x=120, y=25)
check_vmt.invoke()


month_cb.bind('<<ComboboxSelected>>', setup_changed)
qc_type_cb.bind('<<ComboboxSelected>>', qc_type_changed)
t_agents_cb.bind('<<ComboboxSelected>>', t_agents_changed)
ct_agents_cb.bind('<<ComboboxSelected>>', ct_agents_changed)

window.mainloop()