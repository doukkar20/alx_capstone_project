from flask import Flask, render_template, request
import requests
from urllib.parse import unquote

app = Flask(__name__)

API_KEY = '8c5108999873490cb6e365e532ec4762'

# ----------> ROUTES <---------- #

# "Home" --> button
@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html', recipes=[], search_query='')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# Main route for the app
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('search_query', '')
        recipes = search_recipes(query)
        return render_template('index.html', recipes=recipes, search_query=query)

    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    recipes = search_recipes(decoded_search_query)
    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)

# Search recipes by query
def search_recipes(query):
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 10,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    return []

# Define route to view a specific recipe with a given recipe ID
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    search_query = request.args.get('search_query', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        recipe = response.json()
        return render_template('view_recipe.html', recipe=recipe, search_query=search_query)
    return "Recipe not found", 404

# Run the app in debug mode if executed directly
if __name__ == '__main__':
    app.run(debug=True)