from tkinter import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

        #Added a label in the new window
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
                existing_player = collection.find_one({"name": player_name}) #We check first if the player already exists in the databse

                if existing_player:
                     self.label.config(text=f"Welcome back, {player_name}!") #If they exist, we display a welcome back message
                else:
                    player_data = {"name": player_name} #If player doesn't exist, we create a new profile and save it to MongoDB
                    collection.insert_one(player_data) #Insert the new Player Profile into the collection
                    self.label.config(text=f"Good To Have You Here, {player_name}!")

                self.name_prompt.destroy() #Enable closure of the propmt window

            else:
                 print("No name entered.") #This enables us to handle empty inputs


root = Tk() #Created The Main Window

app = Interface(root) #Created an instance of the Interface class


root.mainloop() #Initiated the Tkinter main loop
































































































