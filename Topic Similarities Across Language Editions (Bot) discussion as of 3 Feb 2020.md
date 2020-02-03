## Topic Similarities Across Language Editions (Bot)

My wife is bilingual.

She noticed that for certain topics in English and in Japanese, 
the content can be different. Sometimes this reflects a difference in 
knowledge that an editor might have due to cultural understanding: [Onsen](https://ja.wikipedia.org/wiki/%E6%B8%A9%E6%B3%89 "ja:温泉") in Japanese has more content than [Onsen](https://en.wikipedia.org/wiki/Onsen "Onsen") in English.

Sometimes it can reflect bias: [Nanjing Massacre](https://en.wikipedia.org/wiki/Nanjing_Massacre "Nanjing Massacre") in English is different in tone and content than the [Japanese version](https://ja.wikipedia.org/wiki/%E5%8D%97%E4%BA%AC%E4%BA%8B%E4%BB%B6 "ja:南京事件"). Take that for what you will.

Languages are boundaries that Wikipedia can and should break down
 to spread knowledge and curb bias. This will make all editions of 
Wikipedia better.

Idea:
For most readers, it is not intuitive to read a Wikipedia article and 
then have the idea to read the same entry in another language. However, 
by guiding the reader toward alternate entries of interest, we can 
inspire thoughts to flow more freely between languages and countries. 
This could have the effect of breaking down remaining barriers to 
freedom of information and thought.

Method: 
By visiting a topic, a bot could pull from a given language (ex. 
Japanese), translate that entry through a translation tool (ex. Google 
Translate) into English. It would then compare the English translation 
to the English entry. A NLP algorithm (LSA) would output the similarity 
between the documents. The bot then continues to do this for more 
languages. When it discovers the language pair with English that is the 
most dissimilar, it would add an entry to the 'See Also' section 
mentioning that the language of choice could provide more or differing 
information to explore. It would also provide a direct link.

Result: 
More information for the reader to explore, which in turn could shape 
the content of the English entry. The same could be done in reciprocal 
for the topics in the other language editions. This will help readers 
unlock ideas from cultures around the world, and spread knowledge.

Status:
I made the bot. It works, but I'm busy updating instructions so that 
people can use it. Right now it only gathers articles and compares 
them--I realize that I need the community to give me permission to edit 
articles.

I've gathered and compared ~4800 articles so far, and there is 
ample evidence that articles vary according to their language edition. 
It does seem that there is more knowledge to be shared among established
 topics. I can work on making some charts, and if anyone is interested 
in taking a look for themselves to do a little data science, I'm happy 
to share the db.

You can find the bot code here: [https://github.com/Travis42/wikipedia_language_edition_similarity_bot](https://github.com/Travis42/wikipedia_language_edition_similarity_bot)

If this interests you, please help me by checking out the code, 
giving insights in how to craft a proposal, spreading the word, or 
showing me where I could go to find the right crowd here on Wikipedia to
 make this happen.

Thanks! — Preceding [unsigned](https://en.wikipedia.org/wiki/Wikipedia:Signatures "Wikipedia:Signatures") comment added by [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42#top "User talk:Theory42") • [contribs](https://en.wikipedia.org/wiki/Special:Contributions/Theory42 "Special:Contributions/Theory42")) 04:45, 12 January 2020 (UTC)

There isn't a single entity called "Wikipedia"; each of the 297 
Wikipedias is an independent entity with its own rules on sourcing, 
notability, scope, bias, and what constitutes appropriate content. 
Except for the most basic inconsistency in facts (e.g. "Latin Wikipedia 
says that the Battle of the Alamo took place in 1835 but English 
Wikipedia says that it took place in 1836"), I doubt 
comparing-and-contrasting would be a particularly useful exercise. When 
the community of another language Wikipedia deems their version of an 
article to be of particularly high quality, it's already flagged as such
 in the interwiki link sidebar on that article (see the aforementioned [Battle of the Alamo](https://en.wikipedia.org/wiki/Battle_of_the_Alamo "Battle of the Alamo") for an example). I'd also worry that any kind of plugin linking to 
machine translations would—regardless of intent—lead to editors 
copy-pasting machine translated text into en-wiki articles, which will 
get them blocked and the bot shut down very quickly; see [Wikipedia:Administrators' noticeboard/CXT](https://en.wikipedia.org/wiki/Wikipedia:Administrators%27_noticeboard/CXT "Wikipedia:Administrators' noticeboard/CXT") for some previous discussions about the role of machine translation on en-wiki. ‑ [Iridescent](https://en.wikipedia.org/wiki/User:Iridescent "User:Iridescent") 15:52, 12 January 2020 (UTC)

Thank you for the initial feedback. I'm not suggesting that we 
correct other Wikipedias. What I am suggesting is that we use this bot 
to create a greater awareness that other Wikipedias have information 
worth considering, when such differences exist. The bot can (does) 
point these differences out. The main benefit is to readers, and of 
course if someone wishes to translate information from one Wikipedia to 
another, that is a net benefit to both.

I should also clarify that the bot doesn't point to an English 
translation--I wouldn't know where to store such a thing at present. 
What I'm suggesting is merely a link to the original content along with a
 note to the reader saying that the content is different enough to 
warrant 'See Also' consideration--it would be on the reader to run it 
through their favorite translator.

Last, although Wikipedia editions are run by different crowds, there
 is only one Wikimedia Foundation (to my knowledge). Its mission 
statement is to, "...empower and engage people around the world to 
collect and develop educational content under a free license or in the 
public domain, and to disseminate it effectively and globally." I see 
this as a way to disseminate educational content effectively and 
globally.

What else is needed to develop this idea into something that works 
with the rules of Wikipedia? I hope you can see that it complies with 
its ethos. — Preceding [unsigned](https://en.wikipedia.org/wiki/Wikipedia:Signatures "Wikipedia:Signatures") comment added by [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42#top "User talk:Theory42") • [contribs](https://en.wikipedia.org/wiki/Special:Contributions/Theory42 "Special:Contributions/Theory42")) 17:32, 12 January 2020 (UTC)

- @[Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)"): How are you assessing "different" - a badly written stub article on one
   wikipedia would be more different to a good en-wiki article than a 
  well-written, but heavily differently positioned article. You state the 
  ethos being met as a given, but I'd want to see that, at least the vast 
  (90+%) majority of the time, it was a genuine difference in 
  position/tone that was giving the #1 different article, rather than 
  quality issues - before even moving onto other aspects. 
  Non-controversial articles of equal quality are less likely to be 
  different. We have a great deal of concern of directing readers to 
  controversial articles in other wikipedias without someone giving them a
   once-over to check they're legit. For example, the Azerbaijani 
  wikipedia article on Armenia, its history, and such are very different. 
  However, that Wikipedia is currently under meta discussion to strip 
  every admin of their position because (amongst other things), many of 
  them are accused of having interfered in the content to prevent a 
  neutral article. Sending a reader to something like that would be 
  counter to our ethos. [Nosebagbear](https://en.wikipedia.org/wiki/User:Nosebagbear "User:Nosebagbear") ([talk](https://en.wikipedia.org/wiki/User_talk:Nosebagbear "User talk:Nosebagbear")) 14:15, 13 January 2020 (UTC)

@[Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)"): This is interesting work! I wanted to point you to some research in 
this area that could perhaps give you more ideas and guide your work. 
First, there's some recent work on [aligning articles across different languages](https://meta.wikimedia.org/wiki/Research:Expanding_Wikipedia_articles_across_languages/Inter_language_approach "meta:Research:Expanding Wikipedia articles across languages/Inter language approach") and building a recommender system to suggest new sections to add to 
articles based on content in other languages. Secondly, going back 
almost ten years now, there's a couple of papers that looked 
specifically at differences between languages and how to enable 
exploration of that. The [Omnipedia paper](http://brenthecht.com/papers/bhecht_CHI2012_omnipedia.pdf) builds a visualization tool based on differences in links used in the 
articles (and also builds an algorithm to discover additional links). 
The [Manypedia paper](https://www.opensym.org/ws2012/p13wikisym2012.pdf) is similar to yours in that it uses machine translation, but in this 
case has a user interface that puts two articles up side-by-side so the 
user can explore them. Hope these are useful food for thought and 
inspiration! Cheers, [Nettrom](https://en.wikipedia.org/wiki/User:Nettrom "User:Nettrom") ([talk](https://en.wikipedia.org/wiki/User_talk:Nettrom "User talk:Nettrom")) 16:27, 13 January 2020 (UTC)

- I like the idea in principle. I'm wondering about how articles 
  are identified as sufficiently different. Could we have a look at some 
  results? I'm particularly interested to see some controls, like the 
  results for articles that we know to be related (e.g. articles on other 
  language wikipedias that we know to have been recently translated from 
  the English one). Implementing the proposal is going to be logistically 
  difficult though: to get the bot to edit on any language wikipedia will 
  need the approval of that wikipedia's community, and that's a separate 
  process for each of them (for the English wikipedia, the main page is at
   [Wikipedia:Bot policy](https://en.wikipedia.org/wiki/Wikipedia:Bot_policy "Wikipedia:Bot policy"),
   and the approvals process is linked from there). I believe some 
  wikipedias will be favourable to such a proposal, but I do not believe 
  the English wikipedia will be among them. There's a general aversion 
  here to any large-scale bot edits that touch on matters of content, 
  external links to content in other langauges is discouraged ([WP:NONENGEL](https://en.wikipedia.org/wiki/Wikipedia:NONENGEL "Wikipedia:NONENGEL")),
   and there are often legitimate concerns about the neutrality of whole 
  swathes of articles on other language wikipedias (the Croatian 
  Wikipedia, which has been taken over by neo-Nazis, is only one extreme, 
  though by no means unusual, example). – [Uanfala (talk)](https://en.wikipedia.org/wiki/User_talk:Uanfala "User talk:Uanfala") 16:32, 13 January 2020 (UTC)

Thank you all for your replies. Your comments have given me a lot to consider. Addressing the comments in order:

- @[Nosebagbear](https://en.wikipedia.org/wiki/User:Nosebagbear "User:Nosebagbear"): I will run some tests this weekend to see how comparisons work between 
  very short texts and long texts, by using an example text and extracts 
  of itself in increasingly small samples. Will let you know what the 
  effect is. Given what I know of how the comparisons are made, I believe
   that even a stub that uses the same wording as found in a longer 
  article will show a high correlation, but it does need to be tested. 
  The larger issue of legitimacy in controversial articles hits upon a 
  part of why I'm interested in this topic--I want to help point people to
   different perspectives who may be in a thought bubble. You bring up a 
  good point that the sword could cut both ways by introducing a reader to
   different content that is of questionable quality.

- @[Nettrom](https://en.wikipedia.org/wiki/User:Nettrom "User:Nettrom"): The links you've provided are excellent. Some of the code pointed me 
  to an alternate way of getting to some machine translation as well. 
  With these other, very similar attempts, I am only left to wonder: why 
  did they choose to make their own offsite apps instead of using what 
  they made to improve Wikipedia?

- @[Uanfala](https://en.wikipedia.org/wiki/User:Uanfala "User:Uanfala"): Thank you for the suggestions--I only have time to do this on weekends,
   so it might be some time, but the proof you're asking for is something 
  I'd like to show. Give me some time and I'll do it...up to now all I 
  have is what's stored in a database and what I saw scrolling in my 
  output. Needs to be charted and prettified. I think you're right about
   the approval for most Wikipedias, although I hope you're not correct 
  about En. Ideally I would not be the only one running this bot, as the 
  translation interface is a bottleneck for one individual (machine 
  translation in bulk has costs, but free accounts can get a certain 
  quota). Part of my motivation for this is to shed light on bad/biased 
  articles (as well as point to good) because I think there is a 
  responsibility for this site to be of high quality. From the sound of 
  it, many editors are well aware that there are articles in other 
  languages that are not in the spirit of what the site should be about 
  (your Croatia example). How is such a thing even tolerated by the 
  Wikimedia Foundation, when millions (billions?) rely on this 
  information? I don't get it. This might be a harder problem than I 
  realized. [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 13:59, 16 January 2020 (UTC)

- @[Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)"): Thanks a lot for undertaking this! There is a great dearth of machine 
  learning research and software on Wikipedia. I don't think a consensus 
  can be established to allow you to directly put the links on the 
  articles (per comments above). But what you can do is create an external
   tool in which one can enter an article name and get the list of other 
  wikis which have significantly different articles on the same topic. You
   can host it on your domain if you have one, but Wikipedians generally 
  prefer to use tools hosted on the [Toolforge](https://tools.wmflabs.org) - you'll have to request an account there. This will help editors to 
  easily find articles on other wikis with different content, for 
  translating from. [SD0001](https://en.wikipedia.org/wiki/User:SD0001 "User:SD0001") ([talk](https://en.wikipedia.org/wiki/User_talk:SD0001 "User talk:SD0001")) 07:51, 19 January 2020 (UTC)

- @[Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)"): I agree a similarity index could be helpful, and where the best article
   across the language versions has already been identified, this should 
  serve as the comparison baseline, so others can then see how far they're
   off, and investigate further what they need to do to close the gap 
  (where best versions have not been identified, the English version might
   serve as the baseline, since these are often best). However, I believe 
  it would help to provide other metrics beyond just a similarity index. 
  It appears the LSA metric you’re using is based on comparisons of 
  relative word frequencies (such as tf-idf) across documents. Thus it 
  would be helpful when comparing 2 language versions, if the list of 
  words with the greatest difference in relative frequency was also shown.
   This could be done in a number of ways, and by glancing at these words 
  editors could then gain better insight into what is driving the 
  difference – e.g. is it bias, or is one article simply missing certain 
  information, etc. Since I am very interested in detecting bias I’d be 
  glad to help anyway I can – e.g. provide suspected biased articles for 
  testing, review and comment on the results, etc [Thhhommmasss](https://en.wikipedia.org/w/index.php?title=User:Thhhommmasss&action=edit&redlink=1 "User:Thhhommmasss (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Thhhommmasss "User talk:Thhhommmasss")) 20:00, 23 January 2020 (UTC)

- @[SD0001](https://en.wikipedia.org/wiki/User:SD0001 "User:SD0001"): Thanks for the tip about Toolforge. I'm going to sign up for it soon. 
  Its nice to know that projects like this can have a cloud hosted home. [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 02:58, 27 January 2020 (UTC)

- @[Thhhommmasss](https://en.wikipedia.org/w/index.php?title=User:Thhhommmasss&action=edit&redlink=1 "User:Thhhommmasss (page does not exist)"): These are good suggestions. I can say that the way I've structured the
   bot so far, its English centric as a 'primary' language. That could 
  easily be adjusted by others, but I guess it kind of meets the intent of
   your first improvement idea, at least in a broad sense. I get what 
  you're saying about using TF-IDF to narrow in on the sections of 
  documents that are most different--but if you want to elaborate, please 
  do. I'll need to think a bit more about the idea to know how to 
  implement it. If you want to send articles of interest my way, please 
  do. The best avenue for that is probably the [Issues page on the Github](https://github.com/Travis42/wikipedia_language_edition_similarity_bot/issues), but you can put them here as well. [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 02:58, 27 January 2020 (UTC)

Update: I had a bug in how the scores were being stored in the db, 
and managed to clean that up this weekend. Through the suggestions 
here, I was also able to find something that the Wikimedia Interlanguage
 team is doing that is similar: [Suggestions for Sections](https://phabricator.wikimedia.org/T224234).
 There is a tool called Content Translation that Wikimedia makes 
available for bilingual people to translate pages. Up to now, this tool
 has only been available for use when a given article exists in one 
language, but not the target language. This new feature will suggest 
'sections' of articles that exist in one language, but not another. 
This means that there will soon be a mechanism for editors to add 
content to articles using suggested content from another language's 
established content, where there exists extra sections in one but not 
the other.

I don't view this as exactly hitting upon the problem set I'm 
interested in, but it is getting close. Does anyone here think that it 
overlaps enough, or do you think that the idea of pointing out 
differences in articles across languages to the readers of Wikipedia (my
 approach) is still a good path to try and go down? Thanks, [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 02:58, 27 January 2020 (UTC)

Maybe you can combine the two since I see advantages to both – 
they identify missing sections, but particularly if you add info on 
differences (Diff) in relative word frequency between 2 articles it can 
offer further insight. E.g. you could calculate:

   Diff(j) = TF-IDF(Article-English)(j) – TF-IDF(Article-German)(j)

where j=1..N is number of unique words across both articles. 
Results could be presented as a list, such as: Word1(Diff1), 
Word2(Diff2), Word3(Diff3)….Word19(Diff19), Word20(Diff20), where these 
are 20 words with the greatest absolute Diffs in relative frequency, 
ordered from most positive (where relative frequency in English article 
is higher) to most negative (where relative frequency in English article
 is lower). I believe -1<Diff<1, so positive Diff Words could be 
highlighted Green while negative Diff ones Red. Looking at these words 
with the greatest Diffs, could provide further insight into what is 
driving overall differences between 2 articles – bias, missing info, 
something else.

It’d be even more useful to show English and German articles 
side-by-side, and highlight the 20 words with greatest Diffs in both 
articles, so users can see sentences these words appear in, for an even 
better sense of what is driving differences. If an Editor wanted to make
 German article more like the English one, they could look at English 
article sentences where the Green-highlighted, positive Diff words 
appear, and then add more of this specific info to the German article. 
For sentences in the German article where the Red-highlighted, negative 
Diff words appear, they could delete or change these sentences, to make 
the article more like the English one

So this would provide more granular, sentence- and word-level 
info on the differences, beyond just missing sections. Btw, I wonder if 
such Word Diffs might also help in comparing 2 regular WP Version diffs.
 For example, inside the current Version diff comparison, calculating 
and highlighting the Words with the greatest TF-IDF Diff between the 2 
Versions, might help editors at-a-glance see which words are the key to 
the changes [Thhhommmasss](https://en.wikipedia.org/w/index.php?title=User:Thhhommmasss&action=edit&redlink=1 "User:Thhhommmasss (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Thhhommmasss "User talk:Thhhommmasss")) 00:03, 28 January 2020 (UTC)

@[Thhhommmasss](https://en.wikipedia.org/w/index.php?title=User:Thhhommmasss&action=edit&redlink=1 "User:Thhhommmasss (page does not exist)"): @[SD0001](https://en.wikipedia.org/wiki/User:SD0001 "User:SD0001"): @[Uanfala](https://en.wikipedia.org/wiki/User:Uanfala "User:Uanfala"): @[Nettrom](https://en.wikipedia.org/wiki/User:Nettrom "User:Nettrom"): @[Nosebagbear](https://en.wikipedia.org/wiki/User:Nosebagbear "User:Nosebagbear"): I took the essence of Thhhommmasss's suggestion and managed to create 
an initial result. The new algorithm finds the article with the 
greatest content distance from the primary language (ex. English). It 
then chops up the article into sentences and compares each to the 
primary language document. The output is the translated sentences with 
different content, most different to least different. You can see an 
example [here](https://github.com/Travis42/wikipedia_language_edition_similarity_bot/blob/master/Preliminary%20Results%20for%20sentence%20comparisons.md). The first few results represent image captions, I believe. Scroll down a bit and you'll see some coherent sentences.

I like your idea of having a web interface for editors and readers 
to quickly discern these sentences by highlighting them. However, this 
represents a huge amount of work to make happen. Right now my bot/app 
is backend only, and ideally I would like to point out content 
differences using edits to Wikipedia. If this turns out not to be 
possible, I guess it could be a stand alone app. I get the sense that 
this would reach FAR less people though, and that makes me reticent to 
dive right in.

Anyone have further thoughts for me? I'm not sure how to proceed at present. [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 18:27, 2 February 2020 (UTC)

@[Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)"): This is very nice. I think it is significant both that the Japanese 
version is furthest from the English, and the individual sentences that 
are furthest off indeed start to provide a sense of what is causing the 
differences - bias and different sources used (which are no doubt the 
source of the bias). Btw, it would also help to do the reverse calc - 
i.e. English version sentences most different from the Japanese version

This needs a front-end to be useful. The above-mentioned
 Manypedia already has some of the front-end UI elements (e.g. 
side-by-side comparisons of different language articles), and the 
Wikipedia Interlanguage Team might also be interested in incorporating 
this, so I’d suggest you contact them. Since I’d be interested in using 
this, I’ll be glad to add my thoughts on how it could be most useful [Thhhommmasss](https://en.wikipedia.org/w/index.php?title=User:Thhhommmasss&action=edit&redlink=1 "User:Thhhommmasss (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Thhhommmasss "User talk:Thhhommmasss")) 21:11, 2 February 2020 (UTC)

I decided to rip through everything I have in my database so far. You can see results from a bunch of entries [here](https://github.com/Travis42/wikipedia_language_edition_similarity_bot/tree/master/results).
 As for what you just said about a front end...I need to chew on the 
idea a bit. Sounds like a next weekend project for now. Cheers! [Theory42](https://en.wikipedia.org/w/index.php?title=User:Theory42&action=edit&redlink=1 "User:Theory42 (page does not exist)") ([talk](https://en.wikipedia.org/wiki/User_talk:Theory42 "User talk:Theory42")) 23:17, 2 February 2020 (UTC)
