import pandas as pd


def mapanalyze():
    rk_df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\provincegdp.csv')
    sf_df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\shengfen.csv')
    sf_list = list(sf_df['name'])
    groupby_df = rk_df.groupby('name')
    print(list(groupby_df))
    datalist = []
    for p in sf_list:
        df = groupby_df.get_group(p)
        s = df['data'].pct_change()*10
        print(s)
        data = round(list(s)[1], 2)
        t = (p, data)
        datalist.append(t)
    print(datalist)
    return datalist
if __name__ == '__main__':
    analyze()
