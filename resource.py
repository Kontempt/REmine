'''Manages major lists and dictionaries used across remine project
    New information sources added here'''

GENERAL = [
    r'real estate', r'housing', r'land', r'mortgage',
    r'project', r'funding', r'buildings', r'mall',
    r'mixed use development'
    ]
FIRMS = [
    r'Cytonn', r'Hassconsult', r'Knight Frank', r'Centum',
    r'PRC', r'Housing Finance', r'Ministry of Land, Housing and Urban Development',
    r'Pam Golding', r'National Housing Corporation',
    ]
KEYWORD = [GENERAL, FIRMS]
#Various 'categories' (eg. GENERAL, FIRM)added to search parameters separately for future
    #...ease when dealing with large sets of KEYWORDs

#DETAILS LIST holds the following:
    # main url [0]
    # list of title and link xpath vals[1]
    # list of link start substrings[2]
    # prefix substring[3]
    # author xpath[4]
    # list of body xpath vals[5]
    # Aricle source[6]
    #time xpath[7]
DN_DETAILS = [
    'http://www.nation.co.ke/business/996-996-x0uutpz/index.html',
    [
        '//div["class=story-teaser"]/h3/a/text()', '//div["class=story-teaser"]/h3/a/@href',
        '//div["class=story-teaser"]/h2/a/text()', '//div["class=story-teaser"]/h2/a/@href'],
    [
        r'http://www.nation.co.ke',
        r'http://www.businessdailyafrica.com'
    ],
    'http://www.nation.co.ke',
    '//section["class=author"]/strong/text()',
    ['//section["class=body-copy"]/div/p/text()'],
    'Daily Nation',
    ''
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
    [r'https://www.standardmedia.co.ke'],
    'https://www.standardmedia.co.ke',
    '//div["class=col-xs-8"]/span["class=date"]/a/text()',
    ['//div["class=main-article"]/p/text()'],
    'The Standard',
    ''
]

EA_DETAILS = [
    'http://www.theeastafrican.co.ke/business/2560-2560-gsk11bz/index.html',
    [
        '//div["class=story-teaser medium-teaser"]/h3/a/text()',
        '//div["class=story-teaser medium-teaserl"]/h3/a/@href',
        '//div["class=story-teaser top-teaser"]/h2/a/text()',
        '//div["class=story-teaser top-teaser"]/h2/a/@href',
    ],
    [
        r'http://www.theeastafrican.co.ke',
    ],
    'http://www.theeastafrican.co.ke',
    '//section["class=author noprint"]/strong/text()',
    ['//section["class=body-copy"]/div/p/text()'],
    'The East African',
    ''
]

BK_DETAILS = [
    'https://biznakenya.com/real-estate/',
    [
        '//*[@id="td-outer-wrap"]/div[4]/div/div/div[1]/div/div/div["class=td-block-span6"]/div/h3/a/@title',
        '//*[@id="td-outer-wrap"]/div[4]/div/div/div[1]/div/div/div["class=td-block-span6"]/div/h3/a/@href',
        '//*[@id="td_uid_23_5a3be03929a08"]/div[1]/div[1]/div[1]/a/@title',
        '//*[@id="td_uid_23_5a3be03929a08"]/div[1]/div[1]/div[1]/a/@href',
        '//div[@id="td_uid_23_5a3be03929a08"]/div/div/div["class=td-module-mx5"]/div["class=td-module-thumb"]/a/@title',
        '//div[@id="td_uid_23_5a3be03929a08"]/div/div/div["class=td-module-mx5"]/div["class=td-module-thumb"]/a/@href'
    ],
    [r'https://biznakenya.com'],
    'https://biznakenya.com',
    '//header["class=td-post-title"]/div/div/a/text()',
    ['//div["class=td-post-content"]/div/p/text()'],
    'Bizna Kenya',
    ''
]

TS_DETAILS = [
    'https://www.the-star.co.ke/sections/business_c29663',
    [
        '//div["class=ds-main"]/div/h1/a/text()',
        '//div["class=ds-main"]/div/h1/a/@href',
        '/div["class=pane-content"]/div/article/footer/div[1]/h1/a/text()',
        '/div["class=pane-content"]/div/article/footer/div[1]/h1/a/@href',
    ],
    [r'https://www.the-star.co.ke'],
    'https://www.the-star.co.ke',
    '/html/body/div[1]/div[6]/div/div[2]/div/div[2]/div/div/div/div/text()',
    ['//div["class=field-name-body"]/p/text()'],
    'The Star',
    '/html/body/div[1]/div[6]/div/div[2]/div/div[1]/div/div/div/div/time/text()'
]

CF_DETAILS = [
    'https://www.capitalfm.co.ke/news/section/kenya/',
    [
        '//div["class=entry-information"]/header/h2/a/text()',
        '//div["class=entry-information"]/header/h2/a/@href',
    ],
    [r'https://www.capitalfm.co.ke'],
    'https://www.capitalfm.co.ke',
    '//span["class=author-byline"]/a/text()',
    [
        '//div["class=entry-content"]/p/strong/text()',
        '//div["class=entry-content"]/p/text()'
    ],
    'CapitalFM News',
    '//header["class=entry-header"]/h5/text()'
]

KW_DETAILS = [
    'http://kenyanwallstreet.com/category/kenyan-news',
    [
        '//header["class=mh-posts-list-header"]/h3/a/@title',
        '//header["class=mh-posts-list-header"]/h3/a/@href',
    ],
    [r'http://kenyanwallstreet.com'],
    'http://kenyanwallstreet.com',
    '//*[@id="post-16572"]/header/p/span[2]/a/text()',
    ['//article/div["class=entry-content clearfix"]/p/text()'],
    'The Kenyan Wallstreet',
    '//*[@id="post-16572"]/header/p/span[1]/a/text()',
]

#SOURCE holds details(eg. xpath val.s, main url...) for all the news/info sources
SOURCE = {0:DN_DETAILS, 1:SD_DETAILS, 2:EA_DETAILS, 3:BK_DETAILS,
          4:TS_DETAILS, 5:CF_DETAILS, 6:KW_DETAILS}

#TODO: FOR ArticleRE add datetime for all sources. Last item in DETaILS list
