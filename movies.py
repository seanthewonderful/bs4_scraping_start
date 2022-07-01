from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2")
data = response.text

soup = BeautifulSoup(data, 'html.parser')


# rankings = []
# each = soup.find_all(name='div', class_='listicle-item')
# for ea in each:
#     rankings.append(ea.span.text.split()[0])
    
# print(rankings)

titles = soup.find_all(name='h3', class_='jsx-4245974604')
print(titles)
# for title in titles:
#     print(title.getText())

with open("movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")