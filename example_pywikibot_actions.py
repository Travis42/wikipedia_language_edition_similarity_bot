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


###################

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
An incomplete sample script.

This is not a complete bot; rather, it is a template from which simple
bots can be made. You can rename it to mybot.py, then edit it in
whatever way you want.

Use global -simulate option for test purposes. No changes to live wiki
will be done.


The following parameters are supported:

-always           The bot won't ask for confirmation when putting a page

-text:            Use this text to be added; otherwise 'Test' is used

-replace:         Don't add text but replace it

-top              Place additional text on top of the page

-summary:         Set the action summary message for the edit.


The following generators and filters are supported:

&params;
"""
#
# (C) Pywikibot team, 2006-2019
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

import pywikibot
from pywikibot import pagegenerators

from pywikibot.bot import (
    SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)

# This is required for the text that is shown when you run this script
# with the parameter -help.
docuReplacements = {'&params;': pagegenerators.parameterHelp}  # noqa: N816


class BasicBot(
    # Refer pywikobot.bot for generic bot classes
    SingleSiteBot,  # A bot only working on one site
    # CurrentPageBot,  # Sets 'current_page'. Process it in treat_page method.
    #                  # Not needed here because we have subclasses
    ExistingPageBot,  # CurrentPageBot which only treats existing pages
    NoRedirectPageBot,  # CurrentPageBot which only treats non-redirects
    AutomaticTWSummaryBot,  # Automatically defines summary; needs summary_key
):

    """
    An incomplete sample bot.

    @ivar summary_key: Edit summary message key. The message that should be
        used is placed on /i18n subdirectory. The file containing these
        messages should have the same name as the caller script (i.e. basic.py
        in this case). Use summary_key to set a default edit summary message.

    @type summary_key: str
    """

    summary_key = 'basic-changing'

    def __init__(self, generator, **kwargs):
        """
        Initializer.

        @param generator: the page generator that determines on which pages
            to work
        @type generator: generator
        """
        # Add your own options to the bot and set their defaults
        # -always option is predefined by BaseBot class
        self.availableOptions.update({
            'replace': False,  # delete old text and write the new text
            'summary': None,  # your own bot summary
            'text': 'Test',  # add this text from option. 'Test' is default
            'top': False,  # append text on top of the page
        })

        # call initializer of the super class
        super(BasicBot, self).__init__(site=True, **kwargs)

        # assign the generator to the bot
        self.generator = generator

    def treat_page(self):
        """Load the given page, do some changes, and save it."""
        text = self.current_page.text

        ################################################################
        # NOTE: Here you can modify the text in whatever way you want. #
        ################################################################

        # If you find out that you do not want to edit this page, just return.
        # Example: This puts Text on a page.

        # Retrieve your private option
        # Use your own text or use the default 'Test'
        text_to_add = self.getOption('text')

        if self.getOption('replace'):
            # replace the page text
            text = text_to_add

        elif self.getOption('top'):
            # put text on top
            text = text_to_add + text

        else:
            # put text on bottom
            text += text_to_add

        # if summary option is None, it takes the default i18n summary from
        # i18n subdirectory with summary_key as summary key.
        self.put_current(text, summary=self.getOption('summary'))


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: str
    """
    options = {}
    # Process global arguments to determine desired site
    local_args = pywikibot.handle_args(args)

    # This factory is responsible for processing command line arguments
    # that are also used by other scripts and that determine on which pages
    # to work on.
    gen_factory = pagegenerators.GeneratorFactory()

    # Parse command line arguments
    for arg in local_args:

        # Catch the pagegenerators options
        if gen_factory.handleArg(arg):
            continue  # nothing to do here

        # Now pick up your own options
        arg, sep, value = arg.partition(':')
        option = arg[1:]
        if option in ('summary', 'text'):
            if not value:
                pywikibot.input('Please enter a value for ' + arg)
            options[option] = value
        # take the remaining options as booleans.
        # You will get a hint if they aren't pre-defined in your bot class
        else:
            options[option] = True

    # The preloading option is responsible for downloading multiple
    # pages from the wiki simultaneously.
    gen = gen_factory.getCombinedGenerator(preload=True)
    if gen:
        # pass generator and private options to the bot
        bot = BasicBot(gen, **options)
        bot.run()  # guess what it does
        return True
    else:
        pywikibot.bot.suggest_help(missing_generator=True)
        return False


if __name__ == '__main__':
    main()
