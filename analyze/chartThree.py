import pandas as pd

def threeanalyze():
    df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\chartThree.csv')
    df['Year'] = df['Year'].astype(str)
    print(type(df['Year']))

    # 分别提取Urban和Rural的数据
    urban_data = df['Urban'].tolist()
    rural_data = df['Rural'].tolist()
    data_dict = {
        'years': df['Year'].tolist(),
        'urban_data': urban_data,
        'rural_data': rural_data
    }
    print(data_dict)
    return data_dict

if __name__ == '__main__':
    threeanalyze()
