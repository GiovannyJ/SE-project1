import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
import json


@dataclass
class Recipe:
    title: str  # The title of the recipe
    ingredients: list  # A list of Ingredient data class instances
    instructions: list  # A list of cooking instructions
    # prep_time: int  # Preparation time in minutes
    # cook_time: int  # Cooking time in minutes
    servings: int  # Number of servings


class WebScrape:
    def __init__(self):
        self.__url = "https://tasty.co/"
        self.curRecipe = None

    def __checkSite(self, url):
        """
        Helper method to check if the site can be scraped
        URL: URL to scrape from
        Return: html of the webpage
        """
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None

    def __buildUrl(self, path, user_input):
        """
        Helper method to build the url depending on the path
        path: path from the base url
        user_input: value given by user to redirect
        Return: URL for search or recipe
        """
        if path == "search":
            return f"{self.__url}search?q={user_input}&sort=popular"
        elif path == "recipe":
            return f"{self.__url}{user_input}"
        else:
            return None

    def Scrape(self, user_input):
        """
        Scrapes the url (https://tasty.co) for recipes based on user_input and binds it to self.curRecipe
        user_input: the ingredient the user wants to search for
        Returns: unbinded Recipe properties
        """
        search_url = self.__buildUrl("search", user_input)
        
        soup = BeautifulSoup(self.__checkSite(search_url), 'html.parser')
       

        search_results_div = soup.find('div', id='search-results-feed')

        if search_results_div:
            
            first_a_tag = search_results_div.find('a')

            if first_a_tag:
                recipe_url = self.__buildUrl("recipe", first_a_tag.get('href'))

                soup = BeautifulSoup(self.__checkSite(recipe_url), 'html.parser')
                
                #GETTING TITLE
                recipe_title = soup.find('h1', class_='recipe-name extra-bold xs-mb05 md-mb1').text
                #==============================================================================================
                

                #GETTING INGREDIENTS
                ingredients_section = soup.find('div', class_='ingredients__section')
                recipe_ingredients = []
                ingredient_items = ingredients_section.find_all('li', class_='ingredient')

                for item in ingredient_items:
                    ingredient_text = ' '.join(item.stripped_strings)
                    recipe_ingredients.append(ingredient_text)

                #==============================================================================================
                
                
                #GETTING INSTRUCTIONS
                instructions_list = soup.find('ol', class_='prep-steps')
                recipe_instructions = []
                instruction_items = instructions_list.find_all('li')
                for i, item in enumerate(instruction_items, start=1):
                    instruction_text = item.get_text(strip=True)
                    recipe_instructions.append(f"Step {i}: {instruction_text}")
                #==============================================================================================
                
                                
                #GETTING COOK TIME
                # cooktimes = soup.find('div', class_="desktop-cooktimes xs-hide xs-pb05 md-block lg-mb2")
                # if cooktimes:
                #     time_elements = cooktimes.find_all("p", class_="xs-text-4 md-hide")
                #     last_two_times = [time.text for time in time_elements[-2:]]
                #     time_integers = [int(time.split()[0]) for time in last_two_times]
                #     prep_time = time_integers[0]
                #     cook_time = time_integers[1]
                #==============================================================================================

                #GETTING SERVINGS
                servings_text = soup.find("p", class_="servings-display xs-text-2 xs-mb2").text
                tokens = servings_text.split()
                if len(tokens) >= 2:
                    servings = int(tokens[1])

                #==============================================================================================

            else:
                print("No 'a' tags found within the specified 'div'.")
        else:
            print("No 'div' with id 'search-results-feed' found.")
        
        self.curRecipe = Recipe(
            title=recipe_title,
            ingredients=recipe_ingredients,
            instructions=recipe_instructions,
            # prep_time=prep_time,
            # cook_time=cook_time,
            servings=servings,
        )
        
        return self.curRecipe

    def Package(self):
        """
        Binds self.curRecipe to json format
        Returns: self.curRecipe as JSON jump
        """
        if self.curRecipe is not None:
            recipe_data = {
                "title": self.curRecipe.title,
                "ingredients": self.curRecipe.ingredients,
                "instructions": self.curRecipe.instructions,
                "servings": self.curRecipe.servings,
            }

            return json.dumps(recipe_data, ensure_ascii=False, indent=4)
        else:
            return None


if __name__ == '__main__':
    ws = WebScrape()
    ws.Scrape("waffles")
    print(ws.curRecipe)
    print(ws.curRecipe.title)
    # print(ws.curRecipe.cook_time)
    # print(ws.curRecipe.prep_time)
    print(ws.curRecipe.servings)
    print(ws.curRecipe.ingredients)
    print(ws.curRecipe.instructions)