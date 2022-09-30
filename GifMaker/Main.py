import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
import glob
from PIL import Image
from PIL import ImageTk
import time


#setup------------------------
screen = tk.Tk()
screen.title("Gif Studio - Cloudless")
screen.configure(width=800, height= 600)
screen.configure(bg="blue")
screen.iconbitmap("Imgs/GS.ico")
img_list = []
gif_list = []
save_path = ""
play_speed = tk.IntVar()
frame = 0
#show checker board----------------------
def checker_board():
    checker = ImageTk.PhotoImage(Image.open("Imgs/GreyBox.png"))
    label_ck = tk.Label(image= checker)
    label_ck.photo = checker
    label_ck.place(x=100, y=100)

#Clear lists aka restart?-----------------
def Clear_All(list1, list2):
    list1.clear()
    list2.clear()
    showinfo(title = "Cleared", message = "You can now make another one!")
    print(list1)
    print(list2)



#open file func for our images --------------------------------------------------------
def open_file():

    filetypes = (
    ("png files", "*.png"),
    ("jpeg files", "*.jpg"),
    ("All files", "*.")
    )

    filenames = fd.askopenfilenames(title = "Open Files",initialdir = "/",filetypes = filetypes)
    showinfo(title = "Selected Files",message = str(len(filenames)) + " image(s) added to the list!")
    for each in filenames:
        img_list.append(each)
    print(img_list)
    show_anim(img_list)

#display images on the left --------------------------------------------------------
def show_anim(LIST):
    image1 = Image.open(LIST[frame]).resize((200,200))
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(image= test)
    label1.image = test
    label1.place(x=100, y=100)

#cycle through the images ----------------------------------------------------------------
def next_frame():
    global frame
    if img_list != []:
        if frame < len(img_list)-1:

            print("list" + str(len(img_list)))
            print("frame" + str(frame))
            frame += 1
            show_anim(img_list)
        else:
            frame = 0
            show_anim(img_list)
            print("frame back to 0")
    else:
        print("empty list")

#set anim speed --------------------------
speed_label= tk.Label(screen, text = "Animation Speed")
speed_entry= tk.Entry(screen, textvariable = play_speed, font= ("calibre", 11, "normal"))

#good link on how to make gifs in Pillow!
#https://propolis.io/articles/make-animated-gif-using-python.html

def make_gif(LIST, path):
    for each in LIST:
        im = Image.open(each)
        gif_list.append(im)
    print(save_path)
    gif_list[0].save(path, save_all = True, append_images=gif_list[1:], disposal = 2, optimize = False, duration = play_speed.get(), loop=0)
    Clear_All(img_list, gif_list)
    checker_board()
#-------------------------------------------------------------------------------
def save_file():
    files = (
    ("Gif File", "*.gif"),
    ("All files", "*.")
    )
#open the "save as" gui and select the folder and name the file
    if play_speed.get() < 1:
        showinfo(title = "Error",message = "Speed cannot be 0!")
    else:
        if img_list != []:
            filenames = asksaveasfilename( filetypes = files, defaultextension= "*.gif")
            showinfo(title = "Done",message = "Gif Saved =)")

        #convert our file path into a string, I guess just to be safe??
        #Pass it into our make_gif as a path parameter oh boy... messy, but works? =)

            our_path = str(filenames)
            print(save_path)
            make_gif(img_list, our_path)
        else:
            showinfo(title = "Problem",message = "No images selected...")
#-----------------------------------------------------------------------------

# open file button save button and speed as well as text
title = Label(text = "GIF STUDIO",bg="blue",  font=("Terminal", 30))
title.place(x=250, y=30)
text1 = Label(text = "1. Load the images you want (png or jpeg)",bg="blue",  font=("Terminal", 20))
text1.place(x=20, y=350)
text2 = Label(text = "2. Set speed of gif, higher number = slower",bg="blue",  font=("Terminal", 20))
text2.place(x=20, y=400)
text3 = Label(text = "3. Save as .gif and have a nice day =)",bg="blue",  font=("Terminal", 20))
text3.place(x=20, y=450)
text4 = Label(text = "4. For best results use same size images",bg="blue",  font=("Terminal", 20))
text4.place(x=20, y=500)
save_button = ttk.Button(screen, text = "Save As", command= lambda:save_file())
save_button.pack(expand = True)
save_button.place(x=400, y = 200)
open_button = ttk.Button(screen, text = "Load Images", command = lambda:open_file())
open_button.pack(expand = True)
open_button.place(x= 400, y= 100)
speed_label.place(x= 400, y= 150)
speed_entry.place(x= 500, y = 150)

next = ttk.Button(screen, text = "Next Frame", command = lambda:next_frame())
next.place(x=160, y =310)
#clear preview image----------------------------------------
checker_board()




screen.mainloop()
