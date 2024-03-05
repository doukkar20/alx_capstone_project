********************
pip install virtualenv
virtualenv venv
********************
venv\Scripts\activate
********************
pip install Flask
pip install requests
code .
********************
set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_DEBUG=1
flask run
********************
create the app.py
short the imports
from flask import Flask, render_template
app = Flask(__name__)
Congratulations! You’ve just created your first web application with Python and Flask.
********************
get and paste API KEY
********************
define and set the home button method/ function
methods=['GET'] --> for the 'index.html'
Render the main page with empty recipe list and search query
render 'index.html'
********************
create templates folder
create index.html inside the template folder
********************
Define the main route for the app
create the index home view -- main route
methods=['GET', 'POST']
Perform a search for recipes with the given query
1 - if request.method == 'POST':
    If a form is submitted
    Perform a search for recipes with the given query
    Render the main page with the search results and the search query
2 - if request.method == 'GET':
    If it's a GET request or no form submitted
    Perform a search for recipes with the decoded search query
    Render the main page
********************
Define search function/method
Function to search for recipes based on the provided query
Send a GET request to the Spoonacular API with the query parameters
1 - If the API call is successful
    response.status_code == 200:
    Parse the API response as JSON data
    Return the list of recipe results
2 - If the API call is not successful
    return []
********************
Define route to view a specific recipe with a given recipe ID
Get the search query from the URL query parameters
Build the URL to get information about the specific recipe ID from Spoonacular API
Send a GET request to the Spoonacular API to get the recipe information
1 - If the API call is successful
    response.status_code == 200:
    return the result
2 - If the API call is not successful
    return 404 error of not found
********************
set debugmode to True
********************
Setup the index.html
********************
Define a form with method="POST"
button --> Home
********************
Display logic
********************
Create logic which will contain all the code needed in order to display the recipe cards, including their images
********************
run the app()
********************
Create CSS styling
********************
create base.html

