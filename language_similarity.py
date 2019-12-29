#!python3

import pywikibot as wiki
site = wiki.Site('en', 'wikipedia') # The site we want to run our bot on
page = wiki.Page(site, 'Wikipedia:Sandbox')
page.text = page.text.replace('foo', 'bar')
page.save('Replacing "foo" with "bar"') # Saves the page

#############another example, shows how to access different language versions.

import pwb  # only needed if you haven't installed the framework as side-package
import pywikibot
site = pywikibot.Site('en', 'wikipedia')  # any site will work, this is just an example
page = pywikibot.Page(site, 'Douglas Adams')
item = pywikibot.ItemPage.fromPage(page)  # this can be used for any page object
# you can also define an item like this
repo = site.data_repository()  # this is a DataSite object
item = pywikibot.ItemPage(repo, 'Q42')  # This will be functionally the same as the other item we defined
item.get()  # you need to call it to access any data.
sitelinks = item.sitelinks
aliases = item.aliases
if 'en' in item.labels:
    print('The label in English is: ' + item.labels['en'])
if item.claims:
    if 'P31' in item.claims: # instance of
        print(item.claims['P31'][0].getTarget())
        print(item.claims['P31'][0].sources[0])  # let's just assume it has sources.

# Edit an existing item
item.editLabels(labels={'en': 'Douglas Adams'}, summary=u'Edit label')
item.editDescriptions(descriptions={'en': 'English writer'}, summary=u'Edit description')
item.editAliases(aliases={'en':['Douglas Noel Adams', 'another alias']})
item.setSitelink(sitelink={'site': 'enwiki', 'title': 'Douglas Adams'}, summary=u'Set sitelink')
item.removeSitelink(site='enwiki', summary=u'Remove sitelink')

# You can also made this all in one time:
data = {'labels': {'en': 'Douglas Adams'},
  'descriptions': {'en': 'English writer'},
       'aliases': {'en': ['Douglas Noel Adams', 'another alias'], 'de': ['Douglas Noel Adams']},
     'sitelinks': [{'site': 'enwiki', 'title': 'Douglas Adams'}]}
item.editEntity(data, summary=u'Edit item')