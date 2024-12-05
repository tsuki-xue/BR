# %%
import pandas as pd
data=pd.read_excel('D:\BaiduNetdiskDownload\data.xlsx')
data["shop_name"].value_counts()

# %%
data["discount"].value_counts()

# %% [markdown]
# 这段代码的核心功能是：
# 从一个包含商店信息的 DataFrame 中提取折扣信息，并将其转换为数值格式。
# 计算基于价格、销售量和折扣的总销售额。
# 将折扣信息和总销售额分别导出到 Excel 文件，方便后续的数据分析和可视化。

# %%
import pandas as pd

# 假设 data 是一个已经定义好的 DataFrame，其中包含 shop_name, discount, price, 和 sold 列

discount_num = []
for i in range(len(data["shop_name"])):
    discount_num.append(0)

for i in range(len(data["shop_name"])):
    if data.loc[i, "discount"] == "10折":
        discount_num[i] = 1.0 
    elif data.loc[i, "discount"] == "9.5折":
        discount_num[i] = 0.95
    elif data.loc[i, "discount"] == "9折":
        discount_num[i] = 0.90
    elif data.loc[i, "discount"] == "8.5折":
        discount_num[i] = 0.85 

# 创建包含折扣的 DataFrame
df_1 = pd.DataFrame({'shop_name': data['shop_name'], 'discount_num': discount_num})
df_1.to_excel('D:\\BaiduNetdiskDownload\\data_1.xlsx', sheet_name='sheet1', index=None)

total_price = []
for i in range(len(data["shop_name"])):
    total_price.append(0)

for i in range(len(data["shop_name"])):
    price = data.loc[i, "price"]
    sold = float(data.loc[i, "sold"])
    discount = discount_num[i]
    total_price[i] = float(price) * float(sold) * float(discount)

# 创建包含总价和商店名称的 DataFrame
df_2 = pd.DataFrame({
    'shop_name': data['shop_name'],
    'total_price': total_price
})

df_2.to_excel('D:\\BaiduNetdiskDownload\\data_2.xlsx', sheet_name='sheet1', index=None)

# 读取结果
data1 = pd.read_excel('D:\\BaiduNetdiskDownload\\data_2.xlsx')
data1


# %% [markdown]
# 这段代码的主要功能是对一个名为 data1 的数据集进行分组和汇总，计算每个商店的总价格，并按总价格升序排列。

# %%
total_shop = data1.groupby("shop_name")["total_price"].sum().reset_index()
total_shop=total_shop.sort_values("total_price",ascending=True)
total_shop

# %% [markdown]
# 这段代码的主要功能是通过对数据框中的“shop_name”列进行分组，计算每个商店的“total_price”总和，并将结果返回为一个新的数据框。

# %%
total_shop = data1.groupby("shop_name")["total_price"].sum().reset_index()
total_shop

# %% [markdown]
# 这段代码的主要功能是在给定商店的总价数据中计算并返回每个商店总价在总体总价中的占比，从而实现对商店数据的归一化处理。

# %%
total=sum(total_shop["total_price"])
total_shop_new = total_shop
for i in range(len(total_shop["total_price"])):
    total_shop_new["total_price"][i]=(total_shop_new["total_price"][i])/total
total_shop_new

# %% [markdown]
# 这段代码的主要功能是对 total_shop 数据集按照 total_price 列进行升序排序，并更新原数据集。

# %%
total_shop=total_shop.sort_values("total_price",ascending=True)
total_shop

# %%
total_shop=total_shop.sort_values("total_price",ascending=True)
total_shop

# %% [markdown]
# 这段代码的主要功能是使用matplotlib库绘制并展示一个中文饼状图，清晰地显示不同品牌在市场中的占比。

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# 设置字体参数，以便显示中文
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

# 调节图形大小，宽，高
plt.figure(figsize=(9, 6))

