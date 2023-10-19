import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    amount: str

@dataclass
class Recipe:
    title: str  # The title of the recipe
    ingredients: list[Ingredient]  # A list of Ingredient data class instances
    instructions: list  # A list of cooking instructions
    prep_time: int  # Preparation time in minutes
    cook_time: int  # Cooking time in minutes
    servings: int  # Number of servings
    cuisine: str  # The type of cuisine (e.g., Italian, Chinese)


class WebScrape:
    def __init__(self, url=""):
        self.url = url
        self.curRecipe = Recipe()

    def __checkSite(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        return None

    def Scrape(self):
        # soup = BeautifulSoup(self.__checkSite(), 'html.parser')
        '''
        parse text for:
        recipe name
        ingredients
            name
            amount
        prep time
        cooking time
        servings
        type of cuisine
        
        BIND TO self.curRecipe
        '''
        self.curRecipe(
            title= 'test',  # The title of the recipe
            ingredients= [
                Ingredient(name='ing1', amount='1')
                ],
            instructions= ['thing'],
            prep_time= 30,
            cook_time= 20,
            servings= 5,
            cuisine= 'new yotk'
        )

    



if __name__ == '__main__':
    ws = WebScrape()
    ws.Scrape()
    print(ws.curRecipe)
# # Define the URL of the webpage you want to scrape
# url = "https://example.com/articles"

# # Send an HTTP GET request to the URL
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content of the page using BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Locate the HTML elements containing the data you want to scrape
#     # Here, we're looking for article titles within <h2> tags
#     article_titles = soup.find_all('h2')

#     # Loop through the article titles and print them
#     for title in article_titles:
#         print(title.text)
# else:
#     print("Failed to retrieve the webpage. Status code:", response.status_code)
