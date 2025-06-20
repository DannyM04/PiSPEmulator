from tkinter import *
from tkinter import ttk

#Sets resolution, background colour, exit for application
root = Tk()     #Creates the window for the UI
root.attributes ("-fullscreen", True) #Sets the application to fullscreen
root.bind("<Escape>", lambda event : root.quit()) #Binds escape key to quit the app (temporary)
root.configure(bg='#1b1b1b') #Sets background for application

#showFrame makes the selected frame visible to the user
def showFrame(frame):
    frame.tkraise()

#Master frame in root window
container = Frame(root)
container.pack(fill="both", expand=True)

#Creates emulator screens, stores them in the container and sets background
homeScreen = Frame(container, bg='#1b1b1b')
pspScreen = Frame(container, bg='#1b1b1b')
n64Screen = Frame(container, bg='#1b1b1b')
pcScreen = Frame(container, bg='#1b1b1b')

#Sets all frames to be fullscreen by default
for frame in (homeScreen, pspScreen, n64Screen, pcScreen):
    frame.place(relwidth= 1, relheight= 1)

#homeScreen UI:
homeTitle = Label(homeScreen, text="PiSP DEMO", fg="white", font=28, bg="blue") #Creates a title for the application
homeTitle.pack(pady=40)

#Creates a function that allows the user to navigate the menu.
def navButton (text, command, masterFrame):
    return Button(homeScreen,
                  text=text, #Allows us to label each button
                  width=20, #Sets width
                  height=2, #Sets height
                  bg="#333333", #sets background colour
                  activebackground="#555555", #Sets background when hovered over with cursor
                  relief=FLAT, #Sets the buttons appearance. Flat = no borders and 2D (flat looks modern & sleek)
                  command=command) #Allows us to attach a command to the button (navigates us to new menus)

#Creates a dedicated home button, same design as the navButton.
def HomeButton(masterFrame):
    homeButton= Button(masterFrame,
                      text="Home",
                      width=20,
                      height=2,
                      bg="#333333",
                      activebackground="#555555",
                      relief=FLAT,
                      command=lambda: showFrame(homeScreen))
    homeButton.pack(side=BOTTOM, pady=20)

#Creates the buttons and spaces them out
buttonPSP = navButton("PSP", lambda: showFrame(pspScreen), homeScreen)
HomeButton(pspScreen)
buttonPSP.pack(pady=10)
buttonN64 = navButton("N64", lambda: showFrame(n64Screen), homeScreen)
buttonN64.pack(pady=10)
buttonPC = navButton("PC", lambda: showFrame(pcScreen), homeScreen)
buttonPC.pack(pady=10)

#Placeholder text (add features and remove once done)
Label(pspScreen, text="PSP Games Coming Soon", fg="white", bg="black", font=("Helvetica", 24)).pack(expand=True)
Label(n64Screen, text="N64 Games Coming Soon", fg="white", bg="black", font=("Helvetica", 24)).pack(expand=True)
Label(pcScreen, text="PC Games Coming Soon", fg="white", bg="black", font=("Helvetica", 24)).pack(expand=True)

showFrame(homeScreen) #Starts user on the homeScreen

root.mainloop() #Starts the Application
