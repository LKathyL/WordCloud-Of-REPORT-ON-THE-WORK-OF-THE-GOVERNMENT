import jieba
import wordcloud
from scipy.misc import imread

#打开文件
f = open("report.txt", 'r', encoding = 'utf-8')
t = f.read()
f.close()
#删除文本中的特殊符号
for ch in '!"#$%&()*+，。-.、“”/:;<=>?@[\\]^_‘{|}~':
        t = t.replace(ch, " ") 

#分词
ls = jieba.lcut(t)

#统计词频
count = {}
for i in ls:
	count[i] = count.get(i,0)+1
counts = list(count.items())
counts.sort(key = lambda x:x[1], reverse = True)

#取出现次数最多的前30个词汇做输入
li = []
for i in range(30):
	item,_ = counts[i]
	li.append(item)
txt = " ".join(li)

#生成词汇云图片
mask = imread('star.png')
w = wordcloud.WordCloud(width = 1000, height = 700, background_color = 'white', mask = mask, font_path = '/System/Library/Fonts/Hiragino Sans GB W3.ttc')
w.generate(txt)
w.to_file('wc.png')