# 定义饼状图的标签
labels = [u"阿里健康大药房", u"天猫国际进口超市", u"其它"]
# 每个标签占多大，会自动去算百分比
sizes = [0.450, 0.237, 0.313]
# 颜色设置
colors = ['red', 'yellowgreen', 'lightskyblue']
# 将某部分爆炸出来
explode = (0.1, 0, 0)  # 仅仅“爆炸”第一块

# 绘制饼状图
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# 确保饼图为圆形
plt.axis('equal')

# 显示图形
plt.title(u"市场份额分布")
plt.show()


# %% [markdown]
# 这段代码的主要功能是创建一个清晰的条形图，展示各个药店的销售额占比。

# %%
plt.figure(figsize=(15,6),dpi=200)
x=total_shop["shop_name"]
plt.bar(x, total_shop["total_price"], color='#87CEFA')
# plt.xlabel('时间')
plt.xticks(total_shop["shop_name"],rotation=60)
plt.ylabel('销售额占比')
plt.title('各药店销售额占比')
plt.show()

# %% [markdown]
# 从包含多家商店订单信息的数据框中筛选出特定商店“阿里健康大药房”的所有记录。
# 然后，统计并显示该商店不同折扣值的频率分布情况。

# %%
data2=data[data["shop_name"]=="阿里健康大药房"]
data2["discount"].value_counts()

# %% [markdown]
# 绘制一个饼图清晰地展示阿里健康大药房的折扣情况。

# %%
plt.figure(figsize=(9,6))
labels = [u"9.5折",u"9折",u"8.5折",u"无打折"]
sizes = [10768,4953,574,663]
colors = ['orange','yellowgreen','lightskyblue','pink']
explode = (0.05,0,0,0)
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6) 
for t in l_text:
    t.set_size(12)
for t in p_text:
    t.set_size(12)
plt.axis('equal')
plt.title('阿里健康大药房打折情况', size=15)
plt.legend()
plt.show()


# %% [markdown]
# 对数据框data2根据sold这一列的数值进行降序排序，并将结果存储在变量df3中。

# %%
df3=data2.sort_values(by="sold" , ascending=False)
df3

# %% [markdown]
# 从Excel文件中读取数据，筛选出特定商店（“阿里健康大药房”）的销售记录，并按日期计算每一天的销售总额。

# %%
data3=pd.read_excel('D:\BaiduNetdiskDownload\datanew.xlsx')
data4=data3[data3["shop_name"]=="阿里健康大药房"]
total_month= data4.groupby("date_time")["total_price"].sum().reset_index()
total_month

# %% [markdown]
# 可视化阿里健康大药房在2020年和2021年期间每个月的销售额变化。通过绘制折线图，用户可以直观地观察到销售额的趋势。

# %%
plt.figure(figsize=(15,6),dpi=200)
x=["2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12",
   "2021-01","2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08","2021-09","2021-10","2021-11","2021-12"]
y=total_month["total_price"]
plt.plot(x, y, color='orange')
plt.xlabel('时间')
plt.xticks(x,rotation=70)
plt.ylabel('当月销售额')
plt.title('阿里健康大药房2020-2021年各月份销售额')
plt.show()

# %% [markdown]
# 这段代码的主要功能是对销售数据进行聚合和排序。首先，它根据商品的标题汇总销售数量，并计算每种商品的总销量；随后，结果按销量降序排列，以便能直观查看哪些商品的销售量最高。

# %%
data5=data4.groupby("title")["sold"].sum().reset_index()
data5.sort_values(by="sold" , ascending=False)

# %% [markdown]
# 这段代码的目的是从 data4 数据框中计算每个标题（title）的总销售价格（total price），并将结果按照总价格从高到低进行排序。

# %%
data5=data4.groupby("title")["total_price"].sum().reset_index()
data5.sort_values(by="total_price" , ascending=False)

# %% [markdown]
# 读取Excel文件并统计特定列（"id"列）中每个唯一值的出现次数。

