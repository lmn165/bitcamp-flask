import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen


class MelonMusic:
    def __init__(self, url):
        self.url = url

    def scrap(self):
        header = {'User-Agent' : 'Mozilla/5.0'}
        modi = urllib.request.Request(self.url, headers=header)
        soup = BeautifulSoup(urlopen(modi).read(), 'html.parser')
        ls_artist = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        for i, val in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})):
            print(str(i+1) + ' Rank')
            print(f'Title: {val.find("a").text}')
            print(f'Artist: {ls_artist[i].find("a").text}')

        # for i, val in enumerate(soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})):
        #     print(str(i+1) + ' Rank')
        #     print(f'Artist: {val.find("a").text}')


def main():
    # 2021072016
    MelonMusic(f'https://www.melon.com/chart/index.htm?dayTime={input("Date: ")}').scrap()


if __name__ == '__main__':
    main()