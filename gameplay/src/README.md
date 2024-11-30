Redi-School | Python Final Project | Word Guess Game: Zu Hause


ZUHAUSE:
Zu Hause is a name that i came up with for my final project due to its Nature. ZU Hause project Will Be A Word Guess Game That Allows User to Guess Letters.


BACKGROUND
During my childood, my late step-brother would make me and my sister play a word guessing game.
He would divide a paper into two columns and then draw "_" for the word's letters both sides. (One Being Mine and One For My Sister)

We would then go ahead and whoever got it first before a simple house was built and the word HOME added in the roof, 1 point would be added to their score before we would go on to another word.

For Example:
If we had to guess a word "BOY",
Lay out would be like this:

Mustafa             Rose
_ _ _     |    _ _ _
          |
          |

We would each take turns and for every wrong guess a line house would be built: 
That means we would each have about 20 moves(with small windows built too) to build a whole house and loose.
If the word HOME was added to the roof. It means the guessor has lost and would have to move on to the next one.
  ______
 / HOME \
 --------
 |   _  |
 |_ |_|_|


ZU HAUSE DYNAMICS
With that brief background, i would like to bring that game to the Tech Life. 
Named Zu Hause a Deutsch Word for the English noun "home", the Game will have the same play mode as before.
Difference is that, once a player guesses the English word correctly, its Deutsch meaning is displayed too.

For example:
If The word was BOY and player gets it correctly. A display like this comes up:
_______________________________________
You Guessed it right!!!!!!!!!!!!!!!!!!
In Deutsch:
Die Frau / Die Frauen (pl)
Press Next To Continue to aother word__


ZU HAUSE MODE
1.Player Profiles will be created and saved on a database.
2.Words will be selected randomly from CSV Files which will have about 50 word depending on the German Level.
3.For every word guessed right, it will be added to the players profile in the databse so that its not played again. This will faciliate getting to newer levels. Hints for the word will also be displayed while guessing.


ZUHAUSE GOALS
This is to make a game which can help the player learn what the words they have guessed mean in German.


ZU HAUSE Blueprint.
1. VSC Code to write the code.
2. MongoDB to store player profiles, scores and words they have guessed already.
3. Tkinter to design the Graphical User Interactive mode.
4. CSV to store words and their levels.
5. Win10's Toast to notify the user when they have a few wrong guesses left or moved on to another level.
6. API's to get hints for the randomly selected word.
7. GITHUB to share the code.
8. Virtual enviroments to install the libraries like pymongo.