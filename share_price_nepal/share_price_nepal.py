from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


def get_price(csv=False):
    '''
    This function returns today's share price of Nepal.
    To save this data to csv pass parameter of csv=True in the get_price function.
    '''

    html = requests.get('https://www.sharesansar.com/today-share-price').text
    soup = BeautifulSoup(html, 'lxml')

    tables = soup.select('#headFixed > tbody')

    data = []
    table_rows = tables[0].find_all('tr')

    for items in range(len(table_rows)):
        table_data = table_rows[items].find_all('td')
        table_content = {
            'Index': table_data[0].text,
            'Symbol': table_data[1].text.replace('\n', ''),
            'Open': table_data[3].text,
            'High': table_data[4].text,
            'Low': table_data[5].text,
            'Link': table_data[1].a['href']}

        data.append(table_content)

    if csv == True:
        try:
            os.mkdir('output')
            os.chdir('output')

        except:
            os.chdir('output')

        df = pd.DataFrame(data)
        df.to_csv('output.csv', index=False)
        print('File Created')

    return data
