from tkinter import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv #We import the csv module to read and write csv files
from random import choice #We import the 'choice' function from the 'random' module to make random selections

# MongoDB Setup To Enable PlayerProfile Access Setup From MongoDb Database
# MongoDB URI Connection string
uri = "mongodb+srv://MLutaaya:Satire6Digits@wordguess.cr5m5.mongodb.net/?retryWrites=true&w=majority&appName=ZuHause"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["ZuHause"] #Database Access
collection = db["PlayersProfiles"] #Access a Collection in the Databse

class GameInterface:
    def __init__(self,window):
        self.window = window
        self.window.title("Zu Hause") #Set The Window's Title
        self.window.geometry("600x600") #Set the Window's Geometry
        self.window.resizable(0,0) #I Disabled its resizing
        self.mode = "light" #Default color mode has been set to light

        #Added a Label Widget within the class and packed it into the window
        self.label = Label(self.window, text="Wilkommen Zu Hause", font=("Times New Roman", 20))
        self.label.pack(pady=30)

        #Added a Button to get the new window that requests user name input
        self.enter_name_button = Button(self.window, text="Enter Your Name To Play", command=self.ask_name_window)
        self.enter_name_button.pack(pady=10)

        #Added a Color Mode Button assigned to the color_mode function to switch between colors
        self.change_color_mode_button = Button(self.window, text="Color Mode", command=self.color_mode)
        self.change_color_mode_button.place(relx=1, rely=0, anchor=NE) #Postion the Button in the right top corner
    
     # A function to switch between light and dark mode.
    def color_mode(self):
         if self.mode == "light":
              self.window.configure(bg="#17202a")
              self.mode = "dark" #Change mode
              self.label.config(bg="#17202a", fg="white") #We change the lable text to white
         else:
              self.window.configure(bg="#d7bde2")
              self.mode = "light" #Update the mode
              self.label.config(bg="#d7bde2", fg="black") #We Change label text to black

    def ask_name_window(self):
        self.enter_name_button.pack_forget() #This will hude the enter name button once clicked

        #Created a child window
        self.name_prompt = Toplevel(self.window)
        self.name_prompt.geometry("400x150")
        self.name_prompt.title("Enter Your Name")
        
         #We Set the default background color for the child window according to whats happening on the current mode
        if self.mode == "light":
             self.name_prompt.configure(bg ="#d7bde2")  
        else:
             self.name_prompt.configure(bg="#17202a")

        #Added a label in the new window
        self.name_label=Label(self.name_prompt, text="What's your Name? / Wie heissen Sie?", font=('arial', 15, "bold"))
        self.name_label.pack(pady=10)

        # Color_Mode Configurations For The Label 
        if self.mode == "light":
             self.name_label.configure(bg="#d7bde2", fg="black")
        else:
             self.name_label.configure(bg="#17202a", fg="white")

        #Added an entry wdget for the user to type their name
        self.name_entry = Entry(self.name_prompt, font=('arial', 18, "bold"))
        self.name_entry.pack(pady=10)

        #Added a submit button with a function to handle the name input
        self.submit_button = Button(self.name_prompt, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)
     
    def submit_name(self):
            player_name = self.name_entry.get() #Enabled Name Capture for Name entered in the Entry Widget
            if player_name:
                existing_player = collection.find_one({"name": player_name}) #We check first if the player already exists in the databse

                if existing_player:
                     self.label.config(text=f"Welcome back, {player_name}!") #If they exist, we display a welcome back message  
                     #Creates both a continue and new game button
                     self.continue_button = Button(self.window, text="Continue Game", command=self.continue_game)
                     self.continue_button.pack(pady=10)
                     self.newgame_button = Button(self.window, text="New Game", command=self.new_game)
                     self.newgame_button.pack(pady=10)

                else:
                    player_data = {"name": player_name, "score":0, "guessed_words": []} #If player doesn't exist, we create a new profile and save it to MongoDB
                    collection.insert_one(player_data) #Insert the new Player Profile into the collection
                    self.label.config(text=f"Good To Have You Here, {player_name}!")
                    
                    self.newgame_button = Button(self.window, text="New Game", command=self.new_game) #Then Creates a New Game Button
                    self.newgame_button.pack(pady=10)

                self.name_prompt.destroy() #Enable closure of the propmt window

            else:
                 print("No name entered.") #This enables us to handle empty inputs
        
    def new_game(self):
         #We hide both newgame and continue buttons
         self.newgame_button.pack_forget() 
         self.continue_button.pack_forget()
     
         #Configure the light modes & display new statement
         if self.mode=="light":
              self.label.config(text=f"Guess a word........", bg="#d7bde2")
         else:
              self.label.config(text=f"Guess a word........", bg="17202a")
    
    def continue_game(self):
         #We hide both newgame and continue buttons
         self.newgame_button.pack_forget()
         self.continue_button.pack_forget()

         #Configure the light modes & display new statement
         if self.mode=="light":
              self.label.config(text=f"Let's Guess More Words.........", bg="#d7bde2")
         else:
              return self.label.config(text=f"Let's Guess More Words.........", bg="#d7bde2")
        

root = Tk() #Created The Main Window
 
app = GameInterface(root) #Created an instance of the Interface class

root.mainloop() #Initiated the Tkinter main loop 