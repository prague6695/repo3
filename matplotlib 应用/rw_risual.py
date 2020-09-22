import matplotlib.pyplot as plt 
from random_walk import RandaWalk

while True :
    #创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RandaWalk(50000)
    rw.fill_walk()
    #绘制窗口尺寸
    plt.figure(dpi=128,figsize=(10,6))
    #绘制点将图形显示出来
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)
    #突出起点和终点
    plt.scatter(0,0,c='green',s=20)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=20)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? y/n :')
    if keep_running == 'n':
        break