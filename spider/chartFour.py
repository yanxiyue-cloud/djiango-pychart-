import requests
import pandas as pd
import time

def fetch_data():
    url = 'https://data.stats.gov.cn/easyquery.htm'
    params = {
        'm': 'QueryData',
        'dbcode': 'hgnd',
        'rowcode': 'zb',
        'colcode': 'sj',
        'wds': '[]',
        'dfwds': '[{"wdcode":"zb","valuecode":"A0203"}]',
        'k1': str(int(time.time() * 1000)),
        'h': '1'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['returndata']['datanodes']
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

def extract_data(datanodes):
    data = {}
    for node in datanodes:
        if '2023' in node['code']:
            valuecode = node['wds'][0]['valuecode']
            proportion = node['data']['data']
            if valuecode == 'A020302':
                data['Primary'] = proportion
            elif valuecode == 'A020303':
                data['Secondary'] = proportion
            elif valuecode == 'A020304':
                data['Tertiary'] = proportion

    return data

def save_to_csv(data):
    df = pd.DataFrame(data.items(), columns=['industry', 'data'])
    df.to_csv('chartFour.csv', index=False, float_format='%.1f', encoding='utf-8-sig')
    print("Data saved to chartFour.csv")

def main():
    datanodes = fetch_data()
    if datanodes:
        data = extract_data(datanodes)
        save_to_csv(data)

if __name__ == "__main__":
    main()
