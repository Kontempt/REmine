'''
Holds functions and modules to be utilised across the re-mine project
'''
import resource
import re

def tree_parse(src, tree, source):
    '''Goes over returned webpage & extracts article titles and corresponding url links'''
    try:
        title = tree.xpath(source[0][0])
        link = tree.xpath(source[0][1])
        if len(source[0]) == 4:
            '''adds main article and link in cases where xpath vals
                different between the main article  and other articles'''
            title[0] = tree.xpath(source[0][2])[0]
            link[0] = tree.xpath(source[0][3])[0]
        elif len(source[0]) == 6:
            title.insert(0, tree.xpath(source[0][2])[0])
            link.insert(0, tree.xpath(source[0][3])[0])

            title.extend(tree.xpath(source[0][4]))
            link.extend(tree.xpath(source[0][5]))
        else:
            url_link = link
        if src == 0:
            url_link = url_edit_dn(source[1], link)
        else:
            url_link = link
        #TP:
        # print(title)
        # print(url_link)
        return title, url_link
    
    except ValueError:
        print("Some data NOT fetched from website.\ncheck if xpath values are valid.")

def url_edit_dn(start_substr, url):
    '''Checks daily nation urls against substrings and edits accordingly
        Input: start_substring and url
        Output: list of edited urls to include domians where necessary'''
    url_temp = []
    for i, url_link in enumerate(url):
        for  start_substring in start_substr:
            if re.match(start_substring, url_link):
                url_temp.insert(i, url_link)
                break
            else:
                url_join = '/'.join(['http://www.nation.co.ke', url_link])
                url_temp.insert(i, url_join)

    return url_temp[:len(url)]

def filter_title(title, article_url_link):
    ''' Goes over the article titles returned and outputs relevant ones.
        Input: title, article urls
        Output: relevant titles and article urls'''

    title_new = []

    for i, acl_title in enumerate(title):

        weight = 1    #holds the frequency of matches
        results = []    #holds the values of matches made

        if u"\ufffd" in acl_title:
            acl_title = acl_title.replace(u"\ufffd", "\'")

        for  kword in resource.KEYWORD:
            for word in kword:
                re_search = re.search(word, acl_title)
                if re_search:
                    results.append(re_search.group())
                    details = [acl_title, article_url_link[i], i, weight, results]

                    if details in title_new:
                        #Ensure only one instance added to title_new for multiple search returns
                        title_new[title_new.index(details)][3] += 1
                    else:
                        title_new.append(details)

    #TEST POINT: verification of filtered titles
    #print("TP:\n\tRelevant Articles, link, Position , Weight:\n\t", title_new)
    return title_new

def word_analyzer(body):
    '''counts the words in an article to help determine high frequency words'''
    body_temp = []
    for line in body:
        if u"\ufffd" in line:
            line = line.replace(u"\ufffd", "\'")
        body_temp.extend(line.split(' '))
    # print("TP:\n\t", body_temp)
    # print("TP:word count\n\t", len(body_temp))
    return body_temp
