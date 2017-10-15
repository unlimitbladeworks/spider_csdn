#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime  
import decimal
#根据数据动态画图
def drawBydata():
    #读取输出的txt文档
    (recordDate,y) = readData('visitorNumber.txt')
    #获取记录的日期列表范围(0,)
    x = range(len(recordDate))
    # plt.figure() 开始画图,r:红色
    #http://www.360doc.com/content/15/0113/23/16740871_440559122.shtml
    plt.plot(x,y,'ro-')
    #rotation,x轴字体旋转的角度
    plt.xticks(x, recordDate,rotation=70)
    plt.margins(0.08)
    plt.subplots_adjust(bottom=0.15)
    #设置x轴的名字
    plt.xlabel("Date")
    plt.ylabel("Visitors")
    #图的标题
    plt.title("My blog visit analysis") 
    plt.show()
    print('执行成功！') 

#读取数据
def readData(fileName):
    #以只读文件打开
    inFile = open(fileName,'r')
    #定义第一列数据为博客访问量
    visitors = []
    #第二列数据为日期
    recordDate = []
    #遍历文件每一行
    for line in inFile:
        #逗号分隔
        trainingSet = line.split(',')
        #将第一列和第二列数据拼入对应的列表中
        visitors.append(trainingSet[0])
        recordDate.append(trainingSet[1])
    inFile.close()
    return (recordDate,visitors)

if __name__ == '__main__':
    drawBydata()
