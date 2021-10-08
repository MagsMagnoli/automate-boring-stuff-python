import bs4, requests

def get_amazon_price(url):
    headers = {'Cookie': '', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#price_inside_buybox')
    return elems[0].text.strip()

price = get_amazon_price('https://www.amazon.com/Makita-XPH10Z-Lithium-Ion-Cordless-Driver-Drill/dp/B01AD1007I/')
print(f'The price is {price}')