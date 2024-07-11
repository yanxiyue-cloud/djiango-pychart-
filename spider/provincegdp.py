import os
import requests
import csv

# 禁用代理
os.environ['HTTP_PROXY'] = ''
os.environ['HTTPS_PROXY'] = ''

# 省份代码和名称的映射
province_code_to_name = {
    "110000": "北京市",
    "120000": "天津市",
    "130000": "河北省",
    "140000": "山西省",
    "150000": "内蒙古自治区",
    "210000": "辽宁省",
    "220000": "吉林省",
    "230000": "黑龙江省",
    "310000": "上海市",
    "320000": "江苏省",
    "330000": "浙江省",
    "340000": "安徽省",
    "350000": "福建省",
    "360000": "江西省",
    "370000": "山东省",
    "410000": "河南省",
    "420000": "湖北省",
    "430000": "湖南省",
    "440000": "广东省",
    "450000": "广西壮族自治区",
    "460000": "海南省",
    "500000": "重庆市",
    "510000": "四川省",
    "520000": "贵州省",
    "530000": "云南省",
    "540000": "西藏自治区",
    "610000": "陕西省",
    "620000": "甘肃省",
    "630000": "青海省",
    "640000": "宁夏回族自治区",
    "650000": "新疆维吾尔自治区"
}


def get_province_gdp(year):
    url = "https://data.stats.gov.cn/easyquery.htm"
    params = {
        'm': 'QueryData',
        'dbcode': 'fsnd',
        'rowcode': 'reg',
        'colcode': 'sj',
        'wds': '[{"wdcode":"zb","valuecode":"A020101"}]',  # GDP指标代码，可能需要根据实际情况调整
        'dfwds': f'[{{"wdcode":"sj","valuecode":"{year}"}}]',  # 指定年份
        'k1': 'timestamp'
    }

    headers = {
        'User-Agent': 'Your User Agent String'  # 请替换成你的User-Agent，模拟浏览器请求
    }

    response = requests.post(url, data=params, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        data_nodes = json_data['returndata']['datanodes']

        province_gdp = []
        for node in data_nodes:
            province_code = node['wds'][1]['valuecode']  # 省份代码
            province_name = province_code_to_name.get(province_code, "未知省份")  # 获取省份名称
            gdp_value = float(node['data']['strdata'])  # GDP数据，转换为浮点数
            rounded_gdp = round(gdp_value)  # 四舍五入
            province_gdp.append((province_name, year, rounded_gdp))

        return province_gdp
    else:
        print(f"Failed to retrieve data for year {year}. Status code: {response.status_code}")
        return None


def save_combined_gdp_csv(data):
    filename = 'provincegdp.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'year', 'data'])

        for item in data:
            writer.writerow(item)


if __name__ == "__main__":
    combined_gdp_data = []
    for year in [2014, 2023]:
        gdp_data = get_province_gdp(year)
        if gdp_data:
            combined_gdp_data.extend(gdp_data)

    # 按省份名称排序
    combined_gdp_data.sort(key=lambda x: x[0])

    save_combined_gdp_csv(combined_gdp_data)
    print("Combined GDP data saved successfully.")
