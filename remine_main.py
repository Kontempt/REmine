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

        article_details = []
        article_details.append([article_author[0], article_body])
        #TP:
        # print(article_author)
        # print(retools.word_analyzer(article_body))
        # print(articles_details_all)
    return article_details

def content_get(src):
    '''Main function that starts up the remine project'''

    source = resource.SOURCE[src]
    try:
        page = requests.get(source[0])
        tree = html.fromstring(page.content)

        title, urllink = retools.tree_parse(src, tree, source[1:3])

        new_details = retools.filter_title(title, urllink)
        print("TP:\nSOURCE:\n\t", source[5])
        # holds list of relevant articles
        print("NEW DETAILS:\n\t ", new_details)
        
        if new_details:
            article_details_all = indv_content_get(source[3:5], new_details)
        else:
            print("NO relevant articles found")

    except requests.exceptions.HTTPError:
        print("Page not accessed")

    except requests.exceptions.ConnectionError:
        print("Unable to connect due to NETWORK ERROR.")

for key in resource.SOURCE:
    content_get(key)

