from people.analyze.chartOne import *
from pyecharts.charts import Bar
from pyecharts import options as opts

def chartone():
    dict = analyzeone()
    bar = Bar()
    bar.add_xaxis(dict['year'])
    bar.add_yaxis(series_name="GDP", y_axis=dict['data'])
    bar.set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title="近10年GDP变化",
            pos_left='center',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=30
            )
        ),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        yaxis_opts=opts.AxisOpts(name='GDP'),
    )
    bar.set_series_opts(
        itemstyle_opts=opts.ItemStyleOpts(
            color="#91CC75"
        )
    )
    json = bar.dump_options_with_quotes()
    print(json)
    return json


if __name__ == '__main__':
    chartone()
