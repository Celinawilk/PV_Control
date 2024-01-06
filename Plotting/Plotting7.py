import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import numpy as np


steps1 = []
mean_11 = []
std_11 = []
mean_21 = []
std_21 = []


with open('../FDI.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps1.append(row[0])
		mean_11.append(float(row[1]))
		std_11.append(float(row[2]))
		mean_21.append(float(row[3]))
		std_21.append(float(row[4]))


mean_11 = np.array(mean_11)
std_11 = np.array(std_11)
mean_21 = np.array(mean_21)
std_21 = np.array(std_21)


tick_spacing = 24

plt.plot(steps1, mean_11, 'b-', label='Mean No FDI')
plt.fill_between(steps1, mean_11 - std_11, mean_11 + std_11, color='b', alpha=0.2)
plt.plot(steps1, mean_21, 'r-', label='Mean FDI')
plt.fill_between(steps1, mean_21 - std_21, mean_21 + std_21, color='r', alpha=0.2)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
plt.title("FDI Training Rewards")
plt.xlabel("Time Steps")
plt.ylabel("Cumulative Rewards")
plt.legend()
plt.grid()

plt.show()


