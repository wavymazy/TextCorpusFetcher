import logging

import pywikibot
from pywikibot import pagegenerators
import asyncio
import os
import argparse
import sys
from tqdm import tqdm

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def parse_args(args):

    arg_parser = argparse.ArgumentParser('Arguments for fetching wikipedia articles')
    # if no category is given, will default to searching for "wikipedia" as a category, with a depth of 1 and limit of
    # 1 (1 article)
    arg_parser.add_argument('-c', '--category', nargs='?', metavar='category', help='Category of articles',
                            required=False, default="wikipedia")
    arg_parser.add_argument('-d', '--depth', nargs='?', metavar='depth', help='Depth of article tree created',
                            required=False, default=1)
    arg_parser.add_argument('-t', '--total', nargs='?', metavar='total', help='Limit number of articles',
                            required=False, default=1)
    arg_parser.add_argument('-o', '--output_path', nargs='?', metavar='output_path', help='Path of output folder',
                            required=False, default="data/")

    return arg_parser.parse_args(args)


async def write_to_file(text, category_name,  idx, output_path):
    """Writes article to file.

    Parameters
    ----------
    text : str
        article content
    category_name: str
        Name of the category
    idx: int
        Index of the article
    output_path: str
        Output folder
    """

    folder_name = output_path + category_name
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(folder_name + "/wiki_article_" + category_name + "_" + str(idx) + ".txt", "w") as f:
        f.write(text)
        f.close()


async def download_category(category, search_depth, limit_number_of_articles, output_path):
    """Creates an article generator based on a specific category and iterates over it to write article.

    Parameters
    ----------
    category : Category
        Name of the category
    search_depth: int
        Depth of search
    limit_number_of_articles: int
        Limits the number of total articles
    output_path: str
        Output folder
    """

    logger.info("Downloading: " + category.title())
    category_title = category.title().replace(":", "_")
    generated_pages = pagegenerators.CategorizedPageGenerator(category, recurse=search_depth,
                                                              total=limit_number_of_articles)
    article_idx = 1
    for page in tqdm(generated_pages):
        text = page.text
        await write_to_file(text, category_title, article_idx, output_path)
        article_idx = article_idx+1


async def fetch_articles(category_name, search_depth, limit_number_of_articles, output_path):
    """Fetches articles and saves them to an output folder.

    Parameters
    ----------
    category_name : str
        Name of the category
    search_depth: int
        Depth of search
    limit_number_of_articles: int
        Limits the number of total articles
    output_path: str
        Output folder
    """

    site = pywikibot.Site()
    category = pywikibot.Category(site, 'Category:' + category_name)
    await download_category(category, search_depth, limit_number_of_articles, output_path)

if __name__ == '__main__':
    # Script args
    args = parse_args(sys.argv[1:])
    cat_name = args.category
    search_depth = args.depth
    limit_number_of_articles = args.total
    output_path = args.output_path
    # Async execution
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_articles(cat_name, search_depth, limit_number_of_articles, output_path))

