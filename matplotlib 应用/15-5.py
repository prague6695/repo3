import matplotlib.pyplot as plt 
from random_walk import RandaWalk

while True :
    #创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RandaWalk(5000)
    rw.fill_walk()
    #绘制窗口尺寸
    plt.figure(dpi=128,figsize=(10,6))
    #绘制点将图形显示出来
    
    plt.plot(rw.x_values,rw.y_values,linewidth=1)
    #突出起点和终点
    plt.plot(0,0,c='green')
    plt.plot(rw.x_values[-1],rw.y_values[-1],c='red')
    plt.show()


    keep_running = input('Make another walk? y/n :')
    if keep_running == 'n':
        break