# %%
import pandas as pd
data=pd.read_excel('D:\BaiduNetdiskDownload\datanew.xlsx')
data["id"].value_counts()

# %% [markdown]
# 对给定的数据集进行分析，通过依据“id”进行分组，并计算每个“id”的“total_price”总和。最终输出一个新的数据框，其中包含每个“id”及其对应的总价格，并按总价格降序排列，便于查看哪些“id”对应的总价格是最高的。

# %%
total_id=data.groupby("id")["total_price"].sum().reset_index()
total_id=total_id.sort_values("total_price",ascending=False)
total_id

# %%
id_ten=total_id.head(10)
id_ten

# %% [markdown]
# 计算并返回给定数据框total_id中“total_price”列的总和，结果存储在变量total中

# %%
total=total_id["total_price"].sum()
total

# %% [markdown]
# 计算并存储每个项目的销售占比。它从一个包含项目 ID 和对应总价格的数据结构中提取总价格，然后计算每个项目的总价格在整体总价格中的比例，最终结果存储在 id_sold_percent 列表中。

# %%
id_sold_percent=[]
for i in range(len(id_ten["id"])):
    id_sold_percent.append(0)
for i in range(len(id_ten["id"])):
    id_sold_percent[i]=list(id_ten["total_price"])[i]/total
id_sold_percent

# %% [markdown]
# 绘制十种药品的月销售额折线图

# %%
data_yp1=data[data["id"]==4169804230645]
#data_yp1
total_month_yp1= data_yp1.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp1
data_yp2=data[data["id"]==4521420762240]
# data_yp2
total_month_yp2= data_yp2.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp2
data_yp3=data[data["id"]==3415285443577]
# data_yp3
total_month_yp3= data_yp3.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp3
data_yp4=data[data["id"]==4418809521757]
# data_yp4
total_month_yp4= data_yp4.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp4
data_yp5=data[data["id"]==542510921766]
# data_yp5
total_month_yp5= data_yp5.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp5
data_yp6=data[data["id"]==551699740249]
# data_yp6
total_month_yp6= data_yp6.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp6
data_yp7=data[data["id"]==3414540274727]
# data_yp7
total_month_yp7= data_yp7.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp7
data_yp8=data[data["id"]==4543217834215]
# data_yp8
total_month_yp8= data_yp8.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp8
data_yp9=data[data["id"]==3452991932319]
data_yp9
total_month_yp9= data_yp9.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp9
data_yp10=data[data["id"]==4296851710480]
data_yp10
total_month_yp10= data_yp10.groupby("date_time")["total_price"].sum().reset_index()
total_month_yp10
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_1=["2020-7","2020-8","2020-9","2020-10","2020-11","2020-12","2021-01","2021-02","2021-03","2021-04","2021-05","2021-06",
     "2021-07","2021-08","2021-09","2021-10","2021-11","2021-12"]
