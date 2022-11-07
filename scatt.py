from matplotlib import pyplot
from matplotlib import font_manager
import random
myfont=font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")
pyplot.figure(figsize=(12,6))
y_3=[random.randint(5,21) for i in range(31)]#3月气温
y_10=[random.randint(10,26) for j in range(31)]#10月气温
x_3=range(1,32)#1-31天
x_10=range(32,63)
pyplot.scatter(x_3,y_3,label="3月",s=100)
pyplot.scatter(x_10,y_10,label="10月")
x_3label=["3月{}日".format(k) for k in range(1,32)]
x_10label=["10月{}日".format(l) for l in range(1,32)]
x_label=x_3label+x_10label
y_label=["{}℃".format(g) for g in range(5,26,3)]
pyplot.xticks(range(1,63,4),x_label[::4],fontproperties=myfont,rotation=45)
pyplot.yticks(range(5,26,3),y_label,fontproperties=myfont)
pyplot.xlabel("时间",fontproperties=myfont)
pyplot.ylabel("温度",fontproperties=myfont)
pyplot.title("3/10月",fontproperties=myfont)
pyplot.legend(prop=myfont,loc="lower right")
pyplot.show()
