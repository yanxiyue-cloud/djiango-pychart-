from people.analyze.chartThree import *
from pyecharts.charts import Line
from pyecharts import options as opts

def chartthree():
    data_dict = threeanalyze()
    line = Line()
    line.add_xaxis(data_dict['years'])
    # 添加y轴数据（Urban和Rural）
    line.add_yaxis("Urban",data_dict['urban_data'])
    line.add_yaxis("Rural", data_dict['rural_data'])
    line.set_global_opts(
        xaxis_opts=opts.AxisOpts(name='Year'),
        yaxis_opts=opts.AxisOpts(name='Consumption Level'),
        title_opts=opts.TitleOpts(
            title="Urban vs Rural 消费水平",
            pos_left='center',
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=30
            )
        ),
        legend_opts = opts.LegendOpts(
            pos_bottom='bottom',
            orient='horizontal'
        )
    )
    # 渲染为JSON
    json = line.dump_options_with_quotes()
    print(json)
    return json

if __name__ == '__main__':
    chartthree()