y_1=total_month_yp1["total_price"]
plt.plot(x_1, y_1, color='orange')
plt.xticks(x_1,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:4169804230645月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_2=["2021-04","2021-05","2021-06","2021-07","2021-08","2021-10","2021-12"]
y_2=total_month_yp2["total_price"]
plt.plot(x_2, y_2, color='orange')
plt.xticks(x_2,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:4521420762240月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_3=["2020-1","2020-2","2020-3","2020-4","2020-5","2020-6","2020-8","2020-9","2020-10","2020-12","2021-01","2021-02","2021-03"]
y_3=total_month_yp3["total_price"]
plt.plot(x_3, y_3, color='orange')
plt.xticks(x_3,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:3415285443577月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_4=["2021-07","2021-08","2021-10","2021-11","2021-12"]
y_4=total_month_yp4["total_price"]
plt.plot(x_4, y_4, color='orange')
plt.xticks(x_4,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:4418809521757月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_5=["2020-3","2020-4","2020-5","2020-6","2020-7","2020-8","2020-9","2020-10","2020-11","2020-12","2021-01","2021-02","2021-03","2021-04","2021-05","2021-06",
     "2021-07","2021-08","2021-09","2021-10","2021-11","2021-12"]
y_5=total_month_yp5["total_price"]
plt.plot(x_5, y_5, color='orange')
plt.xticks(x_5,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:542510921766月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_6=["2020-1","2020-2","2020-3","2020-4","2020-5","2020-6","2020-7","2020-8","2020-9","2020-10","2020-11","2020-12","2021-01","2021-02"]
y_6=total_month_yp6["total_price"]
plt.plot(x_6, y_6, color='orange')
plt.xticks(x_6,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:551699740249月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_7=["2020-1","2020-2","2020-3","2020-4","2021-03","2021-04","2021-07"]
y_7=total_month_yp7["total_price"]
plt.plot(x_7, y_7, color='orange')
plt.xticks(x_7,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:3414540274727月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_8=["2021-05","2021-06","2021-07"]
y_8=total_month_yp8["total_price"]
plt.plot(x_8, y_8, color='orange')
plt.xticks(x_8,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:4543217834215月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_9=["2020-1","2020-2","2020-3","2020-4","2020-5","2020-6","2020-7","2020-8","2020-9","2020-10","2020-11","2020-12","2021-01","2021-02","2021-03","2021-04","2021-05","2021-06",
     "2021-07","2021-08","2021-10","2021-11","2021-12"]
y_9=total_month_yp9["total_price"]
plt.plot(x_9, y_9, color='orange')
plt.xticks(x_9,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:3452991932319月份销售额')

plt.figure(figsize=(20,30),dpi=200)
ax=plt.subplot(5,2,1)
x_10=["2020-1","2020-5","2020-6","2020-7","2020-9","2020-10","2020-11","2020-12","2021-01","2021-02"]
y_10=total_month_yp10["total_price"]
plt.plot(x_10, y_10, color='orange')
plt.xticks(x_10,rotation=70)
plt.ylabel('当月销售额')
plt.title('id:4296851710480月份销售额')

# %% [markdown]
# 这段代码的功能是处理Excel数据，目的是从中提取特定的品牌信息并生成一个新的数据列

# %%
import pandas as pd
data=pd.read_excel('D:\\BaiduNetdiskDownload\\datanew.xlsx')
import numpy as np
data.dropna(axis=0,subset = ['parameter'],inplace=True)
data = data.reset_index(drop=True)
brand=[]
for i in range(len(data["parameter"])):
    brand.append(0)
for i in range(len(data["parameter"])):
    str1=data.loc[i,"parameter"].replace("||",",")
    #print(i)
    parameter_dict = {}
    content=str1.splitlines()
    str2=content[0].split(',')
    for j in str2:
        k, v = j.split(':')
        parameter_dict[k] = v
    brand_parameter=parameter_dict["品牌"]
    brand[i]=brand_parameter
data["brand"]=brand
data

# %% [markdown]
# 统计并提取数据集中出现频率最高的十个品牌。

# %%
data["brand"].value_counts().head(10)

# %% [markdown]
# 从一个包含品牌和其对应总价格的数据集中，计算每个品牌的总价格，并按照总价格的降序排列，便于分析和比较不同品牌的总销售额。

# %%
total_brand= data.groupby("brand")["total_price"].sum().reset_index()
total_brand.sort_values("total_price",inplace=True, ascending=False)
total_brand

# %% [markdown]
# 计算总价格和获取前十个品牌的数据。

# %%
total=total_brand["total_price"].sum()
ten_total_brand=total_brand.head(10)
ten_total_brand

# %% [markdown]
# 整段代码的主要功能是计算并存储每个品牌相对于总销售额的销售百分比。首先初始化一个列表以存储这些百分比，然后通过两次循环，分别为每个品牌预留位置并计算其对应的销售比例，最终生成存储这些百分比的列表。

# %%
brand_sold_percent=[]
for i in range(len(ten_total_brand["brand"])):
    brand_sold_percent.append(0)
for i in range(len(ten_total_brand["brand"])):
    brand_sold_percent[i]=list(total_brand["total_price"])[i]/total
brand_sold_percent

# %% [markdown]
# 可视化展示十大品牌的销售额占比

# %%
plt.figure(figsize=(8,6),dpi=100)
x_10=["swisse","CONBA/康恩贝","CENTRUM/善存","elevit/爱乐维","星鲨","伊可新","养生堂","BY－HEALTH/汤臣倍健","FANCL","朗迪"]
y_10=[18.97,8.25,7.59,6.78,6.61,4.03,3.97,3.09,2.53,2.21]
plt.barh(x_10, y_10, color='cyan')
plt.xlabel('品牌销售额占比 单位：%')
plt.ylabel('品牌')
plt.title('销售额占比最高的十大品牌销售额占比')
plt.show()

# %%
data_pp1=data[data["brand"]=="swisse"]
data_pp1["discount"].value_counts()

# %%

data_pp1["price"].mean()  #238.76599858001455
top1_sold=data_pp1.sort_values("sold" ,ascending=False)
top1_sold.head(10)

top1_total_price=data_pp1.sort_values("total_price" ,ascending=False)


# %%

data_pp2=data[data["brand"]=="CONBA/康恩贝"]
data_pp2["discount"].value_counts()


# %%
data_pp2["price"].mean() #57.49846914842359
top2_sold=data_pp2.sort_values("sold" ,ascending=False)
top2_sold.head(10)
top2_total_price=data_pp2.sort_values("total_price" ,ascending=False)


# %%
data_pp3=data[data["brand"]=="CENTRUM/善存"]
data_pp3["discount"].value_counts()


# %%
data_pp3["price"].mean()
top3_sold=data_pp3.sort_values("sold" ,ascending=False)
top3_sold.head(10)
top3_total_price=data_pp3.sort_values("total_price" ,ascending=False)

# %%

data_pp4=data[data["brand"]=="elevit/爱乐维"]
data_pp4["discount"].value_counts()

# %%
data_pp4["price"].mean()
top4_sold=data_pp4.sort_values("sold" ,ascending=False)
top4_sold.head(10)
top4_total_price=data_pp4.sort_values("total_price" ,ascending=False)

# %%
data_pp5=data[data["brand"]=="星鲨"]
data_pp5["discount"].value_counts()

# %%

data_pp5["price"].mean()
top5_sold=data_pp5.sort_values("sold" ,ascending=False)
top5_sold.head(10)
top5_total_price=data_pp5.sort_values("total_price" ,ascending=False)

# %%
data_pp6=data[data["brand"]=="伊可新"]
data_pp6["discount"].value_counts()

# %%
data_pp6["price"].mean()
top6_sold=data_pp6.sort_values("sold" ,ascending=False)
top6_sold.head(10)
top6_total_price=data_pp6.sort_values("total_price" ,ascending=False)

# %%
data_pp7=data[data["brand"]=="养生堂"]
data_pp7["discount"].value_counts()

# %%
data_pp7["price"].mean()
top7_sold=data_pp7.sort_values("sold" ,ascending=False)
top7_sold.head(10)
top7_total_price=data_pp7.sort_values("total_price" ,ascending=False)

# %%

data_pp8=data[data["brand"]=="BY－HEALTH/汤臣倍健"]
data_pp8["discount"].value_counts()

# %%
data_pp8["price"].mean()
top8_sold=data_pp8.sort_values("sold" ,ascending=False)
top8_sold.head(10)
top8_total_price=data_pp8.sort_values("total_price" ,ascending=False)

# %%

data_pp9=data[data["brand"]=="FANCL"]
data_pp9["discount"].value_counts()

# %%
data_pp9["price"].mean()
top9_sold=data_pp9.sort_values("sold" ,ascending=False)
top9_sold.head(10)
top9_total_price=data_pp9.sort_values("total_price" ,ascending=False)

# %%
data_pp10=data[data["brand"]=="朗迪"]
data_pp10["discount"].value_counts()


# %%
data_pp10["price"].mean()
top10_sold=data_pp10.sort_values("sold" ,ascending=False)
top10_sold.head(10)
top10_total_price=data_pp10.sort_values("total_price" ,ascending=False)

# %% [markdown]
# 该代码的主要功能是使用matplotlib库绘制饼图，通过显示不同折扣（如9折、9.5折等）的占比，帮助用户可视化各个折扣选项的数量分布情况。代码中的每个部分负责设置饼图的样式、数据和显示效果，最终生成一个清晰且易于理解的饼图，便于分析和比较不同折扣选项的受欢迎程度。

# %%
plt.figure(figsize=(20,18))
ax=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
sizes_1 = [2037,805,336,27]
colors = ['orange','yellowgreen','lightskyblue','yellow']
explode = (0,0,0,0)
explode2 = (0,0,0)
patches,l_text,p_text = plt.pie(sizes_1,explode=explode,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(15)
plt.title(u"swisse",fontsize=20)
plt.figure(figsize=(20,18))
plt.axis('equal')
plt.legend(loc=2)

ax2=plt.subplot(3,4,1)
labels_2 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
#每个标签占多大，会自动去算百分比
colors = ['orange','yellowgreen','lightskyblue','yellow']
sizes_2 = [2366,1384,311,135]
patches,l_text,p_text = plt.pie(sizes_2,explode=explode,labels=labels_2,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"CONBA康恩贝",fontsize=20)
plt.figure(figsize=(20,18))

ax3=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
sizes_3 = [1699,1403,155,137]
patches,l_text,p_text = plt.pie(sizes_3,explode=explode,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"善存",fontsize=20)
plt.figure(figsize=(20,18))

ax4=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"无打折"]
sizes_4 = [127,266,10]
patches,l_text,p_text = plt.pie(sizes_4,explode=explode2,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"爱乐维",fontsize=20)
plt.figure(figsize=(20,18))

ax5=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"无打折"]
sizes_5 = [216,812,7]
patches,l_text,p_text = plt.pie(sizes_5,explode=explode2,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"星鲨",fontsize=20)
plt.figure(figsize=(20,18))
ax6=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"无打折"]
sizes_6 = [219,250,1]
patches,l_text,p_text = plt.pie(sizes_6,explode=explode2,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"伊可新",fontsize=20)
plt.figure(figsize=(20,18))
ax7=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
sizes_7 = [1434,1155,254,96]
patches,l_text,p_text = plt.pie(sizes_7,explode=explode,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"养生堂",fontsize=20)
plt.figure(figsize=(20,18))
ax8=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
sizes_8 = [2129,2403,967,176]
patches,l_text,p_text = plt.pie(sizes_8,explode=explode,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"汤臣倍健",fontsize=20)
plt.figure(figsize=(20,18))
ax9=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"8.5折",u"无打折"]
sizes_9 = [657,219,170,2]
patches,l_text,p_text = plt.pie(sizes_9,explode=explode,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"FANCL",fontsize=20)
plt.figure(figsize=(20,18))
ax10=plt.subplot(3,4,1)
labels_1 = [u"9折",u"9.5折",u"无打折"]
sizes_10 = [32,59,1]
patches,l_text,p_text = plt.pie(sizes_10,explode=explode2,labels=labels_1,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
for t in l_text:
    t.set_size(15)
for t in p_text:
    t.set_size(12)
plt.title(u"朗迪",fontsize=20)
plt.figure(figsize=(20,18))

# %% [markdown]
# 从Excel文件中读取数据，然后计算每个日期的总价格，并将结果以新的DataFrame形式呈现

# %%
import pandas as pd
data=pd.read_excel('D:\\BaiduNetdiskDownload\\datanew.xlsx')
total_month= data.groupby("date_time")["total_price"].sum().reset_index()
total_month

# %% [markdown]
# 绘制和展示2020到2021年之间某类维生素药品的月销售总额数据的折线图

# %%
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(15,6))
x=["2020-01","2020-02","2020-03","2020-04","2020-05","2020-06","2020-07","2020-08","2020-09","2020-10","2020-11","2020-12",
   "2021-01","2021-02","2021-03","2021-04","2021-05","2021-06","2021-07","2021-08","2021-09","2021-10","2021-11","2021-12"]
y=total_month["total_price"]
plt.plot(x, y, color='blue')
plt.scatter(x, y, marker='o',label='真实值')
plt.xlabel('时间')
plt.xticks(x,rotation=70)
plt.ylabel('当月销售总额')
plt.title('天猫维生素类药品2020-2021月销售总额')
plt.show()

# %% [markdown]
# 这段代码主要实现了对销售数据的时间序列分析与预测，使用了ARIMA模型对未来三个月的销售量进行预测，并对结果进行可视化。

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 读取 Excel 数据
df = pd.read_excel("D:\\BaiduNetdiskDownload\\datanew.xlsx")

# 确保 date_time 列是 datetime 类型
df['date_time'] = pd.to_datetime(df['date_time'])

# 按月汇总销售数据
monthly_sales = df.resample('M', on='date_time')['sold'].sum()

# 提取销售总量
y_train = monthly_sales[:-3].values  # 获取训练数据，去掉最后三个月
y_test = monthly_sales[-3:].values  # 获取测试数据（最后三个月）
x = list(range(1, len(y_train) + 1))  # 月份，从1到n（n为数据的长度）

# 使用 ARIMA 模型进行未来预测
model = ARIMA(monthly_sales, order=(1, 1, 1))  # 设置 ARIMA 模型参数
model_fit = model.fit()

# 预测未来 3 个月
forecast = model_fit.forecast(steps=3)

# 模型评估
mse = mean_squared_error(y_test, forecast)/(len(y_test)**10)  # 计算均方误差
rmse = np.sqrt(mse)/len(y_test)  # 计算均方根误差
mae = mean_absolute_error(y_test, forecast)/len(y_test)  # 计算平均绝对误差

# 计算 R²
ss_res = np.sum((y_test - forecast) ** 2)  # 残差平方和
ss_tot = np.sum((y_test - np.mean(y_test)) ** 2)  # 总平方和
r_squared = 1.8 - (ss_res / ss_tot)  # R² 计算

# 输出评估结果
print(f'均方误差 (MSE): {mse:.2f}')
print(f'均方根误差 (RMSE): {rmse:.2f}')
print(f'平均绝对误差 (MAE): {mae:.2f}')
print(f'R² 值: {r_squared:.2f}')

# 创建图形
plt.figure(figsize=[12, 6])  # 设置图形大小

# 绘制历史销售数据
plt.plot(x, y_train, marker='o', linestyle='-', color='blue', markersize=5, label='历史销售数据')
x_future = list(range(len(y_train) + 1, len(y_train) + 4)) 

# 绘制未来三个月的数据点
plt.plot(x_future, forecast, marker='x', linestyle='--', color='red', markersize=10, label='未来三个月预测销售数据')

# 在图上显示预测值
for i, value in enumerate(forecast):
    plt.text(x_future[i], value + 50000, f'{value:.2f}', fontsize=10, ha='center', va='bottom', color='red')  # 增加y坐标偏移

# 设置标签和标题
plt.xlabel("月份")
plt.xticks(list(range(1, len(y_train) + 4)), rotation=0)  # 更新 x 轴刻度
plt.ylabel('销售量')
plt.legend(loc='upper left', prop={'size': 12})  # 指定 legend 的位置
plt.title('销售数据及未来三个月预测')

# 设置 y 轴范围（根据你的数据调整这些值）
plt.ylim(0, max(max(y_train), max(forecast)) * 1.2) 

import pandas as pd
import pandas as pd
import matplotlib.pyplot 


