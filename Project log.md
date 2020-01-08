# Project Log
- Pywikibot code lives here for search purposes: https://github.com/wikimedia/pywikibot/


## Next Actions

MUST DO
- do a check on that database to ensure that you're not redoing work...or find a better way to store titles you've processed.

- make a robust way of crawling a list of articles.
    **breadth first search is ideal...the Wikipedia is quite deep, but the meatiest articles seem to be on the surface levels**
        That looks like:  appending generators to a list. Check the type of an object, etc.

- learn to process categories:
    - Categoris are objects under pywikibot
    - pagegenerators.LinkedPageGenerator(starting_page) can contain them, so they must be handled.
    - category.articles() will make a generator, which yields pages (and possibly more categories.)
        - there is a pagegenerators.CategorizedPageGenerator(category, recurse=False, start=None, total=None, content=False, namespaces=None, step=NotImplemented) that steps through these automaticaly.
        - category.articlesList() is a list version (use the generator instead)
    - category.categories() lists subcategories, if any.
    - category.categoryinfo will show a dict: ex.
            - {'size': 34, 'pages': 29, 'files': 0, 'subcats': 5}

This should be enough info to parse the tree.




#### Methods
- Pick an arbitrary start page, grab all the links that reference other wiki pages, and continue.
    - would need a way to make sure that articles aren't being parsed in a loop.
    - would need a store of starting pages so that if it hits a dead end, it can restart

- report crashes, implement logging.

