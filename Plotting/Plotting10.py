import matplotlib.pyplot as plt
import numpy as np

N = 3
ind = np.arange(N)
width = 0.1

#avals = [0.9608, 0.9598, 0.9557]
#avals = [0.98, 1.003, 1.005]
avals = [1.028, 1.023, 1.022]
bar1 = plt.bar(ind, avals, width, color = 'darkorange', label = 'Normal', edgecolor = 'black')

#bvals = [0.9643, 0.9601, 0.956]
#bvals = [0.9883, 1.012, 1.016]
bvals = [1.021, 1.003, 1.003]
bar2 = plt.bar(ind+width, bvals, width, color = 'royalblue', label = 'No AT-VVC Oscillations', edgecolor = "black")

#dvals = [0.9186, 0.9162, 0.9107]
#dvals = [0.9523, 0.9826, 0.9847]
dvals = [0.9799, 0.9596, 0.958]
bar3 = plt.bar(ind+width*2, dvals, width, color = 'royalblue', label = 'AT-VVC Oscillations', hatch = '/', edgecolor = "black")

#cvals = [0.9902, 0.9898, 0.9864]
#cvals = [1.014, 1.041, 1.046]
cvals = [1.048, 1.034, 1.035]
bar4 = plt.bar(ind+width*3, cvals, width, color = 'mediumpurple', label = 'No AT-VVC Rise', edgecolor = "black")

#fvals = [0.9348, 0.9321, 0.9264]
#fvals = [0.9501, 0.9785, 0.9806]
fvals = [0.9551, 0.9413, 0.9397]
bar5 = plt.bar(ind+width*4, fvals, width, color = 'mediumpurple', label = 'AT-VVC Rise', hatch = '/', edgecolor = "black")

#xvals = [0.9123, 0.9048, 0.8999]
#xvals = [0.9288, 0.9467, 0.9498]
xvals = [0.9571, 0.9339, 0.9326]
bar6 = plt.bar(ind+width*5, xvals, width, color = 'hotpink', label = 'No AT-VVC Drop', edgecolor = "black")

#qvals = [0.9342, 0.9313, 0.9257]
#qvals = [0.9631, 0.9913, 0.9934]
qvals = [0.9934, 0.9801, 0.9786]
bar7 = plt.bar(ind+width*6, qvals, width, color = 'hotpink', label = 'AT-VVC Drop', hatch = '/', edgecolor = "black")

zvals = [0, 0, 0]
bar8 = plt.bar(ind+width, zvals, width, color = 'white', label = ' ')

# line colour is blue
plt.axhline(y=1.05, color='r', linestyle='--')

# line colour is white
plt.axhline(y=0.95, color='g', linestyle='--')

plt.xlabel("Bus")
plt.ylabel('Voltage (pu)')
plt.ylim(0.85, 1.07)
plt.title("Phase C Voltages")

plt.xticks(ind+width*3,['634', '671', '675'])
#plt.figure(figsize=(1,1))
#plt.legend(handles=[bar1, bar2, bar4, bar6, bar3, bar5, bar7])
plt.legend(handles=[bar1, bar2, bar4, bar6, bar8, bar3, bar5, bar7], loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, ncol=2)
plt.tight_layout()
#plt.legend( (bar1, bar2, bar3, bar4, bar5, bar6, bar7), ('Normal', 'No VVC Oscillations Trained',
 #                                                        'VVC Oscillations Trained', 'No VVC Rise Trained',
  #                                                       'VVC Rise Trained', 'No VVC Drop Trained',
   #                                                      'VVC Drop Trained') )
plt.show()

