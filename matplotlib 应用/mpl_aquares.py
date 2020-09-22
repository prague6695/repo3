import matplotlib.pyplot as plt

input_values =  [1,2,3,4,5]
sqares = [1,4,9,16,25]
plt.plot(input_values,sqares,linewidth=5)

plt.title('square Numbers',fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('square of value',fontsize=14)

plt.tick_params(axis='both',labelsize=14)
plt.show()