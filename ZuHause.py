from tkinter import *

class Interface:
    def __init__(self,window):
        self.window = window
        self.window.title("Zu Hause") #Set The Window's Title
        self.window.geometry("600x600") #Set the Window's Geometry
        self.window.resizable(0,0) #I Disabled its resizing

        #Added a Label Widget within the class and packed it into the window
        self.label = Label(self.window, text="Wilkommen Zu Hause", font=("Times New Roman", 20))
        self.label.pack(pady=30)

        #Added a Button to get to the new window that requests user name input
        self.enter_name_button = Button(self.window, text="Enter Your Name To Play", command=self.ask_name_window)
        self.enter_name_button.pack(pady=10)

    def ask_name_window(self):
        #Crated a child window
        self.name_prompt = Toplevel(self.window)
        self.name_prompt.geometry("400x150")
        self.name_prompt.title("What's Your Name? / Wie heissen Sie?")

        #Added a label in thr new window
        self.name_label=Label(self.name_prompt, text="What's your Name? / Wie heissen Sie?", font=('arial', 15, "bold"))
        self.name_label.pack(pady=10)

        #Added an entry wdget for the user to type their name
        self.name_entry = Entry(self.name_prompt, font=('arial', 18, "bold"))
        self.name_entry.pack(pady=10)

        #Added a submit button with a function to handle the name input
        self.submit_button = Button(self.name_prompt, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)
    
    def submit_name(self):
            player_name = self.name_entry.get() #Enabled Name Capture for Name entered in the Entry Widget
            if player_name:
                self.name_prompt.destroy() #Enable closure of the propmt window
            else:
                 print("No name entered.")


root = Tk() #Created The Main Window

app = Interface(root) #Created an instance of the Interface class


root.mainloop() #Initiated the Tkinter main loop
































































































