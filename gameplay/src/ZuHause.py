from tkinter import *  #Imported tkinter for GUI Functionality
from pymongo.mongo_client import MongoClient #Import MongoDB Client
from pymongo.server_api import ServerApi #Import ServerAPI for MongoDB Connection Handling
import csv  # Import the csv module to read and write csv files
from random import choice # Import the 'choice' function from the 'random' module to make random selections

# MongoDB Connection Setup
uri = "mongodb+srv://MLutaaya:Satire6Digits@wordguess.cr5m5.mongodb.net/?retryWrites=true&w=majority&appName=ZuHause" # MongoDB URI Connection string
client = MongoClient(uri, server_api=ServerApi("1"))

#Test MongoDB Connection Setup
try:
    client.admin.command("ping") # Send a ping to confirm a successful connection
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client["ZuHause"]  # Acces the "ZuHause" Database
collection = db["PlayersProfiles"]  # Access the "PlayersProfiles" Collection in the Databse

Max_Wrong_Guesses = 17  # Set the maximum number of wrong guesses before the game ends

# Main Game Interface Class 
class GameInterface:
    def __init__(self, window, wrong_guesses=0, score=0, correct_guesses_count = 0):
        self.window = window
        self.window.title("Zu Hause")  # Set The Window's Title
        self.window.geometry("800x600")  # Set the Window's Size
        self.window.resizable(0, 0)  # Disabled Window Resizing
        self.current_screen = self.setup_ui # Tracks The Main Screen 
        
        # Initalize Game Variables 
        self.mode = "light"  # Default to light mode
        self.level = 1  # Deafult level is 1
        self.target_word = None  # Placeholder for the target word 
        self.hint_text = None  # Placeholder for the hunt
        self.game_active = True # Game State is set to active initially
        self.player_name = None  # Placeholder for player name
        self.correct_guesses = []  # List for correct guesses
        self.wrong_guesses = wrong_guesses  # Track Number of Wrong Guesses
        self.correct_guesses_count = correct_guesses_count #Initialize Counter For Correctly Guessed Words
        self.score = score #Initialization Of Score
        self.played_words = [] # Keep Track of Played Words
        self.delete_buttons = [] #List to store delete Buttons
        self.back_button = None #Initialize Go Back Button
        
        self.window.bind("<KeyPress>", self.handle_guess) # Bind Key Press to Guess Handler
        
        self.setup_ui() # Initialize UI Elements
        
        
        
    '''UI SETUP'''    
    def setup_ui(self):
        #Sets Up The UI Elemenys Of The Game
        self.label = Label(self.window, text="Wilkommen Zu Hause", font=("Raleway Bold", 16))
        self.label.pack(pady=30)

        # Button To Enter The Player's Name
        self.enter_name_button = Button(self.window, text="Enter Your Name To Play", command=self.ask_name_window)
        self.enter_name_button.pack(pady=10)

        # Button To Change Color Mode
        self.change_color_mode_button = Button(self.window, text="Color Mode", command=self.color_mode)
        self.change_color_mode_button.place(relx=1, rely=0, anchor=NE)  # Postion the Button in the right top corner

        # Level Display Label
        self.level_label = Label(self.window, text="Level: 1", font=("Raleway", 15))
        self.level_label.pack(side=BOTTOM, pady=20)
        self.level_label.pack_forget()  # Initially Hidden Until The Profile Is Checked

        # Display For Guessed Word
        self.guessed_word_label = Label(self.window, text="", font=("Raleway", 15))
        self.guessed_word_label.pack(pady=10)

        # Display For House Drawing 
        self.house_label = Label(self.window, text="", font=("Arial", 15), justify=CENTER, bg="grey")
        self.house_label.place(relx=1.0, rely=1.0, anchor=SE) #Here we have set the house_lael to the bottom right corner

        # Button To Show Hints
        self.hint_button = Button(self.window, text="Hint", command=self.hint)
        self.hint_button.pack(pady=10)
        self.hint_button.pack_forget() #Initially Hidden
        
        # Profiles Button 
        self.profiles_button = Button(self.window, text="Profiles", command=self.show_profiles)
        self.profiles_button.place(relx=0.0, rely=1.0, anchor=SW, x=10, y=-10)
        
        # Profiles Label
        self.profiles_label = Label(self.window, text="", justify="left", anchor="w", width=50, height=10, bg="lightgrey", relief="solid")
        self.profiles_label.pack_forget() #Initialyy Hide It
        
        # Notification Label For Level Up & 5 Wrong Guesses Left
        self.notification_label = Label(self.window, text="", font=("Arial", 12, "bold"), fg="white", bg="green")
        self.notification_label.place(x=10,y=10) # Position The Notification At The Top-Left Corner
        
    def color_mode(self):
        #Toggle Between Light & Dark Mode
        if self.mode == "light":  # Changes To Dark Mode
            self.window.configure(bg="#17202a")  
            self.mode = "dark"
            self.label.config(bg="#17202a", fg="white") 
            self.level_label.config(bg="#17202a", fg="white")  
        else: #Changes To Light Mode
            self.window.configure(bg="#d7bde2")
            self.mode = "light"
            self.label.config(bg="#d7bde2", fg="black")
            self.level_label.config(bg="#d7bde2", fg="black") 
            
    def draw_house(self, wrong_guesses):
        #Draws The House Based On The Number Of Wrong Moves
        house = [
            r"""
        __________
        """,
            r"""
        __________
       /          \
      /            \   
        """,
            r"""
        ____________
       /            \
      /______________\
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
       |____    ____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |            |
       |____|  |____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |            |
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |           _|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |            |
       |          |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |          |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |_         |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |           _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /______________\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /___ZU_________\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /___ZU__HA_____\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /___ZU__HAUS___\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /___ZU__HAUSE__\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
            r"""
        ____________
       /            \
      /___ZU__HAUSE._\
       |            |
       |_          _|
       |_|        |_|
       |     __     |
       |____|__|____|
        """,
        ] 
        self.house_label.config(text=house[min(wrong_guesses, len(house) - 1)])
    
   
    
    '''INITIAL MANDATORY GAME CONCEPTS'''
    # Player's Name Request Through Prompting
    def ask_name_window(self):
        self.enter_name_button.pack_forget()  # Hide The Enter Name Button Once Clicked

        # Create A Child Window To Ask For The Name
        self.name_prompt = Toplevel(self.window)
        self.name_prompt.geometry("400x150")
        self.name_prompt.title("Enter Your Name")

        # Color_Mode Configurations For The Window
        if self.mode == "light":
            self.name_prompt.configure(bg="#d7bde2")
        else:
            self.name_prompt.configure(bg="#17202a")

        # Add A Label In The New Window
        self.name_label = Label(self.name_prompt,text="What's your Name? / Wie heissen Sie?",font=("Raleway Bold", 15, "bold"),)
        self.name_label.pack(pady=10)

        # Add Text color For The Label According To The Mode:
        if self.mode == "light":
            self.name_label.config(bg="#d7bde2", fg="black")  # If light mode, text will be black
        else:
            self.name_label.config(bg="#17202a", fg="white")  # If dark mode, text will be white

        # Add An Entry Widget For The User To Type Their Name
        self.name_entry = Entry(self.name_prompt, font=("Raleway", 18, "bold"))
        self.name_entry.pack(pady=10)

        # Add Text Color For The Widget Depending On The Mode
        if self.mode == "light":
            self.name_entry.config(fg="black")  # If light mode , text will be black
        else:
            self.name_entry.config(fg="black")  # If dark mode, text will be white

        # Submit Button With A Function To Handle The Name Input
        self.submit_button = Button(self.name_prompt, text="Submit", command=self.submit_name)
        self.submit_button.pack(pady=10)

        # Add Text Color For The Button Too Depending on the mode
        if self.mode == "light":
            self.submit_button.config(fg="black")
        else:
            self.submit_button.config(fg="black")

    # Name Submission & Player Profile Handling
    def submit_name(self):
        player_name = self.name_entry.get() # Captures Name entered in the Entry Widget & Makes A Checkup In The Database
        if player_name:  
            existing_player = collection.find_one({"name": player_name})  

            if existing_player:  # If Name Exists, We Retrieve The Level & Score Then Display A Welcome Back Message
                self.player_name = player_name  
                self.level = existing_player.get("level", 1)
                self.score = existing_player.get("score", 0)
                self.label.config(text=f"Welcome back, {player_name}!")  
                
                # Remove The Profiles Button Then Display A Play Game Button
                self.playgame_button = Button(self.window, text="Play Game", command=self.play_game)
                self.playgame_button.pack(pady=10)
                self.profiles_button.place_forget()

            else:  # if its a new name, Set The Player Name, Create A New MongoDB Profile With Score, Correct Guesses & Level & Save It Into The Database
                self.player_name = player_name
                player_data = {"name": player_name,"score": 0,"level": 1, "correct_guesses_count": 0}
                collection.insert_one(player_data) 
                self.label.config(text=f"Good To Have You Here, {player_name}!")

                # Remove The Profiles Button Then Display A Play Game Button
                self.profiles_button.place_forget()
                self.playgame_button = Button(self.window, text="Play Game", command=self.play_game) 
                self.playgame_button.pack(pady=10)
                
            # self.name_entry.config(state='disabled') # Disable Name Entry To Prevent Further CHanges Till Reset
            self.name_prompt.destroy()  # Enable closure of the propmt window
            
        else:
            print("No name entered.")  # Handles Empty Inputs



    '''GAME PLAY SETUP'''
    # Game Play Systematics
    def play_game(self):
        self.playgame_button.pack_forget() # Remove Play Game Button
        self.profiles_button.place_forget() # Remove Profiles Button
        self.game_active = True # Enables guesses after "Play On" button is clicked
        self.correct_guesses = []  # Reset Correct Guesses
        self.wrong_guesses = 0  # Reset wrong Guesses
        self.select_word()  # Start Playing by selecting a random word in the CSV
        self.level_label.pack() #Display The Level Label
        self.level_label.config(text=f"Level: {self.level}")
        
        self.guessed_word_label.config(text=self.construct_guessed_word()) # Display Underscores For Unguessed Letters
        self.label.config(text=f"Guess a word........")
        self.hint_button.pack(pady=10) #Unhide The Hint Button
        
        #Ensure The Score_Label Is Created Only Once
        if not hasattr(self, 'score_label'):
            self.score_label = Label(self.window, text=f"Score: {self.score}", font=("Raleway", 15))
            self.score_label.pack(side=BOTTOM) #Display The Score At The Bottom Of The Screen
        
        if not hasattr(self, 'level_label'):
            self.score_label = Label(self.window, text=f"Level: {self.level}", font=("Raleway", 15))
            self.level_label.pack(side=TOP) #Display The Score At The Bottom Of The Screen
        
        if not hasattr(self, 'guessed_word_label'):
            self.score_label = Label(self.window, text=self.construct_guessed_word())
            self.guessed_word_label.pack(side=TOP) #Display The Score At The Bottom Of The Screen

    # Continue Game An Addition To Play Game
    def continue_game(self, message):
        self.game_active = False # Disables Guesses
        self.house_label.config(text="")  # Clear The House Drawing
        
        if hasattr(self,'playgame_button') and self.playgame_button.winfo_exists():
            self.playgame_button.pack_forget() #This checks if the Play On button already exists and destroys it if it does
            
        self.playgame_button = Button(self.window, text="Play On", command=self.play_game)
        self.playgame_button.pack(pady=10)

        self.playgame_button.bind("<Button-1>", self.remove_playon_button)  # PlayGame_Button Press is Binded To Click Of Remove_PlayOn_Button
        
    # Remove The Play On Button after it has been clicked
    def remove_playon_button(self, event):
        self.playgame_button.pack_forget() #Destroys the Play On Button
        self.play_game() #Restarts the game
        
    # Reset The Database Scores, Levels & Played Words, Then Restart The Game Window
    def reset_game_state(self):
        # Clear The Player's Level, Score & Played Words From Database 
        if self.player_name:
            player = collection.find_one({"name": self.player_name})
            
            if player:
                collection.update_one(
                    {"name": self.player_name},
                    {"$set":{
                        "score": 0,
                        "level":1,
                        "played_words": []
                    }}
                )
            else:
                print("Player not found in Databse")
        
        self.window.destroy() #Then Close The Current Window
        
        #Re-Open The Window & Start The Game Afresh
        root = Tk() # Create A New Instance of TK
        app = GameInterface(root)  # Create A New instance Of The Interface class
        root.mainloop()  # Start The New Game Widnow


    
    '''GAME PLAY LOGIC HANDLING'''
     # Select A Random Word From The CSV File That Has Never Been Played By The Player Before
    def select_word(self):
        # Check The Database & Get Words That Have Been Played Already By The Player
        player = collection.find_one({"name": self.player_name})
        played_words = player.get("played_words", [])
        normalized_played_words = [word.lower().replace(" ", "_")for word in played_words]
        
        # Open The CSV File
        try:
            with open("ZuHause50.csv", mode="r") as csvfile:
                reader = list(csv.reader(csvfile))  # Read the CSV file nto a list of rows
                available_words = [row for row in reader if row[0].lower().replace(" ", "_") not in normalized_played_words]  # This filters out the already guessed words by making them look exactly identical to those in the CSV
                
                # If Words Are Finished The Game Ends & Displays A Message Together With A Reset Game Buttin
                if not available_words:
                    self.target_word = None
                    self.game_active = False
                    return

                selected_row = choice(available_words)  # Randomly Select A Word
                
                self.target_word = selected_row[0].strip().lower().replace(" ", "_")  # Set The Word To Be Guessed
                self.hint_text = selected_row[1]  # Set The Word's Hint From The CSV
                self.meaning = selected_row[2] # Set The Meaning Of The Word From The CSV
                self.translation = selected_row[3]# Set The Translation Of The WOrd From The CSV
                self.translated_definition = selected_row[4]# Set The Translation's Definition From The CSV
                self.target_word = self.target_word.replace(" ", "_") # If Chosen Word Has Spaces, They Are Replaced With _
                self.correct_guesses=['_'] * self.target_word.count('_') # Same Is Implied For Correct Guesses Add space as '_'
                
        except FileNotFoundError: # Handle The Case When The File Is Not Found
            self.label.config(text="CSV File Not Found!")
            
        except Exception as e: # Handle Any Other Excepted Errors
            self.label.config(text=f"An Error Occured: {str(e)}")
    
    # Handle Guessing Game Logic Aftermath
    def handle_guess(self, event):
        if not self.game_active: # Allows Guesses Only When The Game Is active
            return
        
        guessed_letter = event.char.lower() #On Key Press, Character Is COnverted To Loewr String
        
        if guessed_letter.isalpha() and len(guessed_letter) == 1:  # Checks If Player Has Input A Single Letter
            if guessed_letter in self.target_word:
                if guessed_letter not in self.correct_guesses:
                    self.correct_guesses.append(guessed_letter)
                    self.label.config(text=f"Good Guess")
            else: #Increments Wrong Guesses Which Facilitate House Drawing
                self.wrong_guesses += 1  
                self.draw_house(self.wrong_guesses)  
                self.label.config(text=f"Wrong Guess")
                
                if self.wrong_guesses == (Max_Wrong_Guesses -5): # If Only 5 Wrong Moves Are Left, Notification Pops Up
                    self.five_wrong_guesses_left_notification()

            self.guessed_word_label.config(text=self.construct_guessed_word())

            # After Correct Guesses, Update Database
            if self.construct_guessed_word().replace(" _ ", "") == self.target_word:
                player=collection.find_one({"name": self.player_name})
                played_words = player.get("played_words", [])
                
                # Calculate The Score Based On Word Length 
                word_score = 10 
                if len(self.target_word) > 14:
                    word_score = 15
                
                # Update The Score Both Locally & In The Database
                self.score += word_score 
                collection.update_one({"name": self.player_name},{"$set":{"score": self.score}})
                
                #Update Correct Guesses Count Too & Check If Level-Up Is Needed
                self.correct_guesses_count += 1
                if self.correct_guesses_count >= 5:
                    self.level += 1
                    self.correct_guesses_count = 0 # Immediate Reset For The New Level Counter
                    
                    collection.update_one(
                        {"name": self.player_name},
                        {"$set": {"level": self.level, "correct_guesses_count": self.correct_guesses_count}}
                    )
                    
                    self.level_up_notification() # Show Level-Up Notification
                
                # Display The Word, Meanings And Score
                self.label.config(
                    text=f"Correct! The Word Was: {self.target_word.capitalize()}\n"
                    f"Meaning: {self.meaning}\n\n"
                    f"AUF DEUTSCH: {self.translation}\n"
                    f"Definition: {self.translated_definition}\n"
                    f"Your Current Score: {self.score}" 
                    )
                
                self.score_label.config(text=f"Score: {self.score}") # Update The Score Label Too
                
                self.window.after(3000, self.continue_game, "Play On") # Display Meanings For 3 Seconds, Before Adding The "Play On" Button For Display
                
                # Add The Guessed Word To The Played Words List
                if self.target_word not in played_words:
                    played_words.append(self.target_word) 
                    collection.update_one(
                        {"name": self.player_name},
                        {"$set": {"played_words": played_words}}, 
                    )
            # If Player Run's Out Of Wrong Guesses, "You Failed Message Is Displayed"
            else:
                if self.wrong_guesses >= Max_Wrong_Guesses:
                    self.label.config(text=f"You Failed")
                    self.continue_game("You Failed")
        else:
            self.label.config(text="Invalid input")  # Display an incorrect message
    
    
    
    '''NOTIFICATIONS SETUP'''
    #Display A Level Up Notification
    def level_up_notification(self):
        self.notification_label.config(text=f"Level Up! You're Now On Level {self.level}", fg="white", bg="blue")
        self.window.after(3000, self.clear_notification) # Clear Notification After 3 Seconds
    
    # Display A Notification When There Are Only 5 Wrong Guesses Left    
    def five_wrong_guesses_left_notification(self):
        self.notification_label.config(text="Only 5 Wrong Guesses Left!", fg="black", bg="red")
        self.window.after(3000, self.clear_notification) # Clear Notification After 3 Seconds 
    
    # Clear Notification After A Set Amount Of Time
    def clear_notification(self):
        self.notification_label.config(text="")
        
        
        
    '''GAME DISPLAYS'''
    # Display The Hint For The Current Word If It Exists
    def hint(self):
        if self.hint_text: 
            self.label.config(text=self.hint_text)  
        else:
            self.label.config(text="No hint available.")
    
    # Word Construction
    def construct_guessed_word(self):
         # If Words Are Over, A Reset Button Is Displayed Together With A Game Over Message
        if self.target_word is None:
            self.game_active = False
            self.level_label.pack_forget()
            self.hint_button.pack_forget()
            if not hasattr(self, 'reset_game_state_button'):
                self.reset_game_state_button = Button(self.window, text="Reset Game", command=self.reset_game_state)
                self.reset_game_state_button.pack(pady=10)
                return "Game Over, No More Words Available.\nCongragulations, Word Genius"
        
        guessed_word = ""
        for letter in self.target_word:
            if letter in self.correct_guesses:
                guessed_word += letter
            else:
                guessed_word += " _ "
        return guessed_word
    
    
    
    '''ON GAME-SITE PROFILE MANAGEMENT'''   
    #Check Player Profiles       
    def show_profiles(self):
        #  Check If They Exist Then Hide All Game Elements Temporarily
        if hasattr(self, "score_label"):
            self.score_label.pack_forget()
            
        if hasattr(self, "level_label"):
            self.level_label.pack_forget()
        
        if hasattr(self, 'enter_name_button'):
            self.enter_name_button.pack_forget()
        
        if hasattr(self, 'guessed_word_label'):
            self.guessed_word_label.pack_forget()
        
        if hasattr(self, 'label'):
            self.label.pack_forget()
            
        if hasattr(self, "hint_button"):
            self.hint_button.pack_forget()
        
        # Hide The Delete Buttons Before Showing Profiles Again
        for button in self.delete_buttons:
            button.pack_forget()
        self.delete_buttons.clear()
        
        # Query The Database To Get All Player Profiles
        players = collection.find() # Fetch All Players
        
        # Create A List Of The PLayer Profiles
        profiles_list = []
        # Loop Through Players And Display Their Names & Scores Excluding Other Details
        for player in players:
            player_name = player['name'] 
            player_score = player['score'] 
            profiles_list.append(f"{player_name} - {player_score}") # String The Display
            
            # Create A Button To Delete The Profile Using The Lambda Function Which Passes THe Name of The Profile To Delete
            delete_button = Button(self.window, text=f" Delete Profile", command=lambda 
                                   name=player_name:self.delete_profile(name))
            self.delete_buttons.append(delete_button) # Store The Button
            delete_button.pack() # Show Delete Button
            
        # Join The List Of Profiles Into A Single String
        profiles_text ="\n".join(profiles_list)
            
        # Update The Profile Label Text With The Fetched Data
        self.profiles_label.config(text=profiles_text)
        
        # Un Hide The Profiles Label
        self.profiles_label.pack()
        
        # Show The Main Menu Button
        self.show_back_button(self.setup_ui)
        
    # Deletes The Player Profile From Both The Game & Database
    def delete_profile(self, player_name):
        result = collection.delete_one({"name": player_name})
        
        if result.deleted_count > 0:
            self.label.config(text=f" Success! {player_name} Profile Deleted Successfully")
        else:
            self.label.config(text=f"Error! {player_name} Not Found")
        
        #Refresh The Profiles List After Deletion
        self.show_profiles()

    

    '''BACK BUTTON SYSTEMATICS'''
    # A Button To Take Us Back To Previous Screens
    def show_back_button(self, previous_screen_function):
        if hasattr(self,'back_button') and self.back_button:
            if self.back_button.winfo_exists():
                self.back_button.place_forget() # Remove Previous Back Button, If Any 
         
         # Only Show A Back Button If A Previous Screen Function Is Provided   
        self.back_button = Button(self.window, text="Main Menu", command=lambda: self.go_back(previous_screen_function))
        self.back_button.place(relx=0.0, rely=1.0, anchor=SW, x=10, y=-10)
    
    # Logsout Player, Clears Screen, Then Lands Back To Previous Screen
    def go_back(self, previous_screen_function):
        if hasattr(self, 'back_button'):
            self.back_button.place_forget()
        self.clear_screen()
        previous_screen_function()
    
    # Destroys All Widgets On The Screen To Clear The UI
    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()
               

#  Initiate The Tkinter main loop, Where The Display Window Appears And Handle User Interactions
root = Tk()
app = GameInterface(root)  # Create An instance Of The Interface class
root.mainloop()  