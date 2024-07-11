import pandas as pd

def analyzeone():
    df = pd.read_csv('D:\\desktop\\subjectCode\\shixun\\people\\people\\spider\\chartOne.csv')
    df = df.sort_values(by='year', ascending=True)

    df['year'] = df['year'].astype(str)

    yearlist = list(df['year'])
    datalist = list(df['data'])

    dict = {"year": yearlist, "data": datalist}

    print(dict)

    return dict

if __name__ == '__main__':
    analyzeone()