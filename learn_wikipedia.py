import wikipediaapi as w
wiki_wiki = w.Wikipedia('en')
pag = wiki_wiki.page('python')
print(pag.text[0:500])
