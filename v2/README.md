# SE-project1

# Web Scrape Package
## Data source
https://tasty.co

## Usage
```
import webscrape
ws = WebScrape()    #initialize class
ws.Scrape("FOOD", recipe_number)   #scrape for desired food item default number = 1
ws.package()        #package as json (optional)
```

## Accessing recipe properties
```
title = ws.curRecipe.title
servings = ws.curRecipe.servings
ingredients = ws.curRecipe.ingredients
instructions = ws.curRecipe.instructions
``````

## Package as JSON
```
recipe_json = ws.package()
``````

## Saving JSON data to a file
```
with open("recipe_data.json", "w") as json_file:
    json_file.write(recipe_json)
```    

## Sample JSON data
```
{
    "title": "The Ultimate Waffle",
    "ingredients": [
        "2 cups all purpose flour ( 250 g )",
        "2 teaspoons baking powder",
        "1 teaspoon kosher salt",
        "1 cup whole milk ( 240 mL )",
        "½ cup buttermilk ( 120 mL )",
        "4 tablespoons unsalted butter , melted and cooled",
        "½ teaspoon vanilla extract",
        "2 large eggs , separated",
        "⅓ cup sugar ( 65 g )",
        "nonstick cooking spray , for greasing",
        "butter , for serving",
        "maple syrup , for serving"
    ],
    "instructions": [
        "Step 1: Preheat a waffle iron to medium-high.",
        "Step 2: In a large bowl, whisk together the flour, baking powder, and salt. Make a well in the center and pour in the milk, buttermilk, melted butter, vanilla, and egg yolks. Whisk until the batter just comes together (there will be some lumps).",
        "Step 3: Add the egg whites to a medium bowl and beat with an electric hand mixer until foamy. With the mixer running, gradually add the sugar and continue beating until stiff peaks form. Gently fold the egg whites into the batter until just combined.",
        "Step 4: Spray the heated waffle iron with nonstick cooking spray. Ladle the batter into the waffle iron, close the lid, and cook according to manufacturer’s instructions until the waffle is golden brown and crisp, 5–6 minutes. Transfer the waffle to a plate and repeat with the remaining batter.",
        "Step 5: Serve the waffles hot, with butter and maple syrup alongside.",
        "Step 6: Enjoy!",
        "Step 7: Meal planning made easy with the Tasty app.Download nowto see exclusive curated meal plans."
    ],
    "servings": 4
}
```