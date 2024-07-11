from people.analyze.chartFour import *
from pyecharts.charts import Pie
from pyecharts import options as opts


def chartfour():
    dict = fouranalyze()
    pie = Pie()
    pie.add(
        series_name="2023年各产业占比",
        data_pair=[list(z) for z in zip(dict['industry'], dict['data'])],
        rosetype='radius',
        radius=['30%', '80%'],
    )
    pie.set_global_opts(
        title_opts=opts.TitleOpts(
            title="各产业占比",
            pos_left='center',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=30
            )
        ),
        legend_opts=opts.LegendOpts(orient='vertical', pos_top='18%', pos_left='1%'),
    )
    json = pie.dump_options_with_quotes()
    print(json)
    return json


if __name__ == '__main__':
    chartfour()
