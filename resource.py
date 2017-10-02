'''Manages major lists and dictionaries used across remine project
    New information sources added here'''

GENERAL = [r'real estate', r'housing', r'land', r'mortgage', r'project', r'funding', r'buildings', r'mall']
FIRMS = [r'Cytonn', r'Hassconsult', r'Knight Frank', r'Centum']
KEYWORD = [GENERAL, FIRMS]
#Various 'categories' (eg. GENERAL, FIRM)added to search parameters separately for future
    #...ease when dealing with large sets of KEYWORDs

#DETAILS LIST holds the following:
    # main url [0]
    # list of title and link xpath vals[1]
    # list of link start substrings[2]
    # author xpath[3]
    # body xpath[4]
DN_DETAILS = [
    'http://www.nation.co.ke/business/996-996-x0uutpz/index.html',
    [
        '//div["class=story-teaser"]/h3/a/text()', '//div["class=story-teaser"]/h3/a/@href',
        '//div["class=story-teaser"]/h2/a/text()', '//div["class=story-teaser"]/h2/a/@href'],
    [
        r'http://www.nation.co.ke',
        r'http://www.businessdailyafrica.com'],
    "//section['class=author']/strong/text()",
    '//section["class=body-copy"]/div/p/text()'
]

#SOURCE holds details(eg. xpath val.s, main url...) for all the news/info sources
SOURCE = {0:DN_DETAILS}
