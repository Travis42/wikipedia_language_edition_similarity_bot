# Project Log
- Pywikibot code lives here for search purposes: https://github.com/wikimedia/pywikibot/


## Next Actions

- take another example of 'onsen' from a new language. (done)
    - Process it together with english and japanese
    - store it, and make sure it stores correctly.
        - might need the foreign key to be 'English title' instead of id...can't seem to get those to match.

- add tokenized version to the datastore.

- consider limiting the study to the top n langs on wikipedia.  This can be found on their front page.
    - top langs by active users, descending:
        - English
        - French
        - German
        - Spanish
        - Japanese
        - Russian
        - Italian
        - Chinese
        - Portuguese
        - Arabic
        - Polish
        - Persian
        - Dutch
        - Indonesian

    - source: https://en.wikipedia.org/wiki/List_of_Wikipedias#Detailed_list

#### Why use active users?  

Because I found a lot of discrepancies in other metrics.  Cebuano has the second highest number of articles outright, but they don't have much depth and aren't edited much, which tells me that total articles might not be the best metric.  Active Users is a metric that tells me that the language edition is being kept up and used, and therefore this study will be useful to more people that way.)
    - Contra:  if the idea is to unlock knowledge bound up in cultural understanding as defined by language, wouldn't I want to use the most obscure languages?
        - the problem here comes from diminishing returns from smaller wikipedias.  For this to work, there needs to be an article on the same topic in each language.
        - There is a larger effort to create new articles in other Wikipedias if an entry exists in one language but not the other.  That effort pushes knowledge to other editions, while my project pulls and consolidates knowledge from wikipedia editions.
            - I must first determine if there is 'fruit to pick' from the top languages.  By proving the concept, I can come back around later and do a study on less prolific Wikipedia editions.






- make a robust way of crawling a list of articles.



- store the comparisons.  Store the translated article with the most dissimilarity to the English one, as well as the English doc.
    - ensure that the id numbers match: primary matches all the child translations in terms of id.

- by storing the similarity matrix, I can go back later and do analytics.

- compare top languages (these are shown on wikipedia's main page.)

- determine if its best to run this bot inside the pywikibot clone, or better to instally with pip. Main conscern is with user_config.py as part of pywikibot.
- mess with user-config.py

- (goal should be to grab as much as possible this month and then allow for edits later)  I don't need to edit for a month or more, and approval will take time. Bot scripts exist in the folder that comes with pywikibot.



## Open Questions:
*send questions to pywikibot@lists.wikimedia.org*
*API: https://doc.wikimedia.org/pywikibot/master/api_ref/pywikibot.html?*

- How much is an Azure cloud instance per month?  Comparable to DigitalOcean?




"pywikibot.pagegenerators module

This module offers a wide variety of page generators.

A page generator is an object that is iterable (see http://legacy.python.org/dev/peps/pep-0255/ ) and that yields page objects on which other scripts can then work.

Pagegenerators.py cannot be run as script. For testing purposes listpages.py can be used instead, to print page titles to standard output."


    - I want to start with the most visited pages and work my way down.  Is that possible?

---

- What do these abbreviations correspond to?
This is the list of known languages:
en, ceb, sv, de, fr, nl, ru, it, es, pl, war, vi, ja, zh, ar, pt, uk, fa, ca, sr, no, id, ko, fi, hu, sh, cs, ro, eu, tr, ms, eo, hy, bg, da, he, ce, zh-min-nan, sk, kk, min, hr, et, lt, be, el, sl, gl, az, azb, simple, nn, ur, hi, th, ka, uz, la, ta, vo, cy, mk, tg, ast, lv, mg, tt, af, oc, bs, ky, bn, sq, tl, zh-yue, new, te, be-tarask, br, ml, pms, su, nds, lb, ht, jv, sco, mr, sw, ga, szl, pnb, ba, is, my, fy, cv, lmo, an, ne, pa, yo, bar, io, gu, arz, als, ku, scn, kn, bpy, ckb, wuu, ia, qu, mn, bat-smg, si, wa, cdo, or, gd, yi, am, nap, bug, ilo, mai, hsb, xmf, map-bms, fo, mzn, diq, li, sd, vec, eml, sah, os, sa, ps, nv, ace, mrj, mhr, zh-classical, hif, frr, bcl, roa-tara, hak, pam, nso, km, hyw, se, rue, mi, vls, bh, nah, nds-nl, crh, gan, vep, sc, as, shn, ab, glk, bo, myv, co, so, tk, fiu-vro, lrc, kv, csb, gv, sn, udm, zea, ay, ie, pcd, kab, nrm, ug, ha, lez, stq, kw, mwl, haw, gn, gom, rm, lij, lfn, lad, lo, frp, koi, mt, fur, dsb, dty, ang, ext, olo, ln, cbk-zam, dv, bjn, ksh, gag, pfl, pi, pag, gor, av, bxr, xal, krc, sat, za, pap, tyv, kaa, pdc, rw, to, kl, nov, jam, arc, kbp, kbd, tpi, tet, ig, ki, zu, wo, na, jbo, tcy, roa-rup, lbe, bi, szy, ty, mdf, kg, lg, inh, srn, atj, xh, ban, ltg, chr, got, sm, pih, om, ak, tn, tw, cu, ts, rmy, bm, st, chy, rn, tum, ny, fj, ch, ss, nqo, gcr, pnt, ady, iu, mnw, ve, ee, ks, ik, sg, ff, dz, ti, din, cr, aa, cho, ho, hz, ii, kj, kr, mh, mus, ng, ten, test, test2

- If I start at a particular site, how do I get the equivalent site in each language?  There seem to be functions that used to do this (see below) but they are deprecated.  The ones that do exist (interwiki) are meant to grab links within a document, not the title link for an equivalent site.

## Temp notes

https://www.mediawiki.org/wiki/Manual:Pywikibot/interwiki.py
https://github.com/wikimedia/pywikibot/blob/9f1401842c85790c97056a8d517e7031d9b725db/scripts/interwiki.py
This has functionality to find articles on other Wiki language editions that are of the same type as the one you're on.  The purpose was to make sure links are good, but maybe I can use it to help me pull the articles I want to translate.
- I would need to extract relevant code.  The script is not meant for my purposes directly, and would be dangerous to run outright.
- More specifically, I think I can use this to just give me the interwiki sites for any given English page:
https://github.com/wikimedia/pywikibot/blob/0a2bd87ccb881fa4021b5c144a35fdd25e25c03a/scripts/standardize_interwiki.py

- Even better: (**says its deprecated...either find the new thing or copy the code**) **I could also hack it and 'undeprecate' within pywikibot**
    - https://github.com/wikimedia/pywikibot/blob/7ea6fba1a245024262fb778864d96cb0794336b6/pywikibot/titletranslate.py
    from titletranslate import translate
    translate('page title') # or the url of the site
    - what should come back is a list of titles in other languages.







## Starting:

python3 pwb.py login starts the bot up.



python3 pwb.py -lang:xx
Will switch to the language edition of choice.  I should probably have a handler script that uses this method to scrap a bunch of sites, then process another way.


-simulate   Disables writing to the server. Useful for testing and debugging of new code (if given, doesn't do any real changes, but only shows what would have been changed).




### Pay attention to global scripts you can use:
https://www.mediawiki.org/wiki/Manual:Pywikibot/Scripts




## Answered Tech Qs
- How do I iterate through sites?
    - *Answer: pywikibot.Page(site, u"Hot spring")
        results = [i for i in page.iterlanglinks()] # has the goods*





























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

