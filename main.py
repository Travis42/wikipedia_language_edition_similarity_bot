#!python3

"""
Main.
"""

# You may need to enforce the use of utf-8
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

def main():



"""
# stub code:
# test to see how I would get info from other sites.
import pywikibot
site = pywikibot.Site()
# How do I iterate through sites?
page = pywikibot.Page(site, u"Hot spring")
engtext = page.text

# How to get the equivalent name in a different language automatically:
other_editions = [link for link in page.iterlanglinks()] # pywikibot.page.Link('Onsen', APISite("az", "wikipedia"))

# could sort the above by language using some criteria ^


site_jp = pywikibot.Site('ja')
page_jp = pywikibot.Page(site, u"熱水泉")
page_jp = pywikibot.Page(site_jp, u"熱水泉")
text_jp = page_jp.text
text_jp

results = [i for i in page.interwiki()] # it gives you all the other language reference links in the page...not the equivalent page in the other languages.

# attempt to get other lang pages:
>>> for page in pagegenerators(pages, 100):
...     print(pagegenerators.InterwikiPageGenerator(page))


see https://github.com/wikimedia/pywikibot/blob/eec2ff54b16cbe92700fb63ea8349c4a80272236/pywikibot/pagegenerators.py
"""
#page:
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__unicode__', '__weakref__', '_cache_attrs', '_cmpkey', '_contentmodel', '_cosmetic_changes_hook', '_getInternals', '_get_parsed_page', '_isredir', '_latest_cached_revision', '_link', '_pageid', '_revid', '_revisions', '_save', '_text', '_timestamp', 'applicable_protections', 'aslink', 'autoFormat', 'backlinks', 'botMayEdit', 'canBeEdited', 'categories', 'change_category', 'clear_cache', 'content_model', 'contributingUsers', 'contributors', 'coordinates', 'create_short_link', 'data_item', 'data_repository', 'defaultsort', 'delete', 'depth', 'editTime', 'embeddedin', 'encoding', 'exists', 'expand_text', 'extlinks', 'fullVersionHistory', 'full_url', 'get', 'getCategoryRedirectTarget', 'getCreator', 'getDeletedRevision', 'getLatestEditors', 'getMovedTarget', 'getOldVersion', 'getRedirectTarget', 'getReferences', 'getRestrictions', 'getTemplates', 'getVersionHistory', 'getVersionHistoryTable', 'image_repository', 'imagelinks', 'interwiki', 'isAutoTitle', 'isCategory', 'isCategoryRedirect', 'isDisambig', 'isEmpty', 'isFlowPage', 'isImage', 'isIpEdit', 'isRedirectPage', 'isStaticRedirect', 'isTalkPage', 'is_categorypage', 'is_filepage', 'is_flow_page', 'iterlanglinks', 'itertemplates', 'langlinks', 'lastNonBotUser', 'latestRevision', 'latest_revision', 'latest_revision_id', 'linkedPages', 'loadDeletedRevisions', 'markDeletedRevision', 'merge_history', 'move', 'moved_target', 'namespace', 'oldest_revision', 'pageAPInfo', 'page_image', 'pageid', 'permalink', 'preloadText', 'previousRevision', 'previous_revision_id', 'properties', 'protect', 'protection', 'purge', 'put', 'put_async', 'raw_extracted_templates', 'revision_count', 'revisions', 'save', 'section', 'sectionFreeTitle', 'set_redirect_target', 'site', 'templates', 'templatesWithParams', 'text', 'title', 'titleForFilename', 'titleWithoutNamespace', 'toggleTalkPage', 'touch', 'undelete', 'urlname', 'userName', 'version', 'watch']
'''