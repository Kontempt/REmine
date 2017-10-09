'''Manages major lists and dictionaries used across remine project
    New information sources added here'''

GENERAL = [r'real estate', r'housing', r'land', r'mortgage', r'project', r'funding', r'buildings', r'mall']
FIRMS = [r'Cytonn', r'Hassconsult', r'Knight Frank', r'Centum']
KEYWORD = [GENERAL, FIRMS]
# Various 'categories' (eg. GENERAL, FIRM)added to search parameters separately for future
# ...ease when dealing with large sets of KEYWORDs

#DETAILS LIST holds the following:
    # main url [0]
    # list of title and link xpath vals[1]
    # list of link start substrings[2]
    # author xpath[3]
    # body xpath[4]
    # article source[5]
DN_DETAILS = [
    'http://www.nation.co.ke/business/996-996-x0uutpz/index.html',
    [
        '//div["class=story-teaser"]/h3/a/text()', '//div["class=story-teaser"]/h3/a/@href',
        '//div["class=story-teaser"]/h2/a/text()', '//div["class=story-teaser"]/h2/a/@href'],
    [
        r'http://www.nation.co.ke',
        r'http://www.businessdailyafrica.com'],
    "//section['class=author']/strong/text()",
    '//section["class=body-copy"]/div/p/text()',
    'Daily Nation'
]

SD_DETAILS = [
    'https://www.standardmedia.co.ke/business/category/46/home-away',
    [
        '//li/div["class=col-xs-6"]/h4/a/text()',
        '//li/div["class=col-xs-6"]/h4/a/@href',
        '//div["class=cat-faded-txtr"]/h3/text()',
        '/html/body/div[5]/div[2]/a/@href',
        '/html/body/div[5]/div[4]/div[1]/div["class=col-xs-4"]/h4/a/text()',
        '/html/body/div[5]/div[4]/div[1]/div["class=col-xs-4"]/h4/a/@href'
    ],
    [],
    '//div["class=col-xs-8"]/span["class=date"]/a/text()',
    '//div["class=main-article"]/p/text()',
    'The Standard'
]

#SOURCE holds details(eg. xpath val.s, main url...) for all the news/info sources
SOURCE = {0:DN_DETAILS}
