import requests
import csv
import json


def fetch_data():
    url = "https://data.stats.gov.cn/easyquery.htm"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "_trs_uv=lwwyakpv_6267_fr0v; wzws_sessionid=oGaJ9iiBZjFmNmIygmZjNWVlMYAxMTcuMTcyLjE3My4xOQ==; u=6; JSESSIONID=3tSLxfGiQaADpAmvYpQdv1uQP-4aV99TyDKhLaTpZDCcSTZ7l0BX!-1676502051",
        "Host": "data.stats.gov.cn",
        "Referer": "https://data.stats.gov.cn/easyquery.htm?cn=C01",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    industries = {
        "A040202": "Primary",
        "A040203": "Secondary",
        "A040204": "Tertiary"
    }

    params = {
        "m": "QueryData",
        "dbcode": "hgnd",
        "rowcode": "zb",
        "colcode": "sj",
        "wds": "[]",
        "dfwds": "",
        "k1": "1720332167070",
        "h": "1"
    }

    data = []

    for code, name in industries.items():
        params["dfwds"] = f'[{{"wdcode":"zb","valuecode":"{code}"}}]'
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            json_data = json.loads(response.text)
            for item in json_data['returndata']['datanodes']:
                year = item['wds'][1]['valuecode']
                value = item['data']['data']
                if 2019 <= int(year) <= 2023:
                    data.append([int(year), name, round(value)])

    return data


def save_to_csv(data):
    # Sorting the data by the first column (Year) in descending order
    data.sort(key=lambda x: x[0], reverse=True)

    with open('chartTwo.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Year", "Industry", "Employment"])
        writer.writerows(data)


if __name__ == "__main__":
    data = fetch_data()
    save_to_csv(data)
