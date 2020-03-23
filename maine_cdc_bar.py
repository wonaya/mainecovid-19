import os,sys
import matplotlib.pyplot as plt
import numpy as np
from lxml.html import parse
os.system("wget https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml")
page= parse("coronavirus.shtml")
rows=page.xpath("//table")
col = []

plot1val = []
plot1key = []
i=0
for t in rows[0][1] :
    i+=1
    name=t.text_content()
    #print '%d:"%s"'%(i,name)
    if i==1 : 
        for x in name.split("\n")[1:-1] :
            plot1key.append(x.strip(" ").strip("\r")[:-1])
    if i==2 :
        for x in name.split("\n")[1:-1] :
            plot1val.append(int(x.strip("\r").replace(",","")))

#print plot1key, plot1val
plot2key = []
plot2name = []
plot2confirm = []
plot2pres=[]
plot2recover = []
i=0
for t in rows[1][1] :
    i+=1
    name=t.text_content()
    #print '%d:"%s"'%(i,name)
    if i == 1 :  
       for x in name.split("\n")[1:-1] : 
           plot2key.append(x.strip(" ").strip("\r").strip("\t").strip(" "))
    else :
       test = []
       plot2name.append(name.split("\n")[1].strip("\r").strip("\t").strip(" "))
       plot2confirm.append(int(name.split("\n")[2].strip("\r").strip("\t").strip(" ")))
       #if name.split("\n")[3].strip("\t").strip() :
       #    plot2pres.append(int(name.split("\n")[3].strip("\r").strip("\t").strip(" ")))
       #else : 
       #    plot2pres.append(0)
       if name.split("\n")[3].strip("\t").strip() :
           plot2recover.append(int(name.split("\n")[3].strip("\r").strip("\t").strip(" ")))
       else :
           plot2recover.append(0)
#print plot2key, plot2name , plot2confirm , plot2pres, plot2recover
#count = plot1val
#bars= (plot1key)
#y_pos = np.arange(len(bars))

#plt.bar(y_pos,count)
#plt.xticks(y_pos,bars)
#plt.show()

x = np.arange(len(plot2name))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, plot2confirm, width, label='Confirmed', color='Blue')
#rects2 = ax.bar(x         , plot2pres, width, label='Presumptive', color='Red')
rects3 = ax.bar(x, plot2recover, width, label='Recoverd', color='Yellow')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(x)
ax.set_xticklabels(plot2name)
ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
#autolabel(rects2)
autolabel(rects3)

fig.tight_layout()

plt.show()
os.system("rm -Rf coronavirus.shtml")
