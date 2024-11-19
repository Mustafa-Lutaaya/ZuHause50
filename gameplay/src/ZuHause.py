from tkinter import * #The tkinter library we imported from the start enables Graphical User Interface creation
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

Max_Wrong_Guesses = 17 #Here we set the maximum number of wrong guesses before the game ends

class GameInterface:
    def __init__(self,window,wrong_guesses=0):
        self.window = window
        self.window.title("Zu Hause") #Set The Window's Title
        self.window.geometry("600x600") #Set the Window's Geometry
        self.window.resizable(0,0) #I Disabled its resizing
        self.mode = "light" #Default color mode has been set to light
        self.level = 1 # We set the deafult level to 1
        self.target_word = None # We set the target word to guess to None
        self.player_name = None # We also set the player name  to None
        self.correct_guesses = [] # We Create a list to store correct guesses 
        self.wrong_guesses = wrong_guesses #Here we count the incorrect guesses
        self.window.bind("<KeyPress>", self.handle_guess) #Here we bond the key press to the handle guess function

        #Added a Label Widget within the class and packed it into the window
        self.label = Label(self.window, text="Wilkommen Zu Hause", font=("Times New Roman", 20))
        self.label.pack(pady=30)

        #Added a Button to get the new window that requests user name input
        self.enter_name_button = Button(self.window, text="Enter Your Name To Play", command=self.ask_name_window)
        self.enter_name_button.pack(pady=10)

        #Added a Color Mode Button assigned to the color_mode function to switch between colors
        self.change_color_mode_button = Button(self.window, text="Color Mode", command=self.color_mode)
        self.change_color_mode_button.place(relx=1, rely=0, anchor=NE) #Postion the Button in the right top corner

        #Added a label to display the current level
        self.level_label = Label(self.window, text="Level: 1", font=("Times New Roman", 16))
        self.level_label.pack(pady=10)
        self.level_label.pack_forget() #We first hide it until after the profile check

        #Added a Label to display the guessed word
        self.guessed_word_label = Label(self.window, text="", font=("Arial", 18))
        self.guessed_word_label.pack(pady=10)

        #Added a label to display the house drwawing and its initially set to nothing
        self.house_label = Label(self.window, text="", font=("Courier",14), justify=CENTER, bg="grey")
        self.house_label.place(relx=0.5, rely=0.5, anchor=CENTER)
     
     #A function to switch between light and dark mode.
    def color_mode(self):
         if self.mode == "light": #If current mode is light
              self.window.configure(bg="#17202a") #We change te background color  and set the mode to dark
              self.mode = "dark"
              self.label.config(bg="#17202a", fg="white") #We change the lable text too to white
              self.level_label.config(bg="#17202a", fg="white") #We change level label colors too
         else:
              self.window.configure(bg="#d7bde2") #If current mode is dark, we change the ackground color and set the mode to light
              self.mode = "light"
              self.label.config(bg="#d7bde2", fg="black") #We Change label text to black
              self.level_label.config(bg="#d7bde2", fg="black")# We change level label colors as well
     
    #Here we define a function to draw a house based on wrong guesses
    def draw_house(self, wrong_guesses):
        house = [
        r'''
        __________
        ''',
        r'''
        __________
       /          \
      /            \   
        ''',
        r'''
        ____________
       /            \
      /______________\
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
       |____    ____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
       |____|  |____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |           _|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |            |
       |          |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |          |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |_         |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /______________\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /___ZU_________\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /___ZU__HA_____\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /___ZU__HAUS___\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /___ZU__HAUSE__\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
        r'''
        ____________
       /            \
      /___ZU__HAUSE._\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        ''',
    ]   #We then go ahead and update the house based on the number of wrong guesses
        self.house_label.config(text=house[min(wrong_guesses, len(house) -1)])

    #A function to ask for the player's name throug prompting
    def ask_name_window(self):
        self.enter_name_button.pack_forget() #We first hide the enter name button once clicked

        #Then Create a child window to ask for the name, by setting its size and title plus position
        self.name_prompt = Toplevel(self.window)
        self.name_prompt.geometry("400x150")
        self.name_prompt.title("Enter Your Name")
        
        # Color_Mode Configurations For The Window 
        if self.mode == "light":
             self.name_prompt.configure(bg="#d7bde2")
        else:
             self.name_prompt.configure(bg="#17202a")

        #Added a label in the new window
        self.name_label=Label(self.name_prompt, text="What's your Name? / Wie heissen Sie?", font=('arial', 15, "bold"))
        self.name_label.pack(pady=10)

        #Added text color for the label according to the mode:
        if self.mode == "light":
             self.name_label.config(bg="#d7bde2", fg="black") #If light mode, text will be black
        else:
             self.name_label.config(bg="#17202a", fg="white") #If dark mode, text will be wite

        #Added an entry wdget for the user to type their name
        self.name_entry = Entry(self.name_prompt, font=('arial', 18, "bold"))
        self.name_entry.pack(pady=10)

        # Added text color for the widget depending on the mode
        if self.mode == "light":
             self.name_entry.config(fg="black") #If light mode , text will be black
        else:
             self.name_entry.config(fg="black") #If dark mode, text will be white

        #Added a submit button with a function to handle the name input
        self.submit_button = Button(self.name_prompt, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)

        #Added text color for the button too depending on the mode
        if self.mode == "light":
             self.submit_button.config(fg="black")
        else:
             self.submit_button.config(fg="black")

    #This Function will handle the name submissions
    def submit_name(self):
            player_name = self.name_entry.get() #Enabled Name Capture for Name entered in the Entry Widget
            if player_name: #If the player enters a namw
                existing_player = collection.find_one({"name": player_name}) #We check first if the player already exists in the databse

                if existing_player: #If it does exist
                     self.player_name = player_name #Store the player name
                     self.level = existing_player.get("level", 1) #We get the level from the player
                     self.label.config(text=f"Welcome back, {player_name}!") #If they exist, we display a welcome back message  
                    
                    # Then make the level visible
                     self.level_label.pack()
                     self.level_label.config(text=f"Level: {self.level}")

                     #Display both a play game button
                     self.playgame_button = Button(self.window, text="Play Game", command=self.play_game)
                     self.playgame_button.pack(pady=10)

                else: #if its a new name
                    self.player_name = player_name #We set the player name
                    player_data = {"name": player_name, "score":0, "guessed_words": [], "level": 1} #We create a new profile and save it to MongoDB
                    collection.insert_one(player_data) #Insert the new Player Profile into the collection
                    self.label.config(text=f"Good To Have You Here, {player_name}!")
                    
                    #We show the level
                    self.level_label.pack()
                    self.level_label.config(text=f"Level: {self.level}")

                    #We then create &  display a button to start a new game
                    self.playgame_button = Button(self.window, text="Play Game", command=self.play_game) #Then Creates a New Game Button
                    self.playgame_button.pack(pady=10)

                self.name_prompt.destroy() #Enable closure of the propmt window

            else:
                 print("No name entered.") #This enables us to handle empty inputs
    
     #A Function to start a new game
    def play_game(self):
         #We hide both playgame & continue buttons
         self.playgame_button.pack_forget() 
     
         #Configure the light modes & display new statement
         if self.mode=="light":
              self.label.config(text=f"Guess a word........")
         else:
              self.label.config(text=f"Guess a word........")
         self.correct_guesses = []
         self.wrong_guesses = 0
         self.select_word() #Start Playing by selecting a word
         self.guessed_word_label.config(text=self.construct_guessed_word()) #We Update the guessed word label with underscores for unguessed letters

    #Function to update the level display based on the current level 
    def level_message(self): 
         self.level_label.config(text=f"Level: {self.level}") #This will display what level we are on in the window

    def game_over(self,message):
         self.label.config(text=message)
         self.house_label.config(text="") #We clear the ouse drawing
         self.playgame_button = Button(self.window, text="Play On", command=self.play_game)
         self.playgame_button.pack(pady=10)
              
    #FUnction to select a word randomly from the CSV files based on the player and their current level       
    def select_word(self):
         # During word selection, we use the stored players name to see the words that have and have not been played
         player = collection.find_one({"name":self.player_name})
         guessed_words = player.get("guessed_words", []) #Retrieve the list of guseesd words
         file_name = None

          #Selection of words from different levels based on which CSV we are using
         if self.level == 1:
          file_name = "a1words.csv"
         elif self.level ==2:
              file_name = "alverbs.csv"
         else:
              self.label.config(text="Game Over!, Thanks for playin!") #Display the game over
              return #To stop it from guessing anymore since there are no more levels

         #The Logic here is to be able to move on to the next level, when words in one level / csv file have all been played
         with open(file_name, mode="r") as csvfile:
          reader = list(csv.reader(csvfile)) #We read the CSV file nto a list of rows
          available_words = [row for row in reader if row[0] not in guessed_words] #This filters out the guessed words

          if available_words:
               selected_row = choice(available_words) # We randomly select a word
               self.target_word = selected_row[0] #Then set the word to be guessed
          else:
               self.level += 1 #If all words in the CSV are selected, we move to the next one
               self.select_word() #We then keep playing in the next level as well

    #Function to construct the guessed word it as well diplays underscores for unguessed letters
    def construct_guessed_word(self):
         guessed_word = ""
         for letter in self.target_word:
              if letter in self.correct_guesses:
                   guessed_word += f"{letter}" 
              else:
                   guessed_word += " _ "
         return guessed_word

    #Function to handle the letter guess from the player
    def handle_guess(self, event):
         guessed_letter = event.char.lower()

         if guessed_letter.isalpha() and len(guessed_letter) == 1: #We check if player has input a single letter
              if guessed_letter in self.target_word:
                   if guessed_letter not in self.correct_guesses:
                        self.correct_guesses.append(guessed_letter)
                        self.label.config(text=f"Good Guess")
              else:
                   self.wrong_guesses += 1 #We increase the number of wrong guesses
                   self.draw_house(self.wrong_guesses) #And call function to build part of the house
                   self.label.config(text=f"Wrong Guess")
                   
              self.guessed_word_label.config(text=self.construct_guessed_word())
         
         #If all letter;s have been guessed, then we update the database with the word then move on to the next word
              if self.construct_guessed_word().replace(" _ ","") == self.target_word:
                   collection.update_one(
                        {"name": self.player_name},
                        {"$push": {"guessed_words": self.target_word}}
                    )
              #Then display a message to the player
                   self.label.config(text=f"Correct! The Word was: {self.target_word}")
                   self.play_game() #Play a new word
              else:
                   if self.wrong_guesses >= Max_Wrong_Guesses:
                    self.label.config(text=f"You Failed")
                    self.game_over("You Failed")
         else:
              self.label.config(text="Invalid input") #We display an incorrect message

# We make the main Tkinter window
root = Tk() 
app = GameInterface(root) #Created an instance of the Interface class
root.mainloop() #Initiated the Tkinter main loop, where we display the window and handle user Interactions