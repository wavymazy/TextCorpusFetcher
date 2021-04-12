import os
import pytest
import pywikibot
from CorpusFetcher.main import fetch_articles, write_to_file, download_category


@pytest.mark.asyncio
async def test_write_to_file():

    content = "this is a test"
    category_name = "test_category"
    idx = 1
    output_path = "tests/data/"
    await write_to_file(content, category_name,  idx, output_path)
    expected_result_path = "tests/data/test_category/wiki_article_test_category_1.txt"
    assert os.path.exists(expected_result_path)


@pytest.mark.asyncio
async def test_download_category():

    site = pywikibot.Site()
    category_name = "test_category"
    category = pywikibot.Category(site, 'Category:' + category_name)
    search_depth = 1
    limit_number_of_articles = 1
    output_path = "tests/data/"
    await download_category(category, search_depth, limit_number_of_articles, output_path)
    expected_result_path = "tests/data/test_category/wiki_article_test_category_1.txt"
    assert os.path.exists(expected_result_path)
