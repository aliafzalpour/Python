from bs4 import BeautifulSoup
import requests

articles_texts = []
articles_links = []
article_upvote = []
for page in range(0, 6):
    response = requests.get(f"https://news.ycombinator.com/news?p={page}")
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all(name="span", class_="titleline")
    for article_tag in articles:
        text = article_tag.getText()
        articles_texts.append(text)
        link = article_tag.find(name="a").get("href")
        articles_links.append(link)

    # article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
    for score in soup.find_all(name="span", class_="score"):
        article_upvote.append(int(score.getText().split()[0]))

print(articles_texts)
print(articles_links)
print(article_upvote)
max_upvote = max(article_upvote)
max_upvote_index = article_upvote.index(max_upvote)
print(articles_texts[max_upvote_index])
print(articles_links[max_upvote_index])
print(max_upvote)







# with open("./website.html", encoding="utf-8") as file:
#     content = file.read()
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.ul)
# all_anchor_tags = soup.find_all(name="a")
#
# for anchor in all_anchor_tags:
#     print(anchor.getText())
#
# heading = soup.find(id="name")
# print(heading.getText())