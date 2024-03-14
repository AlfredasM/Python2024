class VarleScraper:
    def __init__(self, url):
        self.url = url
        self.soup = None

    def fetch(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print('Something went wrong cannot get a website data..')

    def parse_page(self):
        product_list = []
        products = self.soup.find_all('div', class_='GRID_ITEM')
        for product in products:
            product_name = product.find('div', class_='product-title').text.strip()
            product_price = product.find('span', class_='price-value').text.strip().replace('\n\xa0', '')
            rating = product.find('li', attrs={'class': 'rating'}).text.strip().replace('\n', '')[:3]

            # print(product_price)
            product_list.append({
                'Produkto pavadinimas': product_name,
                'Produkto kaina': product_price,
                'Ivertinimas': rating
            })
        print(product_list)

    def run(self):
        self.fetch()
        if self.soup:
            self.parse_page()


scraper = VarleScraper('https://www.varle.lt/isoriniai-kietieji-diskai-hdd/')
scraper.run()