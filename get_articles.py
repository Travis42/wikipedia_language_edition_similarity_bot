#!python3
"""
Gets articles from Wikipedia.
"""

import pywikibot

editions = {
            'en' : 'English', 
            'fr' : 'French', 
            'de' : 'German',
            'es' : 'Spanish', 
            'ja' : 'Japanese', 
            'ru' : 'Russian', 
            'it' : 'Italian', 
            'zh' : 'Chinese', 
            'pt' : 'Portuguese', 
            'ar' : 'Arabic',
            'pl' : 'Polish',
            'fa' : 'Persian', 
            'nl' : 'Dutch', 
            'id' : 'Indonesian', 
            'uk' : 'Ukranian', 
            'sv' : 'Swedish', 
            'cs' : 'Czech',
            'ko' : 'Korean',
            'vi' : 'Vietnamese', 
            'hu' : 'Hungarian', 
            'fi': 'Finnish', 
            'ca' : 'Catalan', 
            'no' : 'Norwegian', 
            'hi' : 'Hindi', 
            'th' : 'Thai'
            }

site = pywikibot.Site()
page = pywikibot.Page(site, u"Hot spring")
engtext = page.text
engtitle = page.title()



#' How to get the equivalent name in a different language:
edition_links = [link for link in page.langlinks()]


site = edition_links[0].site
title = edition_links[0].title
page = pywikibot.Page(site, title)



'''
# attempt to search for new areas to pull:
from pywikibot import pagegenerators
for page in pagegenerators(pages, 100):
    print(pagegenerators.InterwikiPageGenerator(page))


see https://github.com/wikimedia/pywikibot/blob/eec2ff54b16cbe92700fb63ea8349c4a80272236/pywikibot/pagegenerators.py
"""
