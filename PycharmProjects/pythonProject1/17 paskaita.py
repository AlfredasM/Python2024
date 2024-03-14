import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

properties = []
for i in range(1,6):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'
    }

    target = f'https://www.kyero.com/en/portugal-property-long-let-1l55731?page={i}'
    response = requests.get(target, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    property_list = soup.find_all('li', class_='mt-5 sm:my-2 sm:px-2 sm:w-1/2 md:w-full md:px-0 md:mx-0 md:mt-5')

    for property in property_list:
        title = property.find('p',
                              class_='mb-1 text-xl font-decor md:w-8/12 leading-tight font-bold md:mt-auto').text.strip()
        price = property.find('a', class_='variant-price')
        if price:
            price_text = price.text.strip()
            numbers = re.findall(r'\d+', price_text)
            price_numeric = int(''.join(numbers))
        else:
            price_numeric = 'Price not found'

        bedrooms = 'N/A'
        bathrooms = 'N/A'
        living_space = 'N/A'

        details_container = property.find('ul', class_='flex')
        if details_container:
            elems = details_container.find_all('li', class_='mr-3 flex items-center')

            for elem in elems:
                svg = elem.find('svg')
                item = elem.find('span', class_='font-bold').text.strip()
                if svg:
                    viewbox = svg.get('viewbox')
                    if viewbox == "0 0 20 19":
                        bedrooms = int(item)
                    elif viewbox == "0 0 20 17":
                        bathrooms = int(item)
                else:
                    living_space = float(item.replace(' m²', '').replace(',', '.'))

        properties.append({
            'title': title,
            'price': price_numeric,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'living_space': living_space
        })

df = pd.DataFrame(properties)
print(df)
df.to_csv('properties.csv', index=False)
