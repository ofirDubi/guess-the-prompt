# Dataset todo
Some of the images (especcially in the same part) have very similar if not identical prompt and just different hyperparameters.
@TODO -
1. filter the images to prevent these duplications
2. images are not so good, descriptions are complicated and not fun

# Server
1. 

# Web (lovable)
@TODO - 
2. test everything (create a list of quick tests maybe)


# howto run 
## server
1. cd gtp-server
2. flask run
## client
npm run dev







# Prompt to GPT to generate the server
You are an expert at developing backend for games, especially in implementing API datasheets in python using flask and sql. Your are also very kind.
I desperately need your help, and will also compensate you greatly if you do an excellent job.


I am developing a web based game which is called "Guess The Prompt". In the game each round the player is presented with an image which was generated using an AI Image generator with a specific prompt.
The game currently has 3 game modes - Casual, Daily Guess and Progress mode.
Progress mode is a level based game mode.
Your mission is to write the server side code.
The server code should be written in python 3 using flask and waitress.

The frontend web client communicates with a dedicated server in order to retrieve prompts and images, perform user login and authentication and fetch other data. 
The web client communicates via requests with the server api.

the progressLevel objects stores data on the user's progress in Progress mode
it looks lik this - 
"progressLevels": [            // Progress mode levels state
    {
      "level": number,           // Level number
      "completed": number,       // Number of completed images
      "total": number,           // Total images in level
      "guesses": number,         // Number of guesses used
      "unlocked": boolean        // Whether level is unlocked
    }

The server should have am sql database with the following tables - 
1. user table - contains information on the different users, should have the following columns - 

token (unique id), username, password hash, casualScore, dailyScore, progressLevel 
2. leaderboard table - should have 3 tables, one for each game mode, which contains user ids and scores sorted by their score.  


the images are stored in data/selected_images folder.
the images information is stored in data/selected_images/selected_images.csv file. 
upon initialization the server will load the selected_images.csv file as a dataframe for later use.


I have created the frontend for the game and an API datasheet for api between the client and the server.
The datasheet is uploaded here as "api-documentation.md" file. 

I will now provide further instruction on how to implement some endpoints. 
*Authentication* 
Each sign up if the user does not exist create a new token for it and store it in the db. if it does exists return an error to the client. 

*Guesses*
upon receiving a guess, calculate the match score by doing fuzzy word similarity using the fuzzyset library. the user should get 90% if all the words were guessed correctly, and 100% if they were guessed correctly and in the right order.  
Note that the user should not get more point for the same word if it appears more times in it's than in the prompt. in other words, each word in the prompt has some points which it can give to a word in the guess, it will give it to the closest word in the guess if there are fuzzy matching word, and to no words in the guess if non fuzzy match it.

Please generate the server backend in python.



Next, the image endpoints. The images are stored in a CSV file, which needs to be loaded into a DataFrame on server start. So I'll read that CSV using pandas and store it as a global variable. For the random image in casual mode, pick a random row from the DataFrame. For daily, maybe pick one based on the date to ensure it's the same for all users each day. Progress mode images are per level, so the DataFrame should have a level column to filter by.


This needs clarification, but given the user's instruction, I'll proceed with separate tables. So each leaderboard table (casual, daily, progress) will have entries for each user with their respective scores. For progress, the score is the average guesses per level.

The progress mode image selection assumes that the DataFrame has 'level' and 'image_number' columns. The CSV should be structured accordingly.

The fuzzy matching logic for exact and similar matches in the guess response is not fully implemented. The current code returns empty lists for similar matches. 

The 'hasSubmittedToday' field in the daily image response is not implemented, as tracking daily submissions requires additional logic (like storing the last submission date per user).

Error handling for missing images or invalid levels needs to be added. 
---
make the following improvments - 
1. implement the 'hasSubmittedToday' field in the daily image response by adding an entry in the user database with the las submmision date.
2. handle errors for missing images and invalid levels by returning errors to the server. implement input validation and return an error to the server if needed,
3. Add logging functionality to all endpoints, which will document the requests. make it optional to print the logs to the screen while debugging. 
4. Add special treatment for when the user id is "guest" - in that case no db updates should never occur - because the user is not logged in. This will be a default user.


---
Now please help me generate the images csv. 
I have a dataset of images and a base csv which describes the dataset. I will upload it, it is called "base_dataset.csv".
From it i want to generate the selected_images.csv which the server will load and use.
Write python code that will generate that for me.
Note that the levels should increase in difficulty within the level and also between different levels. an easy image is an image with a short prompt. for example, in the first level most of the images needs to be easy to guess, but near the end of the level they should be more difficult. the images at the second level should also be relatively easy, but harder than the first level. again at the end of the second level the images should be a little bit harder. 
 



 -----

 make the following changes - 
in the function "fetchGameImage" when fetching the image from the server, change the function so that the server will not return the prompt of the image, only the prompt length.  


Add a user system to the game. sign up and login buttons at the upper right corner of the screen. next to those buttons show the current logged on user and the total score of that users.
users who have not logged in will be playing as guests which start with 0 score. 
At each currect guess send an api request to the server so it will know to update the user's current score. also update the score displayed on the UI.

The game discribed this far is a game mode called "Casual Play". Add another game mode called "The Daily Image" in which each day the server will send a new image and prompt. 
There will be a different score table for "The Daily Image" mode. when the user submits his guess in this game mode it will be sent to the server and added to a dedicated score sum for this game mode.
Once the user submitted his guess for this game mode he will be prompted to return tomorrow for the new image and a ticking time clock which counts backwords to the new image apperence will be displayed.  

Add a leaderboard page. the leaderboard page will send a request to the server which will return the top 1000 users and their scores.
The leaderboard page will displayed these users in a scrolable table. 


Make the website mobile compatib



-------


make the following changes - 
1. When pressing the button turn them into a loading wheel so the user will see some responce from the UI even if the server has not responded yet.
2. When presenting the results of the guess you will receive from the server the words which where an exsact match to the prompts and the words which were not an exact match but where similar and contributed to the score. paint in green the part of the guess which perfectly corresponded to the prompt, paint in dark yellow the parts which where similar to the prompt but not an extact match.
3. change the "How To Play" section so it will include instruction on the current game mode - in casual play you can play infinite number of images. In daily challenge there is one hand-picked challenging image whith a longer prompt each day.
4. When signin up add another field to verify the password. Also add a little prompt that says that the username entered will be displayed in the leaderboard.  
5. Guests cannot submit answers to the daily challenge. if a guest tries to submit a guess show a popup which asks him to sign up in order to submit answers for the daily challenge. 
6. Add a background to the leaderboard button. 
6. In mobile view some of the icons in the upper part of the screen are not visable because the resolution is not wide enough. fix this so all icons will be viewable in mobile version. It is very important that the web page will look good on mobile phones as they are the main costumers of this application. Do the necessery changes so that the UX will be excellent on phone screens.
7. instead of sending the password, send a hash of the password.
8. add a comment block in the code in "gameServices.ts" which specifies exactly the api that is expected from the serve. for each requests that is sent specify the fields of the request and their data type, and for each expected response specify the expected response fields and data types.

-----

make the following changes - 
1. in mobile the mode selection pane overlaps with the "how to play" pane. fix it so they won't overlap.
2. if the user tried to submit an empty guess, show a popup that says "Input your guess before submitting"
3. introcude a new game mode - "progress mode" This mode will be a level-based mode. Each level will contain 40 images which 


In Casual Mode, after the guess is submited and the responce from the server with the original prompt is received, give the user the oprotunity to guess again after you display the result of the guess but before reveiling the original prompt.
The container which showed the prompt text should contain a button which says "reveal original prompt", which only reveals the prompt if clicked.
Also add a button to try again to guess the same image next to the button that allows you to continue to the next round.

Another thing - the sumbit guest API has changed a bit. Instead of similarity we get accuracy, it has the same value but a different name. 
Also similarMatched now returns an array of tuples, each value is a tuple of the form (guess_word, promp_word), these are words which were similar but not an exact match. 
Use the similarMatched field and the exactMatches field to paint the similar words in the guess and the prompt in yellow and the exact matches in the guess and the prompt in green.
if the user does not choose to uncover the prompt, still paint the guess words in the apropriate colors.


keep the user's previous guess in the input box of the guesses after submiting a guest, so it will be easy to edit the previous guess and resend it. 



---------------
make the following changes -
1. In daily Challenge mode, if the user tries to reveal the prompt show a popup that warns him that after revealing the propmt any further guesses will not be counted in his score. Give the user the option to return without revealing the prompt or to continue and reveal the prompt
2. In daily Challenge mode if the user chooses to reveal the original prompt, send an appropriate request to the server so he will know that the user has revealed the prompt and will not add to it's score for any following guesses in that day. 
