import requests
import pandas as pd


def crawl_data_and_save_csv():
    url = 'https://data.stats.gov.cn/easyquery.htm'
    params = {
        'm': 'QueryData',
        'dbcode': 'hgnd',
        'rowcode': 'zb',
        'colcode': 'sj',
        'wds': '[]',
        'dfwds': '[{"wdcode":"zb","valuecode":"A020B"}]',
        'k1': '1720322333506',
        'h': '1'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()['returndata']['datanodes']

    # Extracting data
    urban_data = {}
    rural_data = {}

    for node in data:
        if node['wds'][0]['valuecode'] == 'A020B03':
            year = node['wds'][1]['valuecode']
            urban_data[year] = round(node['data']['data'])
        elif node['wds'][0]['valuecode'] == 'A020B02':
            year = node['wds'][1]['valuecode']
            rural_data[year] = round(node['data']['data'])

    # Creating DataFrame
    years = sorted(set(urban_data.keys()).union(set(rural_data.keys())))
    urban_values = [urban_data.get(year, None) for year in years]
    rural_values = [rural_data.get(year, None) for year in years]

    df = pd.DataFrame({
        'Year': years,
        'Urban': urban_values,
        'Rural': rural_values
    })

    # Saving to CSV
    df.to_csv('chartThree.csv', index=False)


if __name__ == "__main__":
    crawl_data_and_save_csv()
