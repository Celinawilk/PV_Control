import matplotlib.pyplot as plt
import numpy as np

N = 3
ind = np.arange(N)
width = 0.25

avals = [0.9186, 0.9162, 0.9107]
#avals = [0.9523, 0.9826, 0.9847]
#avals = [0.9799, 0.9596, 0.958]
bar1 = plt.bar(ind, avals, width, color = 'darkorange')

bvals = [0.9348, 0.9321, 0.9264]
#bvals = [0.9501, 0.9785, 0.9806]
#bvals = [0.9551, 0.9413, 0.9397]
bar2 = plt.bar(ind+width, bvals, width, color = 'royalblue')

cvals = [0.9342, 0.9313, 0.9257]
#cvals = [0.9631, 0.9913, 0.9934]
#cvals = [0.9934, 0.9801, 0.9786]
bar3 = plt.bar(ind+width*2, cvals, width, color = 'mediumpurple')

# line colour is blue
plt.axhline(y=1.05, color='r', linestyle='--')

# line colour is white
plt.axhline(y=0.95, color='g', linestyle='--')

plt.xlabel("Bus")
plt.ylabel('Voltage (pu)')
plt.ylim(0.85, 1.07)
plt.title("Phase A Voltages")

plt.xticks(ind+width*2,['634', '671', '675'])
plt.legend( (bar1, bar2, bar3), ('Oscillations', 'Rise', 'Drop') )
plt.show()

