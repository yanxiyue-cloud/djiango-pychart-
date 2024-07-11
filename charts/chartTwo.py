from people.analyze.chartTwo import *
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker

def charttwo():
    data_dict = analyzetwo()
    print(data_dict)
    bar = Bar()

    bar.add_xaxis(data_dict["years"])

    print(Faker.values())


    bar.add_yaxis("Primary", data_dict['Primary'])
    bar.add_yaxis("Secondary", data_dict['Secondary'])
    bar.add_yaxis("Tertiary", data_dict['Tertiary'])

    print(data_dict['Secondary'])

    bar.set_global_opts(
        # legend_opts=opts.LegendOpts(is_show=False),
        legend_opts=opts.LegendOpts(
            pos_bottom='bottom',
            orient='horizontal'
        ),
        title_opts=opts.TitleOpts(
            title="各行业就业人数",
            pos_left='center',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=30
            )
        ),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        yaxis_opts=opts.AxisOpts(name='Employment'),
    )


    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=True),
    )


    json = bar.dump_options_with_quotes()
    print(json)
    return json

if __name__ == '__main__':
    charttwo()
