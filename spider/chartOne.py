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
        'dfwds': '[{"wdcode":"zb","valuecode":"A020101"}]',
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
    data = []
    for node in datanodes:
        for year in range(2014, 2024):
            if str(year) in node['code']:
                gdp = float(node['data']['data']) / 10000  # 转换为万亿单位
                gdp_rounded = round(gdp)  # 四舍五入
                data.append({'year': year, 'data': gdp_rounded})
                break
    return data

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('chartOne.csv', index=False, float_format='%.1f', encoding='utf-8-sig')
    print("Data saved to chartOne.csv")

def main():
    datanodes = fetch_data()
    if (datanodes):
        data = extract_data(datanodes)
        save_to_csv(data)

if __name__ == "__main__":
    main()
