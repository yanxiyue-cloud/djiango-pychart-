import pandas as pd

def fouranalyze():
    df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\chartFour.csv')
    print(df)

    df['industry'] = df['industry'].astype(str)

    industrylist = list(df['industry'])
    datalist = list(df['data'])

    dict = {"industry": industrylist, "data": datalist}

    print(dict)

    return dict

if __name__ == '__main__':
    fouranalyze()