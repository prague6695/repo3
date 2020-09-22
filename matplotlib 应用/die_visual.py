from die import Die
import pygal
#创建两个筛子
die_1= Die()
die_2= Die()
results=[]
for roll_num in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
#分析结果
frequencies = []
max_result = die_1.num_sides+die_2.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#对结果进行可视化
hist = pygal.Bar()

hist.title = 'tesults of rolling one D6 1000 times'
hist.x_lables = ['2','3','4','5','6','7','8','9','11','10','12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Rrsult'

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')