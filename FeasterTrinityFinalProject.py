#program: final projct - GUI program for window shades 
#author: Trinity Feaster
#created: 2024-9-29
#purpose: Window shade project GUI program - Quote manual or motorized shades

#start GUI program
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

#open second window definition

#manual shade quoting
def open_Manual_Shade_Button():
    #set up new window
    manual_Shade_Window = Tk()
    manual_Shade_Window.title("Manual Shade Order")
    manual_Shade_Window.configure(background="lightyellow")
    manual_Shade_Window.geometry('1000x750')

    #display all questions for entry for a manual shade 
    #window width
    shadeWidthLabel = Label(manual_Shade_Window, text = "Shade Width:", bg="lightyellow")
    shadeWidthLabel.grid(row=0, column=0, columnspan=1, sticky="W")
    shadeWidthInput = Entry(manual_Shade_Window, width= 20, borderwidth=5)
    shadeWidthInput.grid(row=0, column = 1, columnspan = 1, padx= 10, pady=00)


    #window height
    shadeLengthLabel = Label(manual_Shade_Window, text = "Shade Length:", bg="lightyellow")
    shadeLengthLabel.grid(row=1, column=0, columnspan=1, sticky="W")
    shadeLengthInput = Entry(manual_Shade_Window, width= 20, borderwidth=5)
    shadeLengthInput.grid(row=1, column = 1, columnspan = 1, padx= 10, pady=10)


    #measurement type
    shadeMeasurementLabel = Label(manual_Shade_Window, text = "Shade Measurement Type:", bg="lightyellow")
    shadeMeasurementLabel.grid(row=2, column=0, columnspan=1, sticky="W")
    
    measurementType = StringVar(manual_Shade_Window)
    measurementType.set("Inside")
    measurementTypeVar1 = Radiobutton(manual_Shade_Window, text="Cloth", variable=measurementType, value="Cloth")
    measurementTypeVar2 = Radiobutton(manual_Shade_Window, text="Inside", variable=measurementType, value="Inside")
    measurementTypeVar3 = Radiobutton(manual_Shade_Window, text="Outside", variable=measurementType, value="Outside")
    measurementTypeVar1.grid(row=3, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    measurementTypeVar2.grid(row=4, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    measurementTypeVar3.grid(row=5, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    

    #fabric type
    shadeFabricLabel = Label(manual_Shade_Window, text = "Shade Fabric Type:", bg="lightyellow")
    shadeFabricLabel.grid(row=6, column=0, columnspan=2, sticky="W")
    
    fabricType = StringVar(manual_Shade_Window)
    fabricTypeVar1 = Radiobutton(manual_Shade_Window, text="Blackout", variable=fabricType, value="Blackout")
    fabricTypeVar2 = Radiobutton(manual_Shade_Window, text="Sheer Weave 5% Openess", variable=fabricType, value="Sheer")
    fabricTypeVar1.grid(row=7, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    fabricTypeVar2.grid(row=8, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    
 
 
    #fabric color
    shadeColorLabel = Label(manual_Shade_Window, text = "Shade Fabric Color:", bg="lightyellow")
    shadeColorLabel.grid(row=9, column=0, columnspan=2, sticky="W")
    
    fabricColor = StringVar(manual_Shade_Window)
    fabricColorVar1 = Radiobutton(manual_Shade_Window, text="Charcoal", variable=fabricColor, value="Charcoal")
    fabricColorVar2 = Radiobutton(manual_Shade_Window, text="Linen", variable=fabricColor, value="Linen")
    fabricColorVar1.grid(row=10, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    fabricColorVar2.grid(row=11, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    
    
    
    #chain type
    chainTypeLabel = Label(manual_Shade_Window, text = "Shade Chain Type:", bg="lightyellow")
    chainTypeLabel.grid(row=12, column=0, columnspan=2, sticky="W")
    
    chainType = StringVar(manual_Shade_Window)
    chainTypeVar1 = Radiobutton(manual_Shade_Window, text="Plastic", variable=chainType, value="Plastic")
    chainTypeVar2 = Radiobutton(manual_Shade_Window, text="Stainless Steel", variable=chainType, value="StainlessSteel")
    chainTypeVar1.grid(row=13, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    chainTypeVar2.grid(row=14, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")

    #chain color
    chainColorLabel = Label(manual_Shade_Window, text = "Shade Chain Color:", bg="lightyellow")
    chainColorLabel.grid(row=15, column=0, columnspan=2, sticky="W")
    
    chainColor = StringVar(manual_Shade_Window)
    chainColorVar1 = Radiobutton(manual_Shade_Window, text="Black", variable=chainColor, value="Black")
    chainColorVar2 = Radiobutton(manual_Shade_Window, text="White", variable=chainColor, value="White")
    chainColorVar1.grid(row=16, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    chainColorVar2.grid(row=17, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")

    #chain length
    chainLengthLabel = Label(manual_Shade_Window, text = "Chain Length:", bg="lightyellow")
    chainLengthLabel.grid(row=18, column=0, columnspan=1, sticky="W")
    chainLength = Entry(manual_Shade_Window, width= 20, borderwidth=5)
    chainLength.grid(row=18, column = 1, columnspan = 1, padx= 10, pady=10)





    #pricing calcs
    def price_Manual_Window_Button():

        #price constants
        fabricPricePerSqFootBlackout = 4
        fabricPricePerSqFootSheer = 6.5
        chainTypePlastic = 1.5
        chainTypeStainlessSteel = 3

        #header display
        headerLabel = Label(manual_Shade_Window, text = "Manual Shade Pricing:", bg="lightyellow", font = 'TimesNewRoman 11 bold')
        headerLabel.grid(row=0, column=4, columnspan=2, sticky="W")

        #calculate the footage of fabric per square foot and multiply by the fabric price that has labor included
        footage = round((float(shadeWidthInput.get())*float(shadeLengthInput.get()))/144, 0)
        if fabricType.get() == "Blackout":
            fabricPrice = round(footage*fabricPricePerSqFootBlackout, 0)
        else:
            fabricPrice = round(footage*fabricPricePerSqFootSheer, 0)
        
        fabricPriceLabel = Label(manual_Shade_Window, text = "Fabric Price:", bg="lightyellow")
        fabricPriceLabel.grid(row=1, column=4, columnspan=1, sticky="W")
        fabricPriceDisplay = Label(manual_Shade_Window, text = fabricPrice, bg="lightyellow", state=DISABLED)
        fabricPriceDisplay.grid(row=1, column=5, columnspan=1, sticky="W")

        #chain price
        if chainType.get() == "Plastic":
            chainPrice = round(chainTypePlastic*(int(chainLength.get())/12), 0)
        elif chainType.get() == "StainlessSteel":
            chainPrice = round(chainTypeStainlessSteel*(int(chainLength.get())/12), 0)
        
        chainPriceLabel = Label(manual_Shade_Window, text = "Chain Price:", bg="lightyellow")
        chainPriceLabel.grid(row=2, column=4, columnspan=1, sticky="W")
        chainPriceDisplay = Label(manual_Shade_Window, text = chainPrice, bg="lightyellow", state=DISABLED)
        chainPriceDisplay.grid(row=2, column=5, columnspan=1, sticky="W")
        

        #total pricing
        totalPrice = round(fabricPrice + chainPrice , 0)
                        
        totalPriceLabel = Label(manual_Shade_Window, text = "Total Shade Price:", bg="lightyellow",font = 'TimesNewRoman 11 bold')
        totalPriceLabel.grid(row=4, column=4, columnspan=1, sticky="W")
        totalPriceDisplay = Label(manual_Shade_Window, text = totalPrice, bg="lightyellow", state=DISABLED, font = 'TimesNewRoman 11 bold')
        totalPriceDisplay.grid(row=4, column=5, columnspan=1, sticky="W")



    #validate entries
    def validate_Manual_Window_Button():

        #get all entries
        shadeWidthValidation = shadeWidthInput.get()
        shadeLengthValidation = shadeLengthInput.get()
        measurementTypeValidation = measurementType.get()
        fabricTypeValidation = fabricType.get()
        fabricColorValidation = fabricColor.get()
        chainTypeValidation = chainType.get()
        chainColorValidation = chainColor.get()
        chainLengthValidation = chainLength.get()

        #validate entries
        if shadeWidthValidation.isdigit() == False:
            messagebox.showerror("Attention:", "Please enter a valid number for Shade Width.")
            manual_Shade_Window.deiconify()
        elif shadeLengthValidation.isdigit() == False:
            messagebox.showerror("Attention:", "Please enter a valid number for Shade Length.")
            manual_Shade_Window.deiconify()
        elif measurementTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Measurement Type.")
            manual_Shade_Window.deiconify()       
        elif fabricTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Fabric Type.")
            manual_Shade_Window.deiconify() 
        elif fabricColorValidation == "":
            messagebox.showerror("Attention:", "Please select a Fabric Color.")
            manual_Shade_Window.deiconify()
        elif chainTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Chain Type.")
            manual_Shade_Window.deiconify()
        elif chainColorValidation == "":
            messagebox.showerror("Attention:", "Please select a Chain Color.")
            manual_Shade_Window.deiconify() 
        elif chainLengthValidation.isdigit() == False:
            messagebox.showerror("Attention:", "Please enter a valid number for Chain Length.")
            manual_Shade_Window.deiconify()
        else:
            price_Manual_Window_Button()


    #pricing button - validate entries were made and then price
    price_Manual_Window_Button2 = Button(manual_Shade_Window, text = "Price Manual Shade", command=lambda: validate_Manual_Window_Button())
    price_Manual_Window_Button2.grid(row = 30, column = 0, columnspan = 2, pady=30)

    #exit to first box
    def close_Manual_Window_Button():
        manual_Shade_Window.destroy()

    close_Manual_Window_Button = Button(manual_Shade_Window, text = "Back to Welcome Window", command=close_Manual_Window_Button)
    close_Manual_Window_Button.grid(row = 30, column = 3, columnspan = 2, pady=30)




    

#motorized shade quoting
def open_Motorized_Shade_Button():
    #set up new window
    motorized_Shade_Window = Tk()
    motorized_Shade_Window.title("Motorized Shade Order")
    motorized_Shade_Window.configure(background="lightpink")
    motorized_Shade_Window.geometry('1000x750')

    #display all questions for a motorized shade
    #window width
    shadeWidthLabel = Label(motorized_Shade_Window, text = "Shade Width:", bg="lightpink")
    shadeWidthLabel.grid(row=0, column=0, columnspan=1, sticky="W")
    shadeWidthInput = Entry(motorized_Shade_Window, width= 20, borderwidth=5)
    shadeWidthInput.grid(row=0, column = 1, columnspan = 1, padx= 10, pady=00)


    #window height
    shadeLengthLabel = Label(motorized_Shade_Window, text = "Shade Length:", bg="lightpink")
    shadeLengthLabel.grid(row=1, column=0, columnspan=1, sticky="W")
    shadeLengthInput = Entry(motorized_Shade_Window, width= 20, borderwidth=5)
    shadeLengthInput.grid(row=1, column = 1, columnspan = 1, padx= 10, pady=10)


    #measurement type
    shadeMeasurementLabel = Label(motorized_Shade_Window, text = "Shade Measurement Type:", bg="lightpink")
    shadeMeasurementLabel.grid(row=2, column=0, columnspan=1, sticky="W")
    
    measurementType = StringVar(motorized_Shade_Window)
    measurementType.set("Inside")
    measurementTypeVar1 = Radiobutton(motorized_Shade_Window, text="Cloth", variable=measurementType, value="Cloth")
    measurementTypeVar2 = Radiobutton(motorized_Shade_Window, text="Inside", variable=measurementType, value="Inside")
    measurementTypeVar3 = Radiobutton(motorized_Shade_Window, text="Outside", variable=measurementType, value="Outside")
    measurementTypeVar1.grid(row=3, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    measurementTypeVar2.grid(row=4, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    measurementTypeVar3.grid(row=5, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    

    #fabric type
    shadeFabricLabel = Label(motorized_Shade_Window, text = "Shade Fabric Type:", bg="lightpink")
    shadeFabricLabel.grid(row=6, column=0, columnspan=2, sticky="W")
    
    fabricType = StringVar(motorized_Shade_Window)
    fabricTypeVar1 = Radiobutton(motorized_Shade_Window, text="Blackout", variable=fabricType, value="Blackout")
    fabricTypeVar2 = Radiobutton(motorized_Shade_Window, text="Sheer Weave 5% Openess", variable=fabricType, value="Sheer")
    fabricTypeVar1.grid(row=7, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    fabricTypeVar2.grid(row=8, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    
 
 
    #fabric color
    shadeColorLabel = Label(motorized_Shade_Window, text = "Shade Fabric Color:", bg="lightpink")
    shadeColorLabel.grid(row=9, column=0, columnspan=2, sticky="W")
    
    fabricColor = StringVar(motorized_Shade_Window)
    fabricColorVar1 = Radiobutton(motorized_Shade_Window, text="Charcoal", variable=fabricColor, value="Charcoal")
    fabricColorVar2 = Radiobutton(motorized_Shade_Window, text="Linen", variable=fabricColor, value="Linen")
    fabricColorVar1.grid(row=10, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    fabricColorVar2.grid(row=11, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")

    #motor type
    shadeMotorLabel = Label(motorized_Shade_Window, text = "Shade Motor Type:", bg="lightpink")
    shadeMotorLabel.grid(row=12, column=0, columnspan=2, sticky="W")
    
    motor = StringVar(motorized_Shade_Window)
    motorVar1 = Radiobutton(motorized_Shade_Window, text="Standard", variable=motor, value="Standard")
    motorVar2 = Radiobutton(motorized_Shade_Window, text="Quiet", variable=motor, value="Quiet")
    motorVar1.grid(row=13, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    motorVar2.grid(row=14, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")

    #motor lead length
    shadeMotorLeadLabel = Label(motorized_Shade_Window, text = "Shade Motor Lead Length", bg="lightpink")
    shadeMotorLeadLabel.grid(row=15, column=0, columnspan=2, sticky="W")
    
    motorLead = StringVar(motorized_Shade_Window)
    motorLeadVar1 = Radiobutton(motorized_Shade_Window, text="6", variable=motorLead, value="6")
    motorLeadVar2 = Radiobutton(motorized_Shade_Window, text="12", variable=motorLead, value="12")
    motorLeadVar3 = Radiobutton(motorized_Shade_Window, text="18", variable=motorLead, value="18")
    motorLeadVar4 = Radiobutton(motorized_Shade_Window, text="24", variable=motorLead, value="24")
    motorLeadVar1.grid(row=16, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    motorLeadVar2.grid(row=17, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")
    motorLeadVar3.grid(row=18, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    motorLeadVar4.grid(row=19, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")

    #motor lead color
    shadeLeadColorLabel = Label(motorized_Shade_Window, text = "Shade Lead Color Type:", bg="lightpink")
    shadeLeadColorLabel.grid(row=20, column=0, columnspan=2, sticky="W")
    
    motorLeadColor = StringVar(motorized_Shade_Window)
    motorLeadColorVar1 = Radiobutton(motorized_Shade_Window, text="Black", variable=motorLeadColor, value="Black")
    motorLeadColorVar2 = Radiobutton(motorized_Shade_Window, text="White", variable=motorLeadColor, value="White")
    motorLeadColorVar1.grid(row=21, column=1, columnspan=1,rowspan=1, padx=30, pady=5, sticky="W")
    motorLeadColorVar2.grid(row=22, column=1, columnspan=1,rowspan=1, padx=30, pady=0, sticky="W")


    #validate entries
    def validate_Motorized_Window_Button():

        #get all entries
        shadeWidthValidation = shadeWidthInput.get()
        shadeLengthValidation = shadeLengthInput.get()
        measurementTypeValidation = measurementType.get()
        fabricTypeValidation = fabricType.get()
        fabricColorValidation = fabricColor.get()
        motorTypeValidation = motor.get()
        motorLeadValidation = motorLead.get()
        motorLeadColorValidation = motorLeadColor.get()

        #validate entries
        if shadeWidthValidation.isdigit() == False:
            messagebox.showerror("Attention:", "Please enter a valid number for Shade Width.")
            motorized_Shade_Window.deiconify()
        elif shadeLengthValidation.isdigit() == False:
            messagebox.showerror("Attention:", "Please enter a valid number for Shade Length.")
            motorized_Shade_Window.deiconify()
        elif measurementTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Measurement Type.")
            motorized_Shade_Window.deiconify()       
        elif fabricTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Fabric Type.")
            motorized_Shade_Window.deiconify() 
        elif fabricColorValidation == "":
            messagebox.showerror("Attention:", "Please select a Fabric Color.")
            motorized_Shade_Window.deiconify()
        elif motorTypeValidation == "":
            messagebox.showerror("Attention:", "Please select a Motor Type.")
            motorized_Shade_Window.deiconify()
        elif motorLeadValidation == "":
            messagebox.showerror("Attention:", "Please select a Motor Lead.")
            motorized_Shade_Window.deiconify() 
        elif motorLeadColorValidation == "":
            messagebox.showerror("Attention:", "Please select a Motor Lead Color.")
            motorized_Shade_Window.deiconify()
        else:
            price_Motorized_Window_Button()





    #pricing calcs
    def price_Motorized_Window_Button():

        #price constants
        fabricPricePerSqFootBlackout = 5
        fabricPricePerSqFootSheer = 7.5
        standardMotorPrice = 200
        quietMotorPrice = 500
        motorLeadPricePerFoot = 1.5

        #header display
        headerLabel = Label(motorized_Shade_Window, text = "Motorized Shade Pricing:", bg="lightpink", font = 'TimesNewRoman 11 bold')
        headerLabel.grid(row=0, column=4, columnspan=2, sticky="W")

        #calculate the footage of fabric per square foot and multiply by the fabric price that has labor included
        footage = round((float(shadeWidthInput.get())*float(shadeLengthInput.get()))/144, 0)
        if fabricType.get() == "Blackout":
            fabricPrice = round(footage*fabricPricePerSqFootBlackout, 0)
        else:
            fabricPrice = round(footage*fabricPricePerSqFootSheer, 0)
        
        fabricPriceLabel = Label(motorized_Shade_Window, text = "Fabric Price:", bg="lightpink")
        fabricPriceLabel.grid(row=1, column=4, columnspan=1, sticky="W")
        fabricPriceDisplay = Label(motorized_Shade_Window, text = fabricPrice, bg="lightpink", state=DISABLED)
        fabricPriceDisplay.grid(row=1, column=5, columnspan=1, sticky="W")

        #motor price
        if motor.get() == "Standard":
            motorPrice = standardMotorPrice
        elif motor.get() == "Quiet":
            motorPrice = quietMotorPrice
        
        motorPriceLabel = Label(motorized_Shade_Window, text = "Motor Price:", bg="lightpink")
        motorPriceLabel.grid(row=2, column=4, columnspan=1, sticky="W")
        motorPriceDisplay = Label(motorized_Shade_Window, text = motorPrice, bg="lightpink", state=DISABLED)
        motorPriceDisplay.grid(row=2, column=5, columnspan=1, sticky="W")

        #motor lead price
        motorLeadPrice = round(int(motorLead.get()) * motorLeadPricePerFoot, 0)
                        
        motorLeadPriceLabel = Label(motorized_Shade_Window, text = "Motor Lead Price:", bg="lightpink")
        motorLeadPriceLabel.grid(row=3, column=4, columnspan=1, sticky="W")
        motorLeadPriceDisplay = Label(motorized_Shade_Window, text = motorLeadPrice, bg="lightpink", state=DISABLED)
        motorLeadPriceDisplay.grid(row=3, column=5, columnspan=1, sticky="W")

        #total pricing
        totalPrice = round(fabricPrice + motorPrice + motorLeadPrice, 0)
                        
        totalPriceLabel = Label(motorized_Shade_Window, text = "Total Shade Price:", bg="lightpink",font = 'TimesNewRoman 11 bold')
        totalPriceLabel.grid(row=4, column=4, columnspan=1, sticky="W")
        totalPriceDisplay = Label(motorized_Shade_Window, text = totalPrice, bg="lightpink", state=DISABLED, font = 'TimesNewRoman 11 bold')
        totalPriceDisplay.grid(row=4, column=5, columnspan=1, sticky="W")



    #pricing button
    price_Motorized_Window_Button2 = Button(motorized_Shade_Window, text = "Price Motorized Shade", command=lambda: validate_Motorized_Window_Button())
    price_Motorized_Window_Button2.grid(row = 30, column = 0, columnspan = 2, pady=30)

    #exit to first box
    def close_Motorized_Window_Button():
        motorized_Shade_Window.destroy()

    close_Motorized_Window_Button = Button(motorized_Shade_Window, text = "Back to Welcome Window", command=close_Motorized_Window_Button)
    close_Motorized_Window_Button.grid(row = 30, column = 4, columnspan = 2, pady=30)









#main window
root.title("Welcome to Window Shades LLC")
root.configure(background="lightblue")
root.geometry('900x600')


#exit quote
def close_Window_Button():
    root.quit()


#set text for main window
windowShadeOrderingLabel = Label(root, text="Welcome to Window Shades, LLC!", font = 'TimesNewRoman 18 bold', background="lightblue")
windowShadeOrderingLabel.grid(row = 0, column = 0, columnspan = 1, sticky = W, padx=10)
shadeTypeLabel = Label(root, text="Please select the shade type to quote:  ", font = '16', background="lightblue", pady=10)
shadeTypeLabel.grid(row = 1, column = 0, columnspan = 1, sticky = W, padx=10) 

#show images for manual and motorized shade
manualShadeImage = ImageTk.PhotoImage(Image.open("ClutchRollerShade.jpg"))
motorizedShadeImage = ImageTk.PhotoImage(Image.open("MotorizedRollerShade.jpg"))

#put images on screen
manualShadeImageLabel = Label(image=manualShadeImage)
manualShadeImageLabel.grid(row = 3, column = 0, columnspan = 2, padx = 30, sticky = NSEW)
motorizedShadeImageLabel = Label(image=motorizedShadeImage)
motorizedShadeImageLabel.grid(row = 3, column = 2, columnspan = 2, padx = 00, sticky = NSEW)



# define buttons
open_Manual_Shade_Button = Button(root, text = "Manual Shade", command=open_Manual_Shade_Button)
open_Motorized_Shade_Button = Button(root, text = "Motorized Shade", command=open_Motorized_Shade_Button)
close_Window_Button = Button(root, text = "Close", command=close_Window_Button)

#add button to screen 
open_Manual_Shade_Button.grid(row = 4, column = 0, columnspan = 2, padx = 30, sticky = NSEW)
open_Motorized_Shade_Button.grid(row = 4, column = 2, columnspan = 2, padx = 00, sticky = NSEW)
close_Window_Button.grid(row = 5, column = 0, columnspan = 4, pady=30)





root.mainloop()