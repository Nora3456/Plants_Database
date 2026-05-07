[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21211519)

# Plants Database!

This is a Python and MySQL databse that allows users to manage a plant collection! They can view, update, add, and delete plants while story key informattion like plant name, plant type, size, location, and more!

🔮🪄🤔👣🧐🧙🔮🪄🤔👣🧐🧙🔮🪄🤔👣🧐🧙🔮🪄🤔👣🧐

## ERD 
- This is my created ERD (Entry Relationship Diagram), it shows the draft process of my program, that includes how each entity has a relationship to another. 
- INSERT ERD SCREENSHOT

## You might be wondering, how do you use this plant database manager?

Below is a detailed step-by-step walkthrough of how to use the plant database manager + run the code.
<br/> 

### Requirements:
Here are NECESSARY requirements to run this application:
- Python 3
- MySQL Server
- mysql-connector-python

### First, how to run the program:

1. Save the project files, name it something relate to the porgram like "plant_manager"
2. Open your terminal
3. Navigate to the folder your saves files are in
4. Enter "python main.py" in your terminal

##  How to run/play the simulator after opening the program:

1. 👋 | The application will ask you if you would like to add a plant, view plants, update plants, delete plants, or exit the application. Pick the number that corresponds with the choice you would like to do, type it into the "Choice:" section, and press enter.

- **Adding a Plant**:
2. 🤔 | If you input 1, than you want to **add a plant!** 
- You will be asked for a plant name (Name it anything you like, it could match the color of the plants pot, when you got it, etc., make it fun!) after inputing your chosen plant nme, press enter.
- Re-type your plant name and press enter
- Enter the age of your plant (6 months, 2 years, etc., make sure to include "weeks", "months", "years", etc. after your number so that you are aware of your measurement of time and growth.).
- Then enter your chosen plants type. Listed plants include (but not limited to) Pothos, Bamboo, Cactus. If your plant is any of the pre-added types, input the number associated with that type and press enter. If your plant type is **NOT** on the pre-added list, input 0, and press enter to than add the new plant type. 
- Input the number associated with the size of you chosen plant (extra-small, small, etc.), and then press enter. 
- Input the number associated with the location of your chosen plant, if the location your plant is in does not match the pre-made list, than input 0 and press enter to add a new location, otherwise input a number from the pre-added list and press enter.
- Input the number associated with the level of sunlight your plant receives, then press enter. 
- **You have succesfully added a plant!**
** EXAMPLE: **
- INSERT ADD NEW PLANT SCREENSHOT HERE


3. 🧐 | If you input 2, you want to **view your plants!** You can see the name of you plant first, followed by all the information you included about your plant from step 1! If you don't see your plant, than you likely interrupted your add before succesfully adding your plant. Re-input your plants information if so. 

3. 🎉 | If you input 3, you want to **update a plant(s)!** 
- Click the ID number associated with the plant that contains information you would like to update. You can update the Name of the Plant, or the Age of the plant. 

4. 🎉 | If you input 4, you want to **delete a plant!** 
- Click the ID number associated with the plant that you want to delete.
- You will be prompted a conformation message do make sure you DO want to DELETE your plant.
- If you are sure you want to delete your plant, input "yes" and press enter, if not, input "no" and press enter.

## Table Descriptions
"""INSERT MYSQL TABLES SCREENSHOT"""
- **plants**: stores information about individual plants (name, age, etc.)
- **plant_types**: stores plant categories (Pothos, Aloe Vera, etc.)
- **sizes**: stores plant size options
- **locations**: stores where plants are located
- **sunlight_levels**: stores sunlight requirements

## Troubleshooting
- **If MySQL connection FAILS**, check to make sure your username and password are correct, and that MySQL is running. 

- If "table doesn't exist", make sure that schema.sql has been saved.

- If Python shows an error like "mysql.connector not found", run: pip install mysql-connector-python


## Reflection
This assignments 

## Happy Plant Managing!
 
 <img src="Destiny.gif" alt="Photo gif of Darth Vader saying If that is your destiny." width="200"/>  <img src="choices.gif" alt="Photo gif of person looking between 2 optiions, a diamond or scribble." width="200"/>