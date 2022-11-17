import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, link in enumerate(links):
        url = link.find('a')['href']
        title = link.text
        try:
            if len(subtext[idx].text):
                points = int(subtext[idx].text.replace(' points', ''))
                # print(points)
                if points > 99:
                    hn.append({'title': title, 'link': url, 'votes': points})
        except IndexError:
            continue
    return sort_stories_by_votes(hn)


def scrape_hn():
    mega_links = []
    mega_subtext = []

    pages = int(input("How many pages you want to scrape? "))
    for page in range(1, pages+1):
        url = 'https://news.ycombinator.com/news?p='+str(page)
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all(class_="titleline")
        mega_links += links
        subtext = soup.find_all(class_="score")
        mega_subtext += subtext

    pprint.pprint(create_custom_hn(mega_links, mega_subtext))


if __name__ == '__main__':
    scrape_hn()