# SE-project1

# Web Scrape Package
## Data source
https://tasty.co

## Usage
```
import webscrape
ws = WebScrape()    #initialize class
ws.Scrape("FOOD")   #scrape for desired food item
```

## Accessing recipe properties
```
title = ws.curRecipe.title
servings = ws.curRecipe.servings
ingredients = ws.curRecipe.ingredients
instructions = ws.curRecipe.instructions
``````