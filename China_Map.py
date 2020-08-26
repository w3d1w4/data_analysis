from pyecharts.charts import Map
from pyecharts import options as opts
import excel_reader
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType


provinceList, count = excel_reader.loadDataSetPSE()
listPSE = [[provinceList[i],count[i]] for i in range(len(provinceList))]

provinceList2, count2 = excel_reader.loadDataSetProject()
listProject = [[provinceList2[i],count2[i]] for i in range(len(provinceList2))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="工程师vs项目分布"),
    visualmap_opts=opts.VisualMapOpts(max_=50)  #最大数据范围
    )
map_1.add("工程师全国分布情况", listPSE, maptype="china")
map_1.add("项目师全国分布情况", listProject, maptype="china")
map_1.render('工程师资源分析.html')


from pyecharts.charts import Bar
from pyecharts import options as opts

engineerList,count, meanScore =excel_reader.loadDataSetEngineerScore()
bar = (
    Bar()
    .add_xaxis(engineerList)
    .add_yaxis("项目数", count)
    .add_yaxis("平均分", meanScore)
    .set_global_opts(title_opts=opts.TitleOpts(title="客户满意度"), datazoom_opts=opts.DataZoomOpts(type_='inside', range_start=100))
)
bar.render("满意度分析.html")

