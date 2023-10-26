from webscrape import WebScrape

ws = WebScrape()
result = ws.Scrape("chicken")
print(ws.curRecipe.title)