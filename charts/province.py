from people.analyze.province import *
from pyecharts.charts import Map
from pyecharts import options as opts

def chartmap():
    datalist = mapanalyze()
    map = Map()
    map.add(series_name="经济增长率", data_pair=datalist, maptype="china")
    map.set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        title_opts=opts.TitleOpts(
            title="各省份经济增长率",
            pos_left="center",
            pos_top="top",
            title_textstyle_opts=opts.TextStyleOpts(font_size=30)
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[
                {'min': 3, 'max': 4, 'color': 'lightblue'},
                {'min': 4, 'max': 6, 'color': 'skyblue'},
                {'min': 6, 'max': 8, 'color': 'blue'},
                {'min': 8, 'max': 10, 'color': 'deepskyblue'},
                {'min': 10, 'max': 11, 'color': 'royalblue'},
                {'min': 11, 'max': 12, 'color': 'mediumorchid'},
                {'min': 12, 'max': 14, 'color': 'blueviolet'},
                {'min': 14, 'color': 'darkblue'},
            ],
            orient='horizontal',
            pos_left='center'
        )
    )
    json_res = map.dump_options_with_quotes()
    print(json_res)

    return json_res
