import pandas as pd

def analyzetwo():
    df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\chartTwo.csv')
    df = df.sort_values(by='Year', ascending=True)

    df['Year'] = df['Year'].astype(str)
    df['Employment'] = df['Employment'].astype(int)
    print(type(df['Year']))
    # 初始化字典
    data_dict = {"years": [], "Primary": [], "Secondary": [], "Tertiary": []}

    # 按年份分组
    for year, group in df.groupby('Year'):
        data_dict["years"].append(year)
        # 获取每个行业的就业数据
        primary_employment = int(group[group['Industry'] == 'Primary']['Employment'].values[0])
        secondary_employment = int(group[group['Industry'] == 'Secondary']['Employment'].values[0])
        tertiary_employment = int(group[group['Industry'] == 'Tertiary']['Employment'].values[0])
        # 将数据添加到字典中
        data_dict["Primary"].append(primary_employment)
        data_dict["Secondary"].append(secondary_employment)
        data_dict["Tertiary"].append(tertiary_employment)
    print(data_dict)
    return data_dict


if __name__ == '__main__':
    analyzetwo()
