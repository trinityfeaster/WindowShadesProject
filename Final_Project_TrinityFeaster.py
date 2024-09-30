#program: final projct - GUI program for window shades 
#author: Trinity Feaster
#created: 2024-9-29
#purpose: Window shade project GUI program

#start GUI program
from tkinter import *

root = Tk()

#open second window definition
def open_Manual_Shade_Button():
    #set up new window
    manual_Shade_Window = Tk()
    manual_Shade_Window.title("Manual Shade Order")
    manual_Shade_Window.configure(background="lightyellow")
    manual_Shade_Window.geometry('1000x600')

    #window width
    #window height
    #measurement type
    #fabric type
    #fabric color
    #chain type
    #chain color
    #chain length
    #pricing calcs
    #pricing button

    #exit to first box
    def close_Manual_Window_Button():
        manual_Shade_Window.destroy()

    close_Manual_Window_Button = Button(manual_Shade_Window, text = "Back to Welcome Window", command=close_Manual_Window_Button)
    close_Manual_Window_Button.grid(row = 11, column = 1, columnspan = 2, pady=30)

def open_Motorized_Shade_Button():
    #set up new window
    motorized_Shade_Window = Tk()
    motorized_Shade_Window.title("Motorized Shade Order")
    motorized_Shade_Window.configure(background="lightpink")
    motorized_Shade_Window.geometry('1000x600')

    #window width
    #window height
    #measurement type
    #fabric type
    #fabric color
    #motor type
    #motor lead length
    #motor lead color
    #pricing calcs
    #pricing button
    #exit to first box
    def close_Motorized_Window_Button():
        motorized_Shade_Window.destroy()

    close_Motorized_Window_Button = Button(motorized_Shade_Window, text = "Back to Welcome Window", command=close_Motorized_Window_Button)
    close_Motorized_Window_Button.grid(row = 11, column = 1, columnspan = 2, pady=30)







#main window
root.title("Welcome to Window Shades LLC")
root.configure(background="lightblue")
root.geometry('800x300')

#exit quote
def close_Window_Button():
    root.quit()


#set text for main window
windowShadeOrderingLabel = Label(root, text="Welcome to Window Shades, LLC!", font = 'TimesNewRoman 18 bold', background="lightblue")
windowShadeOrderingLabel.grid(row = 0, column = 0, columnspan = 1, sticky = W, padx=10)
shadeTypeLabel = Label(root, text="Please select the shade type to quote:  ", font = '16', background="lightblue", pady=10)
shadeTypeLabel.grid(row = 1, column = 0, columnspan = 1, sticky = W, padx=10) 


# define buttons
open_Manual_Shade_Button = Button(root, text = "Manual Shade", command=open_Manual_Shade_Button)
open_Motorized_Shade_Button = Button(root, text = "Motorized Shade", command=open_Motorized_Shade_Button)
close_Window_Button = Button(root, text = "Close", command=close_Window_Button)

#add button to screen 
open_Manual_Shade_Button.grid(row = 1, column = 1, columnspan = 1, padx = 20, sticky = NSEW)
open_Motorized_Shade_Button.grid(row = 1, column = 2, columnspan = 1, padx = 10, sticky = NSEW)
close_Window_Button.grid(row = 2, column = 1, columnspan = 2, pady=30)



root.mainloop()