- add tests for critical features (don't lecture me)
    -clue:  take all the asserts and if statements on variables and turn those into tests.






- run a check at the beginning of the program to see progress on my monthly allocation of translation characters.  Halt if nearing the limit.
    - Would be nice if there wer a way of getting the truth from MS.

- learn about and implement Python's logging module
    - incorporate into a daily email, or trigger off of a criteria that checks every hour, whatever.  Cron job.
        - Might also be a neat way to start sending myself texts via twil.io

- Ideally, I want to scrape the most popular sites first, then down.  Protected sites might be not worth doing.

- mess with user-config.py

- Consolidate everything that can be configured, into my own config file, for others to use.
    - create instructions

- Generate a requirements.txt, add instructions for newbs to use that.

- Throw project into Intellij for code cleanup.

- (goal should be to grab as much as possible this month and then allow for edits later)  I don't need to edit for a month or more, and approval will take time. Bot scripts exist in the folder that comes with pywikibot.

- multi-core parallelism.  I have this in another script somewhere.
    - which is another good reason to upload all code to Github...easier to search.


## Open Questions:
*send questions to pywikibot@lists.wikimedia.org*
*API: https://doc.wikimedia.org/pywikibot/master/api_ref/pywikibot.html?*
*IRC Channel: irc://chat.freenode.net:6667/pywikibot*

- Is it possible to do translation with a local model and increase capacity/ not have to pay for a service?



"pywikibot.pagegenerators module

This module offers a wide variety of page generators.

A page generator is an object that is iterable (see http://legacy.python.org/dev/peps/pep-0255/ ) and that yields page objects on which other scripts can then work.

Pagegenerators.py cannot be run as script. For testing purposes listpages.py can be used instead, to print page titles to standard output."


    - I want to start with the most visited pages and work my way down.  Is that possible?


pagegenerators:


*can't figure out what 'category' should be in terms of an object type*
CategorizedPageGenerator(category, recurse=False, start=None, total=None, content=False, namespaces=None, step=NotImplemented)
    Yield all pages in a specific category.
    
    If recurse is True, pages in subcategories are included as well; if
    recurse is an int, only subcategories to that depth will be included
    (e.g., recurse=2 will get pages in subcats and sub-subcats, but will
    not go any further).
    
    If start is a string value, only pages whose sortkey comes after start
    alphabetically are included.
    
    If content is True (default is False), the current page text of each
    retrieved page will be downloaded.

Works:
LanguageLinksPageGenerator(page, total=None, step=NotImplemented)
    Iterate over all interwiki language links on a page.

*this is good.*
LinkedPageGenerator(linkingPage, total=None, content=False, step=NotImplemented)
    Yield all pages linked from a specific page.
    
    See L{pywikibot.page.BasePage.linkedPages} for details.
    
    @param linkingPage: the page that links to the pages we want
    @type linkingPage: L{pywikibot.Page}
    @param total: the total number of pages to iterate
    @type total: int
    @param content: if True, retrieve the current content of each linked page
    @type content: bool
    @return: a generator that yields Page objects of pages linked to
        linkingPage
    @rtype: generator











---


- Even better: (**says its deprecated...either find the new thing or copy the code**) **I could also hack it and 'undeprecate' within pywikibot**
    - https://github.com/wikimedia/pywikibot/blob/7ea6fba1a245024262fb778864d96cb0794336b6/pywikibot/titletranslate.py
    from titletranslate import translate
    translate('page title') # or the url of the site
    - what should come back is a list of titles in other languages.



## Starting via command line

python3 pwb.py login starts the bot up.

python3 pwb.py -lang:xx
Will switch to the language edition of choice.  I should probably have a handler script that uses this method to scrap a bunch of sites, then process another way.


-simulate   Disables writing to the server. Useful for testing and debugging of new code (if given, doesn't do any real changes, but only shows what would have been changed).


### Pay attention to global scripts you can use:
https://www.mediawiki.org/wiki/Manual:Pywikibot/Scripts


## Answered Qs

- How much is an Azure cloud instance per month?  Comparable to DigitalOcean?
    - $15 per month.  DigitalOcean is better.
    - I can use the Azure account for translation services only.
        - https://azure.microsoft.com/en-us/pricing/details/cognitive-services/translator-text-api/
        - for now, choose Pay-as-you-go, S1
            - after this month, do Free.

- sometimes tokens are not getting stored in the db.
    - confirmed that sometimes this is because all words are unique, like when the article is very short (stub)

- How do I iterate through sites?
    - *Answer: pywikibot.Page(site, u"Hot spring")
        results = [i for i in page.iterlanglinks()] # has the goods*


- top langs by active users, descending:
    - English, en
    - French, fr
    - German, de
    - Spanish, es
    - Japanese, ja
    - Russian, ru
    - Italian, it
    - Chinese, zh
    - Portuguese, pt
    - Arabic, ar
    - Polish, pl
    - Persian, fa
    - Dutch, nl
    - Indonesian, id
    - Ukranian, uk
    - Swedish, sv
    - Czech, cs
    - Korean, ko
    - Vietnamese, vi
    - Hungarian, hu
    - Finnish, fi
    - Catalan, ca
    - Norwegian, no
    - Hindi, hi
    - Thai, th
    (all of these are in Microsoft Translator)

- source: https://en.wikipedia.org/wiki/List_of_Wikipedias#Detailed_list


### Some function documentation:

*this is not recommended...there are tons of stub sites on Wikipedia, and this doesn't maximize the program's use of time*
RandomPageGenerator(total=None, site=None, namespaces=None, number='[deprecated name of total]')
    Random page generator.

CategorizedPageGenerator(category, recurse=False, start=None, total=None, content=False, namespaces=None, step=NotImplemented)
    Yield all pages in a specific category.
    
    If recurse is True, pages in subcategories are included as well; if
    recurse is an int, only subcategories to that depth will be included
    (e.g., recurse=2 will get pages in subcats and sub-subcats, but will
    not go any further).
    
    If start is a string value, only pages whose sortkey comes after start
    alphabetically are included.
    
    If content is True (default is False), the current page text of each
    retrieved page will be downloaded.


#### Why use active users as my criteria for choosing a set of languages?  

Because I found a lot of discrepancies in other metrics.  Cebuano has the second highest number of articles outright, but they don't have much depth and aren't edited much, which tells me that total articles might not be the best metric.  Active Users is a metric that tells me that the language edition is being kept up and used, and therefore this study will be useful to more people that way.)
    - Contra:  if the idea is to unlock knowledge bound up in cultural understanding as defined by language, wouldn't I want to use the most obscure languages?
        - the problem here comes from diminishing returns from smaller wikipedias.  For this to work, there needs to be an article on the same topic in each language.
        - There is a larger effort to create new articles in other Wikipedias if an entry exists in one language but not the other.  That effort pushes knowledge to other editions, while my project pulls and consolidates knowledge from wikipedia editions.
            - I must first determine if there is 'fruit to pick' from the top languages.  By proving the concept, I can come back around later and do a study on less prolific Wikipedia editions.

- page object:

'applicable_protections', 'aslink', 'autoFormat', 'backlinks', 'botMayEdit', 'canBeEdited', 'categories', 'change_category', 'clear_cache', 'content_model', 'contributingUsers', 'contributors', 'coordinates', 'create_short_link', 'data_item', 'data_repository', 'defaultsort', 'delete', 'depth', 'editTime', 'embeddedin', 'encoding', 'exists', 'expand_text', 'extlinks', 'fullVersionHistory', 'full_url', 'get', 'getCategoryRedirectTarget', 'getCreator', 'getDeletedRevision', 'getLatestEditors', 'getMovedTarget', 'getOldVersion', 'getRedirectTarget', 'getReferences', 'getRestrictions', 'getTemplates', 'getVersionHistory', 'getVersionHistoryTable', 'image_repository', 'imagelinks', 

'interwiki', (Iterate interwiki links in the page text, excluding language links. ex. hot springs links to a similar site on wikivoyage, commons, and wiktionary.  These are interwikis to Wikipedia).

 'isAutoTitle', 'isCategory', 'isCategoryRedirect', 'isDisambig', 'isEmpty', 'isFlowPage', 'isImage', 'isIpEdit', 'isRedirectPage', 'isStaticRedirect', 'isTalkPage', 'is_categorypage', 'is_filepage', 'is_flow_page', 'iterlanglinks', 'itertemplates', 

 'langlinks', *(gives all links to this article in other languages)*

  'lastNonBotUser', 'latestRevision', 'latest_revision', 'latest_revision_id', 

  'linkedPages', *iterates pages that this page links to*

  'loadDeletedRevisions', 'markDeletedRevision', 'merge_history', 'move', 'moved_target', 'namespace', 'oldest_revision', 'pageAPInfo', 'page_image', 'pageid', 'permalink', 'preloadText', 'previousRevision', 'previous_revision_id', 'properties', 'protect', 'protection', 'purge', 'put', 'put_async', 'raw_extracted_templates', 'revision_count', 'revisions', 'save', 'section', 'sectionFreeTitle', 'set_redirect_target', 'site', 'templates', 'templatesWithParams', 

  'text',  *gives the content*

  'title()', gives the title

  'titleForFilename', 'titleWithoutNamespace', 'toggleTalkPage', 'touch', 'undelete', 'urlname', 'userName', 'version', 'watch']


## Structure
- I have pywikibot installed in the projects directory.  This seems to be the way to use it rather than to pip install.

- my wikiscripts dir is where I'm making my own stuff.

## Setup
- python3 generate_user_files.py
    - your login
    - name of bot
    - generate a password for the bot, as well as permissions according to https://www.mediawiki.org/wiki/Manual:Pywikibot/BotPasswords
    - **there are more things to configure in user_config.py as well as config2.py.**


## Limitations
- Google Translate API might limit translations to 5000 characters. (solved)
By default, it's 5 requests/second/user and 200,000 requests/day (Billable limit) but you can increase the limit requests/second/user in your console web developer google (at https://code.google.com/apis/console/).

## Deployment
- There is something called Toolforge that is part of Wikimedia that might be able to host the mature code.

## Help
/#pywikibot on freenode.org or the mailing list at https://lists.wikimedia.org/mailman/listinfo/pywikibot


# Working with Wikipedians on this idea:

Propose at Idea lab first:

Then propose it here:
https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(proposals)
----

Badass tool for when someone wants to take content from one language and translate into another language version of Wikipedia:
https://www.mediawiki.org/wiki/Content_translation


This is a site for software collab within Wikimedia:
https://phabricator.wikimedia.org/

https://en.wikipedia.org/wiki/Wikipedia:Bot_policy

"Contributors should create a separate account in order to operate a bot. The account's name should identify the bot function (e.g. <Task>Bot), or the operator's main account (e.g. <Username>Bot)"

Bots must edit only while logged into their account. New bots are required to use assertion (feature of the API) to ensure that they edit only when logged in. 

operator's account must be prominently identifiable on the bot's user page.

- only use the bot as approved.  Don't even answer questions as the bot.

Bot operators may wish to redirect a bot account's discussion page to their own. 

-if your bot is inactive for 2 years, it gets deauthed.

--------------

'See also' section is what I want to add to.  Could be explicit, to subtle:  ie. 'the German page (link) has 86% different content compared with this entry' or 'see also this German version (link)'

Cultural understandings are locked in the language. ex. Onsen


Premise:
Lively debate in the form of Wiki edits happens across the range of Wikipedia sites, and yet we see sometimes drastically differing narratives when moving from one language to another on the same Wikipedia topic.  This represents a barrier to free thought.  

It is currently unintuitive to read a Wikipedia article and then have the idea to read the same entry in another language.  However, by guiding the reader toward alternate entries of interest, we can inspire thoughts to flow more freely between languages and countries.  This could have the effect of breaking down remaining barriers to freedom of information and thought.

Method:
By visiting a popular entry, such as WWII, a bot could pull from a given language (ex. Japanese), translate that entry through a state of the art translation tool (ex. Google Translate) into English.  It would then compare the English translation to the English entry for WWII.  A NLP algorithm would output the similarity between the documents.  The bot would continue to do this for more languages.  When it discovers the language pair with English that is the most dissimilar, it would add an entry to the 'Further Reading' section mentioning that the language of choice could provide more or differing information to explore.  It would also provide a direct link.

Result:
More information for the reader to explore, which in turn could shape the content of the English entry.  Livelier debate in seeking truth.

Ultimate outcome:
If we adopt this practice for English only, it will enrich Wikipedia.  But, if this practice could spread to the other Wikipedias in other languages, it could really change the spread of ideas.  The bot would already have enough information from entry comparison to make Further Reading entries on every site's entry; the only limitation would be in gaining permission to run the bot on that version of Wikipedia.  This is a human limitation, rather than a technical one.

Possible Counter Arguments:
- Translation between some languages isn't good enough yet.
Perhaps, but we should experiment to see if there is some value in the method first in promoting further inquiry and discussion that can raise the quality of articles across all Wikipedia versions.
- This could have a negative effect on English Wikipedia by introducing false ideas from other languages.
Maybe, but debate, edit wars, and false ideas are nothing new to Wikipedia.  This method could break down a wall that keeps ideas from flowing, and a necessary side effect will be debate.  This should be embraced instead of avoided, as it will lead to better arguments that lead us toward what is true.
- Showing differences in Wikipedia pages about the same topic might hurt cultural interpretations of topics, until all nuance is lost.
The search for truth about any matter involves putting ideas out into the 'marketplace of ideas' for consideration and debate.  I agree that some topics are open to interpretation.  By easing access to other languages/cultures' interpretation of entries, we are allowing those ideas to enter the marketplace of ideas, which should ultimately lend more nuance to any given topic.  If the average Wikipedia entry's length goes up to compensate for that nuance, so much the better.
- We'll need to change something about the format of Wikipedia.  That is hard, and we'll need consensus or a powerful figure to approve it.
The Further Reading section seems like a good place to put this idea.  I also would make the case that all of Wikipedia is malleable, and there was a point when every aspect of it untested.  This is no different.  Doesn't this idea phttps://en.wikipedia.org/wiki/Special:ContentTranslation#suggestionsromote the values of Wikimedia Foundation to, "...empower and engage people around the world to collect and develop educational content...and to disseminate it effectively and globally."? I think so.
- If people want to read an entry in another language, how will they understand it?
I'd like help with this.  Maybe there is a link we could put in the Wiki to a machine translated version?  By necessity, the bot translates (into English only, for the moment).  I could have the bot send this machine translation to a server in the Wikimedia world so that it could be linked for the reader.  This would probably take some collaboration to make happen.  Maybe the bot could seed the https://en.wikipedia.org/wiki/Special:ContentTranslation#suggestions page based on articles that have the most potential information to transfer from one language to the next?
Or here:
https://en.wikipedia.org/wiki/Wikipedia:Proposed_article_mergers

https://www.mediawiki.org/wiki/Extension:Translate


- It seems that what I'm proposing is the reverse of Content Translation:  I want to pull useful content from other languages into English (at first).  Existing to existing. The minimal version would put a notice that novel content exists.  The full up version would pull a translated version of the section that is novel, and prep it for human refinement, references and all.


(Maybe I could extend Content Translation so that it works with existing-existing languages.

---------
About Content Translation:
https://en.wikipedia.org/wiki/Special:ContentTranslation
code
https://gerrit.wikimedia.org/g/mediawiki/extensions/ContentTranslation/


Can I use Content Translation for editing existing articles?
No. (purely for importing and translating from existing to new)


Node.js on the server side, JQuery in the browser.
https://www.mediawiki.org/wiki/Content_translation/Technical_Architecture

How to run it:
https://www.mediawiki.org/wiki/Content_translation/cxserver/Setup


