ZUHAUSE50:

ZuHause50 Is A Word Guessing Game  Whose Idea Was Inspired By A Word Game That Me, My Sister & Brother Used To Play Growing Up Called "Buyumba" Which Means "Home".

"ZuHause" The German Word Simply Means Home While The Number "50" Represents 50 Words. "ZuHause50" Is Also A Fusion Of Tech Between Two Languages.

Because The 50 Words Are Commonly Used English Tech Words That Once Guessed Correctly Lead To A Display Of Their Deutsch Translation & Definition To The Player.

CLICK THUMBNAIL BELOW TO WATCH A SHORT VIDEO DESCRIPTION

[![Video Description](ZuHause50Logs/LogoPNG.png)](https://youtube.com/shorts/CqZsqFJkuPQ?feature=share)

FEATURES
- User Profiles & Data Stored In MongoDB & Can Be Viewed In Game In Highest Score Order
- Word Guessing With Level Progression
- Responsive GUI With Tkinter


INSTALLATION
1. Install Python 3.x On Windows
2. Clone The Game Repository.
3. Navigate To The src Directory.
4. Create A Virtual Enviroment By Running: " python -m venv myenv " in the command prompt.
5. Activate The Enviroment On Windows By Running: " .\myenv\Scripts\Activate.ps1 "
6. Install Required Libraries By Running: " pip3 install -r requirements.txt "
7. Test The MongoDB Connection By Typing "python test_mongo_connection.py"
8. Run The Game With: " python ZuHause.py "
9. Enter Your Name To Create A Profile. ENJOY THE GAME !!!!!

USAGE
- Navigate to the src folder 
- Run The Game With : python ZuHause.py
- Create A New Profile Or Log In
- Play By Checking For Hints & Guessing Words

API DOCUMENTATION
Game Interface Class: This is the main driver for the game's functionality, containing methods for UI Creation, Gameplay Logic & Database Interaction. Mainly Consist Of;

1. User Login:
- This Part Of The API Manages Player Authentication & Profile Management.
- Login Means That The System Checks If A Player Already Has An Exisiting Profile In The Database. If Not, The System Creates A New Profile.

The Login Process Consists Of:

i. ask_name_window()-
Prompts The Player To Enter Their Name & Stores It In The Database If It Doesnt Exist.

ii. submit_name()-
Handles Submitting The Player's Name. If The Player Exists In The Database, It Loads Their Profile Or Else Creates A New Profile.

2. Word Selection:
- This Part Of The API Is Responsible For Selecting The Word That The Player HaS To Guess.
- The Game Picks A Random Word From The CSV Which COntains The Words, Hints & Meanings.
- It Ensures That The Word Has Not Been Guessed Yet In The Current Session To Prevent Repeats.

The Word Selection Process Consists Of:

i. select_word()-
Selects A Random Word From The CSV That Hasn't Been Guessed Yet.

3. GamePlay Logic:
- This Ecompasses The Rules & Mechanics That Run The Game. 
- It Includes Handling Player Guesses, Providing Feeback Whether Its Correct Or Incorrect, Tracking Progress Of Letters Of Already Guessed Plus Remaining Attempts, Level Progression & Game End Where Player Can Reset The Game. 

The GamePlay Logic Consists Of:

i. play_game()-
Starts The Gameplay By Selecting A Random Word From The CSV File & Managing The UI Updates For Gameplay

ii. handle_guess(event)-
Handles The Player's Guess Input, Updates The Guessed Word And Checks If The Guess Is Correct Or Wrong

iii. continue_game(message)-
Allows The Player To Continue The Game AFter They Guess A Word Or Fail To Guess The Word Within The Allowed Attempts.

iv. clear_notification()-
Clears The Notification Message After A Set Amount Of Time

ZU HAUSE Blueprint.
1. VSC Code to write the code.
2. MongoDB to store player profiles, scores and words they have guessed already.
3. Tkinter to design the Graphical User Interactive mode.
4. CSV to store words.
7. GITHUB to share the code.
8. Virtual enviroment to install the libraries like pymongo.

IMPORTANT TO NOTE:

- Once ZuHause Is In GamePlay Only Way Out Is By Closing The Window.
- Profiles Can Only Be Viewed At The Start Of The Game Before Name Submission

NOTABLE RESOURCES 

- W3Schools MongoDB Tutorial : https://www.w3schools.com/mongodb/index.php
- Datacamp's Gui Tkinter Tutorial : https://www.datacamp.com/tutorial/gui-tkinter-python
- Linie 1 A1 - B1 Deutsch Books & ChatGPT For German Words & Translation


Screenshots 
![alt text](<Dark Mode ScreenShot.jpg>)
![alt text](<../imgs/Light Mode ScreenShot.jpg>)
![alt text](<Name Entry ScreenShot.jpg>)
![alt text](<Game Play ScreenShot.jpg>)
![alt text](<../imgs/Profile ScreenShot.jpg>)
![alt text](<Game Final Screenshot.jpg>)

TROUBLESHOOTING.
Common Issues:
1. MongoDB Connection Error
Make Sure Your MongoDB Service Is Running & Accesible.

CONTRIBUTION
Contributions Are Welcome For Bug Fixes, Enhancements & Additional Features After Contacting Me & Letting Me Know Where Exactly You Would Like To Improve Or Addon. After Contact & Aprroval You Will Get Instructions On Steps For Contribution.

LICENSE
This Project Is Licensed Under The MIT License.
