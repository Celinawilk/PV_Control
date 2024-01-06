import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import numpy as np


steps1 = []
mean_11 = []
std_11 = []
mean_21 = []
std_21 = []

steps2 = []
mean_12 = []
std_12 = []
mean_22 = []
std_22 = []

steps3 = []
mean_13 = []
std_13 = []
mean_23 = []
std_23 = []

steps4 = []
mean_14 = []
std_14 = []
mean_24 = []
std_24 = []


with open('../VVC_Normal.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps1.append(row[0])
		mean_11.append(float(row[1]))
		std_11.append(float(row[2]))
		mean_21.append(float(row[3]))
		std_21.append(float(row[4]))

with open('../VVC_Oscillations.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps2.append(row[0])
		mean_12.append(float(row[1]))
		std_12.append(float(row[2]))
		mean_22.append(float(row[3]))
		std_22.append(float(row[4]))

with open('../VVC_Rise.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps3.append(row[0])
		mean_13.append(float(row[1]))
		std_13.append(float(row[2]))
		mean_23.append(float(row[3]))
		std_23.append(float(row[4]))

with open('../VVC_Drop.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps4.append(row[0])
		mean_14.append(float(row[1]))
		std_14.append(float(row[2]))
		mean_24.append(float(row[3]))
		std_24.append(float(row[4]))

mean_11 = np.array(mean_11)
std_11 = np.array(std_11)
mean_21 = np.array(mean_21)
std_21 = np.array(std_21)

mean_12 = np.array(mean_12)
std_12 = np.array(std_12)
mean_22 = np.array(mean_22)
std_22 = np.array(std_22)

mean_13 = np.array(mean_13)
std_13 = np.array(std_13)
mean_23 = np.array(mean_23)
std_23 = np.array(std_23)

mean_14 = np.array(mean_14)
std_14 = np.array(std_14)
mean_24 = np.array(mean_24)
std_24 = np.array(std_24)

tick_spacing = 24

# plt.plot(steps1, mean_11, 'b-', label='Mean A2C')
# plt.fill_between(steps1, mean_11 - std_11, mean_11 + std_11, color='b', alpha=0.2)
# plt.plot(steps1, mean_21, 'r-', label='Mean PPO')
# plt.fill_between(steps1, mean_21 - std_21, mean_21 + std_21, color='r', alpha=0.2)
# plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
# plt.title("VVC Normal Training Rewards")
# plt.xlabel("Time Steps")
# plt.ylabel("Cumulative Rewards")
# plt.legend()
# plt.grid()

# plt.plot(steps2, mean_12, 'b-', label='Mean A2C')
# plt.fill_between(steps2, mean_12 - std_12, mean_12 + std_12, color='b', alpha=0.2)
# plt.plot(steps2, mean_22, 'r-', label='Mean PPO')
# plt.fill_between(steps2, mean_22 - std_22, mean_22 + std_22, color='r', alpha=0.2)
# plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
# plt.title("VVC Oscillations Training Rewards")
# plt.xlabel("Time Steps")
# plt.ylabel("Cumulative Rewards")
# plt.legend()
# plt.grid()

# plt.plot(steps3, mean_13, 'b-', label='Mean A2C')
# plt.fill_between(steps3, mean_13 - std_13, mean_13 + std_13, color='b', alpha=0.2)
# plt.plot(steps3, mean_23, 'r-', label='Mean PPO')
# plt.fill_between(steps3, mean_23 - std_23, mean_23 + std_23, color='r', alpha=0.2)
# plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
# plt.title("VVC Rise Training Rewards")
# plt.xlabel("Time Steps")
# plt.ylabel("Cumulative Rewards")
# plt.legend()
# plt.grid()


plt.plot(steps1, mean_11, 'b-', label='Mean VVC Normal')
plt.fill_between(steps1, mean_11 - std_11, mean_11 + std_11, color='b', alpha=0.2)
plt.plot(steps2, mean_12, 'r-', label='Mean VVC Oscillations')
plt.fill_between(steps2, mean_12 - std_12, mean_12 + std_12, color='r', alpha=0.2)
plt.plot(steps3, mean_13, 'g-', label='Mean VVC Rise')
plt.fill_between(steps3, mean_13 - std_13, mean_13 + std_13, color='g', alpha=0.2)
plt.plot(steps4, mean_14, 'm-', label='Mean VVC Drop')
plt.fill_between(steps4, mean_14 - std_14, mean_14 + std_14, color='m', alpha=0.2)
#plt.plot(steps4, mean_24, 'r-', label='Mean PPO')
#plt.fill_between(steps4, mean_24 - std_24, mean_24 + std_24, color='r', alpha=0.2)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
plt.title("VVC Training Rewards")
plt.xlabel("Time Steps")
plt.ylabel("Cumulative Rewards")
plt.legend()
plt.grid()

plt.show()


