import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings  # 忽略一切警告
warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码问题
plt.rcParams['axes.unicode_minus'] = False
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# "b-"         blue 蓝
# "g-"         green 绿
# "r-"         red 红
# "c-"         cyan 蓝绿
# "m-"         magenta 洋红
# "y-"         yellow 黄
# "b-"         black 黑
# "w-"         white 白

# 分别展示每只股票的股价走势图
def get_stock_price(df):
    fig = plt.figure(figsize=(10, 10), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig.suptitle('Stock price chart', fontsize=14, fontweight='bold')  # 设置画布名称
    # ax.set_title("Apple")  # 设置子图的名称
    # ax.set_xlabel("date")  # 设置x轴名称
    # ax.set_ylabel("price")  # 设置y轴名称

    ax = fig.add_subplot(2, 2, 1)  # 创建子图坐标
    plt.title("Apple")
    plt.xlabel("date")
    plt.ylabel("price")
    # 生成折线图
    plt.plot(df['DATE'], df['NASDAQ.AAL'], color='r', label='Apple股票价格', linewidth=2)
    # sns.lineplot(df['DATE'], df['NASDAQ.AAL'], color='r', label='股票成交量', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid()

    ax2 = fig.add_subplot(2, 2, 2)  # 创建子图坐标
    plt.title("Google")  # 设置子图的名称
    plt.xlabel("date")  # 设置x轴名称
    plt.ylabel("price")  # 设置y轴名称

    # 生成折线图
    plt.plot(df['DATE'], df['NASDAQ.GOOGL'], color='b', label='Google股票价格', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid()

    ax3 = fig.add_subplot(2, 2, 3)  # 创建子图坐标
    plt.title("Facebook")  # 设置子图的名称
    plt.xlabel("date")  # 设置x轴名称
    plt.ylabel("price")  # 设置y轴名称

    # 生成折线图
    plt.plot(df['DATE'], df['NASDAQ.FB'], color='g', label='Facebook股票价格', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid()

    ax4 = fig.add_subplot(2, 2, 4)  # 创建子图坐标
    plt.title("Microsoft")  # 设置子图的名称
    plt.xlabel("date")  # 设置x轴名称
    plt.ylabel("price")  # 设置y轴名称

    # 生成折线图
    plt.plot(df['DATE'], df['NASDAQ.MSFT'], color='c', label='Microsoft股票价格', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid()
    plt.show()


# https://www.cnblogs.com/anenyang/articles/8776278.html
# 展示两只股票的股价走势对比图
def get_Compared_price(df):
    fig = plt.figure(figsize=(10, 10), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig.suptitle('Stock price chart', fontsize=14, fontweight='bold')  # 设置画布名称
    plt.title("Apple and Microsoft")
    plt.xlabel("date")
    plt.ylabel("price")

    # 设置横坐标x和两个纵坐标y1和y2
    x = df['DATE']
    y1 = df['NASDAQ.AAL']
    y2 = df['NASDAQ.MSFT']

    # 设置苹果和微软的股价对比图，展示股价变化趋势
    plt.plot(x, y1, color='r', label='Apple', linewidth=2)
    plt.plot(x, y2, color='b', label='Microsoft', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.plot(secondary_y=["AAPL", "MSFT"], grid=True)  # 怎样用两个不同的标度来作图
    plt.grid(True)
    plt.show()

# 将每个时间段的股票价格跟开始的股票价格相比较，得到股票的收益率，然后与1进行比较，反映股票的收益水平
def get_df_income(df):
    df2 = df[['DATE', 'NASDAQ.AAL', 'NASDAQ.GOOGL', 'NASDAQ.FB', 'NASDAQ.AMZN', 'NASDAQ.MSFT']]
    df3 = df[['DATE']]
    df_return = df2.apply(lambda x: x / x[0])  # 后面的时间对应的股价分别比上第一个时间对应的股价

    plt.grid(True)  # 生成网格线
    fig = plt.figure(figsize=(10, 10), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig.suptitle('Income level', fontsize=14, fontweight='bold')  # 设置画布名称
    plt.title("Stock income")
    plt.xlabel("date")
    plt.ylabel("price")

    x = df3['DATE']
    y1 = df_return['NASDAQ.AAL']
    y2 = df_return['NASDAQ.GOOGL']
    y3 = df_return['NASDAQ.FB']
    y4 = df_return['NASDAQ.AMZN']
    y5 = df_return['NASDAQ.MSFT']

    # 分别生成每只股票对应得收益率折线图，反映收益水平
    plt.plot(x, y1, color='r', label='Apple', linewidth=1.5)
    plt.plot(x, y2, color='b', label='Google', linewidth=1.5)
    plt.plot(x, y3, color='g', label='Facebook', linewidth=1.5)
    plt.plot(x, y4, color='c', label='Amazon', linewidth=1.5)
    plt.plot(x, y5, color='y', label='Microsoft', linewidth=1.5)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid(True)  # 生成网格线
    # 设置y = 1为基准线，1以上的代表收益为正，1以下代表收益为负，反映不同股票的收益情况
    plt.axhline(y=1, color="black", ls="-", linewidth=3)
    plt.show()

# 使用对数差异来表示股票价格变化  股票的百分比差异，但是不受分母的影响
def get_df_change(df):
    df2 = df[['NASDAQ.AAL', 'NASDAQ.GOOGL', 'NASDAQ.FB', 'NASDAQ.AMZN', 'NASDAQ.MSFT']]
    df3 = df[['DATE']]
    # 计算不同股价相对于第一个时刻的股价的对数差
    df_change = df2.apply(lambda x: np.log(x) - np.log(x.shift(1)))  # shift(1)将日期数据整体向下移动一格

    plt.grid(True)  # 生成网格线
    fig = plt.figure(figsize=(13, 13), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig.suptitle('Change level', fontsize=14, fontweight='bold')  # 设置画布名称

    plt.title("Stock change")
    plt.xticks(rotation=45)  # 旋转45°
    plt.xlabel("date")
    plt.ylabel("price")

    x = df3['DATE']
    y1 = df_change['NASDAQ.AAL']
    y2 = df_change['NASDAQ.GOOGL']
    y3 = df_change['NASDAQ.FB']
    y4 = df_change['NASDAQ.AMZN']
    y5 = df_change['NASDAQ.MSFT']

    plt.plot(x, y1, color='r', label='Apple', linewidth=1.5)
    plt.plot(x, y2, color='b', label='Google', linewidth=1.5)
    plt.plot(x, y3, color='g', label='Facebook', linewidth=1.5)
    plt.plot(x, y4, color='c', label='Amazon', linewidth=1.5)
    plt.plot(x, y5, color='y', label='Microsoft', linewidth=1.5)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid(True)  # 生成网格线

    # 设置y = 0为基准线，反映不同股票的收益情况
    plt.axhline(y=0, color="black", ls="-", linewidth=3)
    plt.show()



# 移动平均值
def get_df_mean(df):
    df2 = df[['DATE', 'NASDAQ.AAL', 'NASDAQ.GOOGL', 'NASDAQ.FB', 'NASDAQ.AMZN', 'NASDAQ.MSFT']]
    df3 = df[['DATE']]
    Apple = df2[['DATE', 'NASDAQ.AAL']]

    Apple = Apple.copy()
    Apple.loc[:, '移动平均股价'] = Apple['NASDAQ.AAL'].rolling(window=5).mean()  # 翻滚函数，得到移动平均值3
    Apple[['NASDAQ.AAL', '移动平均股价']].plot(subplots=True, figsize=(9, 5), grid=True)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.show()

    plt.plot(Apple['DATE'], Apple['NASDAQ.AAL'], label='实际股价', linewidth=2)
    plt.plot(Apple['DATE'], Apple['移动平均股价'], label='移动平均股价', linewidth=2)
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.show()

    # 得到实际股价与平均股价的差值的绝对值，观察偏离水平
    price = lambda x: np.fabs(x - x.mean()).mean()
    Apple['移动平均股价'].rolling(window=5).apply(price).plot(figsize=(9, 5), grid=True)
    plt.show()



