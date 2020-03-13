import bs4 as bs
import pickle
import requests
class Search_500_Snp:
    def __init__(self, url="https://en.wikipedia.org/wiki/S%26P_500_Index"):
        self.url = url
        pass
    def request(self):
        resp = requests.get(self.url)
        soup = bs.BeautifulSoup(resp.text)
        table = soup.find('table', {'id': 'constituents'})
        tickers = []
        for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            tickers.append(ticker)
        return self.__str__(), tickers

    def save(self, tickers):
        with open("sp500tickers.pickle", "wb") as f:
            pickle.dump(tickers, f)

    def __str__(self, tickers):
        return str(tickers)

search = Search_500_Snp()
search.request()
search.save()
