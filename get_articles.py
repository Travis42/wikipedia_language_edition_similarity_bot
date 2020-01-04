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



#' How to get the equivalent name in a different language automatically:
# This takes a long time!
#edition_links = [link for link in page.iterlanglinks()]
# format: pywikibot.page.Link('Onsen', APISite("az", "wikipedia"))
# this takes less time!  What's the diff?  (NO DIFFERENCE IN OUTPUT)
edition_links = [link for link in page.langlinks()]


site = edition_links[0].site
title = edition_links[0].title
page = 



site_jp = pywikibot.Site('ja')
page_jp = pywikibot.Page(site, u"熱水泉")
page_jp = pywikibot.Page(site_jp, u"熱水泉")
text_jp = page_jp.text
text_jp

results = [i for i in page.interwiki()] # it gives you all the other language reference links in the page...not the equivalent page in the other languages.


# attempt to get other lang pages:
from pywikibot import pagegenerators
for page in pagegenerators(pages, 100):
    print(pagegenerators.InterwikiPageGenerator(page))


see https://github.com/wikimedia/pywikibot/blob/eec2ff54b16cbe92700fb63ea8349c4a80272236/pywikibot/pagegenerators.py
"""
