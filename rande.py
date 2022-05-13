#引入模块
import random as r
import time as time
import codecs
import os

#开始时间
startTime = time.localtime()
startPerfCounter = time.perf_counter()
print('程序启动的时间',time.strftime('%Y-%m-%d %H:%M:%S',startTime))

#从name.txt中读取名单
with codecs.open('name.txt','r',encoding='utf-8') as file:
    name_list=(file.read().splitlines())
    print("本轮奖池如下:\n")
    numb=len(name_list)
    print('共'+format(numb)+'人\n')
    for i in range(0,numb):
        print('{:^3}'.format(name_list[i]),end='')
        if (i+1)%10==0:
            print("\n")
        else:
            print("\t",end='')
            
print("\n")
#获取抽取人数
eggs=eval(input("请输入抽取人数"))

#初始化参数
i=0
counts={}

#设定随机次数
c=114514
print("随机114514次")

#进行随机抽取
while (i<=c):
#对随机种子进行随机化
    r.seed(r.randint(1,10000000)+r.random())
 #随机抽取 
    b=(r.choice(name_list))
#统计随机抽取次数  
    counts[b] = counts.get(b, 0) + 1
    i+=1 

#列表处理
items = list(counts.items())
items.sort (key=lambda x:x[1],reverse=True)

#打印统计结果
print("本轮结果如下：\n")
for i in range(eggs):
    b,count=items[i]

#不打印次数只打印顺序  
    print("{0:<10}\n".format(b))

#打印次数和顺序
#   print("{0:<10} {1:>5} 次\n".format(b,count))

#结束时间及时间统计
Endtime = time.perf_counter()
endPerfCounter = time.perf_counter()
totalPerf = endPerfCounter - startPerfCounter
endTime = time.localtime() 
print("程序运行总时间是:{}秒".format(totalPerf))
print('程序结束时间：',time.strftime('%Y-%m-%d %H:%M:%S',endTime))

#保持窗口
ass=input("pause")
