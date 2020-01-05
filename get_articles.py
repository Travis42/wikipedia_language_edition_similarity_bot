#!python3
"""
Gets articles from Wikipedia.
"""
from translate import translate

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

#############

def get_articles():
    # starting site
    site = pywikibot.Site()
    page = pywikibot.Page(site, u"Hot spring")

    # Getting the equivalent topic in different languages (editions):
    edition_links = [link for link in page.langlinks()]

    # construct the memory datastore:
    topic = {}
    topic['title'] = page.title()
    topic['content'] = page.text
    topic['language'] = {}
    for link in edition_links:
        lang_code = str(link.site)[-2:]
        if lang_code in editions.keys(): 
            page = pywikibot.Page(link)
            topic['language'][lang_code] = {
                                'title': page.title(),
                                'orig_content': page.text,
                                'translated_content': translate(page.text)
                                    }
    return topic


'''
page = pywikibot.Page(edition_links[0]) # works

site = edition_links[0].site
title = edition_links[0].title
page = pywikibot.Page(site, title) # this also works

# to extract the lang:
str(page.site) # or editionlinks[0].site

pywikibot.site.APISite

# attempt to search for new areas to pull:
from pywikibot import pagegenerators
for page in pagegenerators(pages, 100):
    print(pagegenerators.InterwikiPageGenerator(page))


see https://github.com/wikimedia/pywikibot/blob/eec2ff54b16cbe92700fb63ea8349c4a80272236/pywikibot/pagegenerators.py
'''
