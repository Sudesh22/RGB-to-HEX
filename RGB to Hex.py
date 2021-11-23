from tkinter import *

root = Tk()
root.title("RGB to HEX Converter V0.1")
root.geometry("300x300")

def hex_(rgb):
    c_list = rgb.split(',')
    r = hex(int(c_list[0]))[2:]
    g = hex(int(c_list[1]))[2:]
    b = hex(int(c_list[2]))[2:]
    
    if r=='0' or g=='0' or b=='0' or int(int(c_list[0]))<10 or int(int(c_list[1]))<10 or int(int(c_list[2]))<10:
        if r=='0' or int(int(c_list[0]))<10:
            r1="0"+str(r)
            r=r1
        if g=='0' or int(int(c_list[1]))<10:
            g1="0"+str(g)
            g=g1
        if b=='0' or int(int(c_list[2]))<10:
            b1="0"+str(b)
            b=b1
    elif int(r, 16)<16 or int(g, 16)<16 or int(b, 16)<16:
        if int(r, 16)<16:
            r1="0"+str(r)
            r=r1
        if int(g, 16)<16:
            g1="0"+str(g)
            g=g1
        if int(b, 16)<16:
            b1="0"+str(b)
            b=r1
    else:
        hex_box.delete(0, END)
        hex_box.insert(0,("#"+str(r)+str(g)+str(b)).upper())
    hex_box.delete(0, END)
    hex_box.insert(0,("#"+str(r)+str(g)+str(b)).upper())
    butt0n = Label(root, text="                 ", height=3, bg=("#"+str(r)+str(g)+str(b)).upper(), padx=5, pady=5)
    butt0n.grid(row=4, column=0)
    

def rgb(hex):
    if hex[0:1] == '#':
        hex = hex[1:]
    red = hex[0:2]
    r1 = int(red[0:1], 16)
    r2 = int(red[1:2], 16)
    r2 = r1*16 + r2
    green = hex[2:4]
    g1 = int(green[0:1], 16)
    g2 = int(green[1:2], 16)
    g2 = g1*16 + g2
    blue = hex[4:6]
    b1 = int(blue[0:1], 16)
    b2 = int(blue[1:2], 16)
    b2 = b1*16 + b2
    rgb_box.delete(0, END)
    rgb_box.insert(0,b2)
    rgb_box.insert(0,",")
    rgb_box.insert(0,g2)
    rgb_box.insert(0,",")
    rgb_box.insert(0,r2)
    butt0n = Label(root, text="                 ", height=3, bg=("#"+hex.upper()), padx=5, pady=5)
    butt0n.grid(row=4, column=0)
    hex_box.delete(0, END)
    hex_box.insert(0, "#"+hex.upper())
    
def copy_hex():
    root.clipboard_clear()
    root.update()
    root.clipboard_append(hex_box.get())

def copy_rgb():
    root.clipboard_clear()
    root.update()
    root.clipboard_append(rgb_box.get())

label_rgb = Label(root, text="Enter the RGB value here: ")
label_rgb.grid(row=0, column=0, padx=5, pady=5, sticky=W)
label_hex = Label(root, text="Enter the Hex value here: ")
label_hex.grid(row=5, column=0, padx=5, pady=5, sticky=W)
color = Label(root, text="                 ", height=3, relief=RIDGE, borderwidth=5, padx=5, pady=5)
color.grid(row=4, column=0)
preview = Label(root, text="Preview:", pady=5)
preview.grid(row=3, column=0, sticky=W)

rgb_box = Entry(root, width=30, borderwidth=5)
rgb_box.grid(row=1, column=0, padx=5, pady=5)
hex_box = Entry(root, width=28, borderwidth=5)
hex_box.grid(row=6, column=0, padx=4, pady=3, sticky=E)
status = Label(root, text="#", relief=SUNKEN)
status.grid(row=6, column=0, sticky=W, padx=5)

rgb_button = Button(root, text="Get Hex value", command=lambda: hex_(rgb_box.get()))       #DA70D6 orchid color -> rgb(218, 112, 214).
rgb_button.grid(row=1, column=1, sticky=W)
rgb_copy_button = Button(root, text="Copy RGB value", command=copy_rgb)
rgb_copy_button.grid(row=2, column=0)
hex_button = Button(root, text="Get RGB value", command=lambda: rgb(hex_box.get()))        #220,20,60  -> #DC143C
hex_button.grid(row=6, column=1, sticky=W)
hex_copy_button = Button(root, text="Copy Hex value", command=copy_hex)
hex_copy_button.grid(row=8, column=0)

root.mainloop()