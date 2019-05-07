from tkinter import *

root = Tk()
frame = Frame(root)

########################################
'''
'''
def tkgscreen(width_of_window, height_of_window):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width/2) - (width_of_window/2)
    y_coordinate = (screen_height/2) - (height_of_window/2)
    root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
#####################################
'''
'''
def tkset(width_of_window, height_of_window):
    root.geometry(tkgscreen(width_of_window, height_of_window))
######################################
'''
'''
def tkframe(width_of_window, height_of_window, backgroundcolor, side):
    frame = Frame(root, backgroundcolor, height_of_window, width_of_window)
    frame.pack(side = side.upper())
#####################################
'''
'''
def tkbframe(text, textcolor, screenside):
    fbutton = Button(frame, text = str(text), fg = str(textcolor))
    fbutton.pack(side = screenside.upper())
#####################################
'''
'''   
def tkpack():
    frame.pack()
#####################################
