'''
我发现微博可能会扰乱语块（诗句）流行程度，所以做一份新的表格，
筛除掉微博统计，然后看看每一句话在有微博和没有微博的情况下排名
出现的变动幅度。

一共13列，第2列是石老师的评分，第4列是林嘉妮的评分，
第8列是微博，第13列是包括微博的总数（BCC）
长恨歌全文60句，120行
'''

import csv

def revert(dic2list):  #revert each tuple in the list of dictionary items
     #dic.items() is not a deep copy. It is a reference
    res = []
    for j in dic2list:
        tpl = (j[1], j[0])
        res.append(tpl)
    return res  #returns the reverted list of tuples

def sort_freq(dic2list):  #sort the resulted list from revert(). the list is sorted by frequency of the sentence
    res = sorted(dic2list, reverse=True)
    return res

def ranking(n, lst2):  #returns the ranking of a sentence in lst2
    c = 0
    while (lst2[c][0] != n):
        c += 1
    return (c + 1)


freq_weibo = {}   #每行的微博频率
freq_no_weibo = {}    #每行包括不微博的总频率
freq_bcc = {}    #每行包括微博的总频率
sen = []         #储存每行是哪句诗
shi = {}
lin = {}
with open("freq_changhenge_utf8.csv", 'r', newline='', encoding='utf-8') as freq_changhenge:
    original = csv.reader(freq_changhenge)  #13 attributes
    c = 0
    for i in original:
        if (c == 0):
            c += 1
            continue
        elif (c > 120):
            break
        sen.append(i[2])
        shi[c - 1] = int(i[1])
        lin[c - 1] = int(i[3])
        freq_weibo[c - 1] = int(i[7])
        freq_bcc[c - 1] = int(i[12])
        freq_no_weibo[c - 1] = int(i[12]) - int(i[7])
        #print("微博： " + i[7] + "  bcc:  " + i[12])
        c += 1

weibo_sorted = revert(sort_freq(revert(freq_weibo.items())))
no_weibo_sorted = revert(sort_freq(revert(freq_no_weibo.items())))
bcc_sorted = revert(sort_freq(revert(freq_bcc.items())))

with open("无微博长恨歌.csv", 'w', encoding='ansi', newline='') as writerfile:
    out = csv.writer(writerfile)
    #out.writerow(['原句', 'bcc总排名', '除去微博排名'])
    out.writerow(['原句', '分（石）', '分（林）', 'bcc总排名', 'bcc频率', '无微博总排名', '无微博总频率', '排名升降', '微博排名', '微博频率'])
    c = 0
    for i in bcc_sorted:
        c += 1
        num = i[0]
        no_weibo_rank = ranking(num, no_weibo_sorted)
        weibo_rank = ranking(num, weibo_sorted)
        out.writerow([sen[num], shi[num], lin[num], c, i[1], no_weibo_rank, freq_no_weibo[num], c - no_weibo_rank, weibo_rank, freq_weibo[num]])

print (len(freq_weibo))