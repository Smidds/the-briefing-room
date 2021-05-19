# import wikipediaapi
# import sys

# wikipediaapi.log.setLevel(level=wikipediaapi.logging.DEBUG)

# out_hdlr = wikipediaapi.logging.StreamHandler(sys.stderr)
# out_hdlr.setFormatter(wikipediaapi.logging.Formatter('%(asctime)s %(message)s'))
# out_hdlr.setLevel(wikipediaapi.logging.DEBUG)
# wikipediaapi.log.addHandler(out_hdlr)

# wikipedia = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)
# countries_list_page = wikipedia.page('List_of_countries')

# # check if page exists
# print("Page - Exists: %s" % countries_list_page.exists())
# # print title
# print("Page - Title: %s" % countries_list_page.title)
# # page url
# print("Page - URL: %s" % countries_list_page.fullurl)


from mediawikiapi import MediaWikiAPI
mediawikiapi = MediaWikiAPI()
countries_page = mediawikiapi.page("List of sovereign states")

print(countries_page.title)
print(countries_page.url)
print(countries_page.content)
