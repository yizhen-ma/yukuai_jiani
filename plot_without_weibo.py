import matplotlib.pyplot as plt
import csv
import math

#x轴是排名，y轴是频率
with open('无微博长恨歌.csv', 'r', encoding='ansi', newline='') as inpu:
    data = csv.reader(inpu)
    x_bcc = []
    y_bcc = []
    x_no_weibo = []
    y_no_weibo = []
    x_weibo = []
    y_weibo = []
    #测评分和频率的关系，总评分为y轴，频率是x轴
    x_zongfen = []
    y_zongfen = []
    c = 0
    for i in data:
        c += 1
        if (c == 1):
            continue
        x_bcc.append(math.log2(int(i[3])))
        y_bcc.append(math.log2(int(i[4])))
        x_no_weibo.append(math.log2(int(i[5])))
        y_no_weibo.append(math.log2(int(i[6])))
        zongfen = int(i[1]) + int(i[2])
        y_zongfen.append(zongfen)
        x_zongfen.append(int(i[3]))
        y1 = int(i[9])
        if (y1 > 0): #处理频率为0的情况
            y1 = math.log2(y1)
        y_weibo.append(y1)
        x_weibo.append(math.log(int(i[8])))
    print (len(x_bcc))
    '''
    x_bcc = map(math.log2, x_bcc)
    y_bcc = map(math.log2, y_bcc)
    x_no_weibo = map(math.log2, x_no_weibo)
    y_no_weibo = map(math.log2, y_no_weibo)
    '''
    #plt.plot([math.log2(1200), 0], [0, math.log2(1200)], label='std')
    '''
    plt.plot([10, 0], [0, 10], label='std')
    plt.scatter(x_bcc, y_bcc, label='bcc', s=5, color='red')
    plt.scatter(x_no_weibo, y_no_weibo, label='bcc无微博', s=5, color='navy')
    plt.scatter(x_weibo, y_weibo, label='weibo', s=5, color='green')
    plt.xlabel('frequency')
    plt.ylabel('ranking')
    '''
    plt.scatter(x_zongfen, y_zongfen, label='pingfen', s=5)
    plt.show()