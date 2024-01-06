import matplotlib.pyplot as plt
import numpy as np

N = 3
ind = np.arange(N)
width = 0.15

avals = [0.981, 0.9778, 0.9719]
#avals = [1.011, 1.041, 1.043]
#avals = [1.043, 1.029, 1.028]
bar1 = plt.bar(ind, avals, width, color = 'royalblue', label = 'No AT O`', edgecolor = "black")

bvals = [0.9342, 0.9312, 0.9257]
#bvals = [0.9631, 0.9913, 0.9934]
#bvals = [0.9934, 0.9801, 0.9786]
bar2 = plt.bar(ind+width, bvals, width, color = 'royalblue', label = 'No AT O', hatch = '/', edgecolor = "black")

xvals = [0.9672, 0.9608, 0.9546]
#xvals = [0.9956, 1.0238, 1.026]
#xvals = [0.9916, 0.9726, 0.9707]
bar3 = plt.bar(ind+width*3, xvals, width, color = 'orange', label = 'AT O`', edgecolor = "black")

yvals = [0.9211, 0.9151, 0.9091]
#yvals = [0.9482, 0.9751, 0.9772]
#yvals = [0.9444, 0.9263, 0.9245]
bar4 = plt.bar(ind+width*4, yvals, width, color='orange', hatch = '/', label = 'AT O', edgecolor = "black")



# line colour is blue
plt.axhline(y=1.05, color='r', linestyle='--')

# line colour is white
plt.axhline(y=0.95, color='g', linestyle='--')

plt.xlabel("Bus")
plt.ylabel('Voltage (pu)')
plt.ylim(0.85, 1.07)
plt.title("Phase A Voltages")

plt.xticks(ind+width*2,['634', '671', '675'])
plt.legend(handles=[bar1, bar2, bar3, bar4], loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, ncol=2)
plt.tight_layout()
#plt.legend( (bar1, bar2, bar3, bar4), ('No FDI Trained Attacked', 'No FDI Trained True', 'FDI Trained Attacked', 'FDI Trained True') )
#plt.grid()
plt.show()

