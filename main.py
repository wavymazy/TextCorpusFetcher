import pywikibot
from pywikibot import pagegenerators
import asyncio
import os


async def write_to_file(text, category_name,  idx):
    folder_name = "data_" + category_name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(folder_name + "/wiki_article_" + category_name + "_" + str(idx) + ".txt", "w") as f:
        f.write(text)
        f.close


async def download_category(cat, search_depth):
    print("Downloading: " + cat.title())
    cat_name = cat.title()
    cat_name = cat_name.replace(":", "_")
    gen = pagegenerators.CategorizedPageGenerator(cat, recurse=search_depth)
    article_idx=1
    for page in gen:
        # Do something with the page object, for example:
        text = page.text
        await write_to_file(text, cat_name, article_idx)
        article_idx = article_idx+1
        print(article_idx)


async def main():
    site = pywikibot.Site()
    cat_name = "insurance"
    search_depth = 5 # Category Insurance with search_depth=2 yields to 1092 articles
    cat = pywikibot.Category(site, 'Category:' + cat_name)
    await download_category(cat, search_depth)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

