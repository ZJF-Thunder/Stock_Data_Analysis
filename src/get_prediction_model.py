import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# 忽略一切警告
import warnings
warnings.filterwarnings("ignore")

# "b-"         blue 蓝
# "g-"         green 绿
# "r-"         red 红
# "c-"         cyan 蓝绿
# "m-"         magenta 洋红
# "y-"         yellow 黄
# "b-"         black 黑
# "w-"         white 白


# 线性回归模型初态
def build_predictive_model1(df):
    df2 = df[['DATE', 'SP500']]
    next_minute = df2['SP500'].iloc[1:]  # 将next_minute等于每次下一分钟的股价
    df2 = df2.iloc[:-1, :]  # 去掉最后一行
    df2["next_minute"] = next_minute.values
    print(df2)
    print(df2.dtypes)  # 获取每一列的类型
    regressor = LinearRegression()  # 创建线性回归模型
    # 由于做回归的时候，预测器predictors必须是个DataFrame,一般它包含多个属性，
    # 而此处只有一个属性，但也不能直接使用sp500["value"]因为这是Series对象，索引应当将其放到list中。
    predictors = df2[["SP500"]]
    to_predict = df2["next_minute"]
    # 在测试集上训练线性回归模型。
    regressor.fit(predictors, to_predict)
    # 使用线性回归模型生成预测列表
    next_day_predictions = regressor.predict(predictors)  # 对未知点X做预测y，结果为数组
    print(next_day_predictions)
    accuracy = regressor.score(predictors, to_predict)
    print(accuracy)  # 对模型进行评分，结果越大越好
    df2['next_minute_predictions'] = next_day_predictions
    print(df2)

    fig1 = plt.figure(figsize=(13, 13), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig1.suptitle('Prediction model', fontsize=14, fontweight='bold')  # 设置画布名称
    plt.title("SP500 prediction")
    plt.xlabel("date")
    plt.ylabel("price")

    x = df2['DATE']
    y1 = df2['SP500']
    y2 = df2['next_minute_predictions']

    # 将预测模型数据绘制成折线图，观察预测效果
    plt.plot(x, y1, color='r', label='SP500', linewidth=2)
    plt.plot(x, y2, color='g', label='next_minute_predictions', linewidth=1.5)
    plt.plot(secondary_y=['SP500', 'next_minute_predictions'], grid=True)  # 怎样用两个不同的标度来作图
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid(True)
    plt.show()


# 线性回归模型优化
def build_predictive_model2(df):
    df2 = df[['DATE', 'SP500']]
    next_minute = df2['SP500'].iloc[1:]  # 将next_minute等于每次下一分钟的股价
    df2 = df2.iloc[:-1, :]  # 去掉最后一行
    df2["next_minute"] = next_minute.values
    print(df2)
    print(df2.dtypes)  # 获取每一列的类型
    regressor = LinearRegression()  # 创建线性回归模型
    # 由于做回归的时候，预测器predictors必须是个DataFrame,一般它包含多个属性，
    # 而此处只有一个属性，但也不能直接使用df["value"],因为这是Series对象，索引应当将其放到list中。

    train_row = int(df2.shape[0] * 0.8)
    train = df2.loc[:train_row, :]  # 测试集：占全数据的80%
    x_train = train[["SP500"]]
    y_train = train["next_minute"]

    test = df2.loc[train_row:, :]  # 训练集：占全数据的20%
    # 在训练集上训练线性回归模型。
    regressor.fit(x_train, y_train)  # 将训练集进行拟合训练模型
    print(regressor.intercept_)  # 获得截距
    print(regressor.coef_)  # 获得斜率，回归系数

    # 使用训练后的线性回归模型生成预测值数组
    predictions = regressor.predict(test[["SP500"]])  # 对未知点X做预测y，结果为数组
    print(predictions)

    # 增加列next_minute_predictions
    df2.loc[train_row:, 'next_minute_predictions'] = predictions
    df2.loc[:train_row, 'next_minute_predictions'] = train["next_minute"]
    print(df2)

    judgment = regressor.score(test[["SP500"]], predictions)
    print(judgment)  # 对模型进行评分，结果越大越好

    # fig = plt.figure(figsize=(13, 13), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    # fig.suptitle('Stock price chart', fontsize=14, fontweight='bold')  # 设置画布名称

    plt.scatter(train["SP500"], train["next_minute"])
    plt.plot(train["SP500"], regressor.predict(train[["SP500"]]), color='r')
    plt.show()

    plt.scatter(test["SP500"], test["next_minute"])
    plt.plot(test["SP500"], predictions, color='r')
    plt.show()

    fig1 = plt.figure(figsize=(13, 13), facecolor='w', edgecolor='r', frameon=True)  # 创建一个画布
    fig1.suptitle('Prediction model', fontsize=14, fontweight='bold')  # 设置画布名称
    plt.title("SP500 prediction")
    plt.xlabel("date")
    plt.ylabel("price")

    x = df2['DATE']
    y1 = df2['SP500']
    y2 = df2['next_minute_predictions']

    # 将预测模型数据绘制成折线图，观察预测效果
    plt.plot(x, y1, color='r', label='SP500', linewidth=2)
    plt.plot(x, y2, color='g', label='next_minute_predictions', linewidth=1.5)
    plt.plot(secondary_y=['SP500', 'next_minute_predictions'], grid=True)  # 怎样用两个不同的标度来作图
    plt.legend(loc=0, ncol=2)  # 设置折线图的标签
    plt.grid(True)
    plt.show()



