import pymongo
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

#链接pymongo
client = pymongo.MongoClient("localhost",27017)
db = client['FangTX']
table = db['bjzufang']
#读取数据
data = pd.DataFrame(list(table.find()))
#选取要展示的项目
data = data[['address','price']]

x = []
y = []

for i,j in data["address","price"]:
	x.append(i)
	j.append(int(j))


import pygal


#对结果进行可视化
hist = pygal.Bar()

hist.title = "北京租房"
hist.title = "北京租房"
hist.x_title = "address"
hist.y_title = y

hist.add(x,y)
hist.render_to_file('die_visual.svg') 