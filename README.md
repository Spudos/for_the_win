# For the Win

![Mockup image](/images/home_screen.png)

[Live webpage](https://for-the-win-a2a63eea4e56.herokuapp.com//)

## Table of Contents

- [1.0 Introduction](#10-introduction)
- [2.0 User Stories](#20-user-stories)
  - [2.1 As a User](#21-as-a-user)
  - [2.2 As the Site Owner](#22-as-the-site-owner)
- [3.0 Project logic](#30-project-logic)
- [4.0 Features](#40-features)
  - [4.1 Welcome Screen](#41-welcome-screen)
  - [4.2 User Login](#42-user-login)
  - [4.3 Team Selection](#43-team-selection)
  - [4.4 Match Engine](#44-match-engine)
- [5.0 Testing](#50-testing)
  - [5.1 PEP8 Validation](#51-pep8-validation)
  - [5.2 Test User Stories](#52-test-user-stories)
- [6.0 Unresolved Bugs](#60-unresolved-bugs)
- [7.0 Deployment](#70-deployment)
- [8.0 Credits](#80-credits)
- [9.0 Technologies and Libraries Used](#90-technologies-and-libraries-used)

## 1.0 Introduction

Back in the 1980s, football play by mails were enjoyed by thousands of fans.

A gamemaster, or GM, would have software on a very low-level computer that would simulate the 
management of a football club and print out the results.  It was not fantasy football in modern 
terms as it bore no relation or had no connection with real life.  These were fictitious clubs
and players and managers from around the world would wait for results to be posted to them 
before filling in a turn sheet and posting it back for the next game.

While they still exist today, they are of course not as popular thanks to modern games like
Championship Manager and FIFA.

For the Win taps into those memories.  Just like the PBMs, FTW has a myriad of background stats,
a random element and the ability to pick whatever team you want from the players available.

Players are then given a performance rating to see how well they did, you are told who was the 
man of the match and who assisted and scored goals.

This is a cut down version of the concept as you can include many hundreds of features and 
adjustments to allow the manager to create his or her perfect team but it certainly reminds 
the user of the experience and introduces the newcomer to what is known by some as the
good old days of football gaming.

## 2.0 User Stories

### 2.1 As a User

1. Play a fun, interactive football based game multiple times with simple to understand rules and see the outcome

2. Be reminded of or introduced to PBMs the 80s and 90s

3. Pick whatever team I want to take on another (computer) manager

4. See detailed and realistic match output

5. Log in so that in future versions of the game I can review my results

### 2.2 As the Site Owner

6. Store data in an easy to access medium so that details can easily be edited as required

7. Have clear code with granular functions for ease of understandability, readability and maintenance

8. Have multiple 'behind the scenes' stats and some random elements that maintain the unpredictability of the results

## 3.0 Project Logic

The data flow and logic for the app is shown in the images below

Stage 1 - User login Logic
![User Login](/images/flow_login.png)

Stage 2 - Team Selection Logic
![Team Selection](/images/flow_selection.png)

stage 3 - Match Engine Logic
![Match Engine](/images/flow_match_engine.png)

## 4.0 Features

### 4.1 Welcome Screen

The welcome screen shows the game logo and introductory instructions and text.  Pressing any key on this screen progresses you to the log in screen

![Welcome Screen](/images/home_screen.png)

User Stories covered - 1, 2, 5

### 4.2 User Login

The user is asked if they have existing details to log in and if not, details can be created.  If the user has details they can log in and play the game

![user Login](/images/user_login.png)

User Stories covered - 5

### 4.3 Team Selection

The user picks their team using a simple selection method using the id of the player they want to select before being shown a summary of the team they picked and the team they are up against

![team Selection](/images/team_selection.png)

User Stories covered - 1, 3

### 4.4 Match Engine

Performance ratings are calculated for the teams at a player level before being amalgamated into total figure for defence, midfield and attack.  These ratings are then used to decide the outcome of the game and generate stats

![Home Team](/images/home_team.png)

![Away Team](/images/away_team.png)

![Match Outcome](/images/match_outcome.png)

User Stories covered - 1, 4

## 5.0 Testing

### 5.1 PEP8 Validation

The Code Institute python linter was use to validate the project code 

![PEP8 Linter](/images/pep8_linter.png)

### 5.2 Test User Stories

### As a User

1. Play a fun, interactive football based game multiple times with simple to understand rules and see the outcome

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Whole app | Following the linear processes within the game you start with simple instructions and finish with the match results | all criteria satisfied |

2. Be reminded of or introduced to PBMs the 80s and 90s

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Python in a terminal design method | The feel of the early games is retained by the simple coloured text of basic output to a terminal.  Features and style are in keeping with those games | all criteria satisfied |

3. Pick whatever team I want to take on another (computer) manager

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Team selection | Complete flexibility is given in the team selection screen as long as 11 players are picked and every player is selected once.  Validation ensures this is the case | all criteria satisfied |

4. See detailed and realistic match output

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Match Output | the final details given describe a summary of the game with 8 different elements highlighted to tell the user how the players and team performed | all criteria satisfied |

5. Log in so that in future versions of the game I can review my results

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Login functionality  | The ability to create or use existing credentials exists | all criteria satisfied |

### As the Site Owner

6. Store data in an easy to access medium so that details can easily be edited as required

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Google sheets | Ease of use and maintenance make these ideal for the requirements of the owner | all criteria satisfied |

7. Have clear code with granular functions for ease of understandability, readability and maintenance

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| run.py | The function 'main' links to the functions in the code with some of those functions calling sub-functions as required.  Emphasis was placed on not repeating code where possible as this is easy to do when you run all the code twice to generate two teams | all criteria satisfied |

8. Have multiple 'behind the scenes' stats and some random elements that maintain the unpredictability of the results

| **Feature** | **Action** | **Result** |
|-------------|------------|---------------------|
| Google sheet and game functions | Variables are included in the code that directly affect the outcome of games and also controls random elements.  Player stats are more details than shown which also facilitates more features in future versions of the game | all criteria satisfied |

## 6.0 Unresolved Bugs

All bugs were resolved as they were discovered

## 7.0 Deployment

Pre deployment steps

1. The end of all input instructions need \n to ensure it works with the terminal code from the template
2. from a terminal command in the directory of the project run

   pip3 freeze > requirements.txt

   To ensure the requirements file is built.  Heroku needs this to deploy the project

The website was then deployed using GitHub to Heroku by following these steps:

1. From the Heroku dashboard select 'New' then 'Create new app'
2. Give your app a name and select a region the click 'Create app'
3. In 'Deployment method' select GitHub
4. In 'Connect to GitHub' press search and select the name of your project in Github
5. Click 'Enable Automatic Deploys' so the game will update with each push to GitHub
6. Scroll back to the top of the screen and select 'Settings'
7. Click 'Reveal Config Vars'
8. In the 'Key' field enter 'port' and for 'value' enter '8000' and click 'Add'
9. Click 'Add' again and enter a value of 'creds'
10. Copy the entire contents of you creds.json from your local project and paste them into the 'value' field and click 'Add'
11. You will now be able to click 'Open app' near the top of the Heroku screen to see the project

You can for fork the repository by following these steps:

1. Go to the GitHub repository
2. Click on Fork button in upper right-hand corner

You can clone the repository by following these steps:

1. Go to the GitHub repository
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

## 8.0 Technologies and Libraries used

### Technolgies Used

  Python - To code the project
  Google Cloud and Sheets - Stire data for the game
  PEP8 - Used to verify the code was free from errors in Python conventions
  Drawio.net - Flowchart design
  Git and Github - Version contol
  Visual Stuido - Code editor
  Heroku - Live deployment of the project

### Libraries used

  Gspread - To use google sheets via api
  Random - To generate randome numbers
  OS - For terminal functions like clear
  Google.oauth2.service_account - To use google sheets via api
  Colorama - Text styling

## 9.0 Credits

  No particular guide was used to help create this game btu stack overflow aand other random google serch results were used to help me understand the syntax of some elements where they were not covered in the course

  I also use the book, Python Programming for Beginners by Mark Reed as a handy reference

  Finally thanks to my mentor, Mo Shami, for his advice and guidence throughout my project
