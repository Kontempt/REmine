'''Main remine module from which functions accessed'''

import resource
import retools
from lxml import html
import requests

def indv_content_get(article_info, new_details):
    '''Gets individual content for each of the relevant/filtered articles'''
    for detail in new_details:
        page = requests.get(detail[1])  #fetches article webpage
        tree = html.fromstring(page.content)

        article_author = tree.xpath(article_info[0])
        article_body = tree.xpath(article_info[1])
        print(article_author)
        print(retools.word_analyzer(article_body))

def content_get(src):
    '''Main function that starts up the remine project'''

    source = resource.SOURCE[src]
    try:
        page = requests.get(source[0])
        tree = html.fromstring(page.content)

        title, urllink = retools.tree_parse(src, tree, source[1:3])

        new_details = retools.filter_title(title, urllink)
        # holds litof relevant articles
        print("TP - NEW DETAILS: ", new_details)
        indv_content_get(source[3:5], new_details)

    except requests.exceptions.HTTPError:
        print("Page not accessed")

    except requests.exceptions.ConnectionError:
        print("Unable to connect due to NETWORK ERROR.")

content_get(0)
