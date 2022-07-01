from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

# all_titles = soup.find_all(name='a', class_='titlelink')
# for title in all_titles:
#     print(title.get('href'))

articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)
    
'''See which articles have most upvotes'''
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
# print(article_upvotes)
most_votes = max(article_upvotes)
mv_index = article_upvotes.index(most_votes)
print(mv_index)
print(article_upvotes[mv_index])
print(article_texts[mv_index])
print(article_texts[27])
print(article_links[mv_index])
'''Index off by 1 for links and texts'''
















# with open('website.html') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# all_anchor_tags = soup.find_all(name='a')
# # print(all_anchor_tags)
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get('href'))
    
# heading1 = soup.find(name='h1', id='name')
# section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading.text)

# company_url = soup.select_one(selector='p a')
# name = soup.select_one(selector='#name')
# headings = soup.select('.heading')
# # print(headings)

