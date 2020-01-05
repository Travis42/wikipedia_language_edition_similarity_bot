#!python3
"""
Gets articles from Wikipedia.

see https://github.com/wikimedia/pywikibot/blob/eec2ff54b16cbe92700fb63ea8349c4a80272236/pywikibot/pagegenerators.py
"""
from translate import translate
from utils import write_string_to_txt_file

from pywikibot import Page, pagegenerators, Site

# Deleting some in the name of maximizing cultural difference capture in relation to English.
langs = {
#            'en' : 'English', 
#            'fr' : 'French', 
#            'de' : 'German',
            'es' : 'Spanish', 
            'ja' : 'Japanese', 
            'ru' : 'Russian', 
#            'it' : 'Italian', 
            'zh' : 'Chinese', 
#            'pt' : 'Portuguese', 
            'ar' : 'Arabic',
#            'pl' : 'Polish',
            'fa' : 'Persian', 
#            'nl' : 'Dutch', 
            'id' : 'Indonesian', 
            'uk' : 'Ukranian', 
#            'sv' : 'Swedish', 
#            'cs' : 'Czech',
            'ko' : 'Korean',
            'vi' : 'Vietnamese', 
            'hu' : 'Hungarian', 
#            'fi': 'Finnish', 
#            'ca' : 'Catalan', 
#            'no' : 'Norwegian', 
            'hi' : 'Hindi', 
#            'th' : 'Thai'
            }

def get_topic_articles(page):
    # construct the memory datastore:
    topic = {}
    topic['title'] = page.title()
    # I don't want no stubs
    if len(page.text) < 500:
        return
    topic['content'] = page.text
    edition_links = [link for link in pagegenerators.LanguageLinksPageGenerator(page)]
    if edition_links == []:
        return
    topic['language'] = {}
    for link in edition_links:
        lang_code = str(link.site)[-2:]
        if lang_code in langs.keys():
            # I don't want no stubs
            if len(link.text) < 500:
                continue
            page = Page(link)
            topic['language'][lang_code] = {
                                    'title': page.title(),
                                    'orig_content': page.text,
                                    'translated_content': translate(page.text)
                                    }
    if topic['language'] == {}:
        return
    return topic

def move_to_random_topic():
    # starting site
    site = Site()
    #page = pywikibot.Page(site, u"Whatever")
    return Page(next(pagegenerators.RandomRedirectPageGenerator(1)))


def move_through_topic(starting_topic='History'):
    # starting site
    site = Site()
    starting_page = Page(site, starting_topic)
    return (i for i in pagegenerators.LinkedPageGenerator(starting_page))


# notes
'''
Get all other topics in the given topic:
for link in pagegenerators.LinkedPageGenerator(starting_page):
'''
