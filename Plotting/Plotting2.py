import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import numpy as np


steps = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []
x11 = []
x12 = []
x13 = []
x14 = []
x15 = []
x16 = []
x17 = []
x18 = []
x19 = []
x20 = []
x21 = []
x22 = []
x23 = []
x24 = []
x25 = []
x26 = []
x27 = []
x28 = []
x29 = []
x30 = []
x31 = []
x32 = []
x33 = []
x34 = []
x35 = []
x36 = []
x37 = []
x38 = []
x39 = []
x40 = []
x41 = []
x42 = []
x43 = []
x44 = []
x45 = []
x46 = []
x47 = []
x48 = []
x49 = []
x50 = []
x51 = []
x52 = []
x53 = []
x54 = []
x55 = []
x56 = []
x57 = []
x58 = []
x59 = []
x60 = []
x61 = []
x62 = []
x63 = []
x64 = []
x65 = []
x66 = []
x67 = []
x68 = []
x69 = []
x70 = []
x71 = []
x72 = []
x73 = []

with open('../Load Profiles.csv', 'r') as csvfile:
	lines = csv.reader(csvfile, delimiter=',')
	for row in lines:
		steps.append(row[0])
		x1.append(float(row[1]))
		x2.append(float(row[2]))
		x3.append(float(row[3]))
		x4.append(float(row[4]))
		x5.append(float(row[5]))
		x6.append(float(row[6]))
		x7.append(float(row[7]))
		x8.append(float(row[8]))
		x9.append(float(row[9]))
		x10.append(float(row[10]))
		x11.append(float(row[11]))
		x12.append(float(row[12]))
		x13.append(float(row[13]))
		x14.append(float(row[14]))
		x15.append(float(row[15]))
		x16.append(float(row[16]))
		x17.append(float(row[17]))
		x18.append(float(row[18]))
		x19.append(float(row[19]))
		x20.append(float(row[20]))
		x21.append(float(row[21]))
		x22.append(float(row[22]))
		x23.append(float(row[23]))
		x24.append(float(row[24]))
		x25.append(float(row[25]))
		x26.append(float(row[26]))
		x27.append(float(row[27]))
		x28.append(float(row[28]))
		x29.append(float(row[29]))
		x30.append(float(row[30]))
		x31.append(float(row[31]))
		x32.append(float(row[32]))
		x33.append(float(row[33]))
		x34.append(float(row[34]))
		x35.append(float(row[35]))
		x36.append(float(row[36]))
		x37.append(float(row[37]))
		x38.append(float(row[38]))
		x39.append(float(row[39]))
		x40.append(float(row[40]))
		x41.append(float(row[41]))
		x42.append(float(row[42]))
		x43.append(float(row[43]))
		x44.append(float(row[44]))
		x45.append(float(row[45]))
		x46.append(float(row[46]))
		x47.append(float(row[47]))
		x48.append(float(row[48]))
		x49.append(float(row[49]))
		x50.append(float(row[50]))
		x51.append(float(row[51]))
		x52.append(float(row[52]))
		x53.append(float(row[53]))
		x54.append(float(row[54]))
		x55.append(float(row[55]))
		x56.append(float(row[56]))
		x57.append(float(row[57]))
		x58.append(float(row[58]))
		x59.append(float(row[59]))
		x60.append(float(row[60]))
		x61.append(float(row[61]))
		x62.append(float(row[62]))
		x63.append(float(row[63]))
		x64.append(float(row[64]))
		x65.append(float(row[65]))
		x66.append(float(row[66]))
		x67.append(float(row[67]))
		x68.append(float(row[68]))
		x69.append(float(row[69]))
		x70.append(float(row[70]))
		x71.append(float(row[71]))
		x72.append(float(row[72]))
		x73.append(float(row[73]))

x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
x4 = np.array(x4)
x5 = np.array(x5)
x6 = np.array(x6)
x7 = np.array(x7)
x8 = np.array(x8)
x9 = np.array(x9)
x10 = np.array(x10)
x11 = np.array(x11)
x12 = np.array(x12)
x13 = np.array(x13)
x14 = np.array(x14)
x15 = np.array(x15)
x16 = np.array(x16)
x17 = np.array(x17)
x18 = np.array(x18)
x19 = np.array(x19)
x20 = np.array(x20)
x21 = np.array(x21)
x22 = np.array(x22)
x23 = np.array(x23)
x24 = np.array(x24)
x25 = np.array(x25)
x26 = np.array(x26)
x27 = np.array(x27)
x28 = np.array(x28)
x29 = np.array(x29)
x30 = np.array(x30)
x31 = np.array(x31)
x32 = np.array(x32)
x33 = np.array(x33)
x34 = np.array(x34)
x35 = np.array(x35)
x36 = np.array(x36)
x37 = np.array(x37)
x38 = np.array(x38)
x39 = np.array(x39)
x40 = np.array(x40)
x41 = np.array(x41)
x42 = np.array(x42)
x43 = np.array(x43)
x44 = np.array(x44)
x45 = np.array(x45)
x46 = np.array(x46)
x47 = np.array(x47)
x48 = np.array(x48)
x49 = np.array(x49)
x50 = np.array(x50)
x51 = np.array(x51)
x52 = np.array(x52)
x53 = np.array(x53)
x54 = np.array(x54)
x55 = np.array(x55)
x56 = np.array(x56)
x57 = np.array(x57)
x58 = np.array(x58)
x59 = np.array(x59)
x60 = np.array(x60)
x61 = np.array(x61)
x62 = np.array(x62)
x63 = np.array(x63)
x64 = np.array(x64)
x65 = np.array(x65)
x66 = np.array(x66)
x67 = np.array(x67)
x68 = np.array(x68)
x69 = np.array(x69)
x70 = np.array(x70)
x71 = np.array(x71)
x72 = np.array(x72)
x73 = np.array(x73)

tick_spacing = 24



plt.plot(steps, x1)
# plt.plot(steps, x2)
# plt.plot(steps, x3)
# plt.plot(steps, x4)
# plt.plot(steps, x5)
# plt.plot(steps, x6)
# plt.plot(steps, x7)
# plt.plot(steps, x8)
# plt.plot(steps, x9)
# plt.plot(steps, x10)
# plt.plot(steps, x11)
# plt.plot(steps, x12)
# plt.plot(steps, x13)
# plt.plot(steps, x14)
# plt.plot(steps, x15)
# plt.plot(steps, x16)
# plt.plot(steps, x17)
# plt.plot(steps, x18)
# plt.plot(steps, x19)
# plt.plot(steps, x20)
# plt.plot(steps, x21)
# plt.plot(steps, x22)
# plt.plot(steps, x23)
# plt.plot(steps, x24)
# plt.plot(steps, x25)
# plt.plot(steps, x26)
# plt.plot(steps, x27)
# plt.plot(steps, x28)
# plt.plot(steps, x29)
# plt.plot(steps, x30)
# plt.plot(steps, x31)
# plt.plot(steps, x32)
# plt.plot(steps, x33)
# plt.plot(steps, x34)
# plt.plot(steps, x35)
# plt.plot(steps, x36)
# plt.plot(steps, x37)
# plt.plot(steps, x38)
# plt.plot(steps, x39)
# plt.plot(steps, x40)
# plt.plot(steps, x41)
# plt.plot(steps, x42)
# plt.plot(steps, x43)
# plt.plot(steps, x44)
# plt.plot(steps, x45)
# plt.plot(steps, x46)
# plt.plot(steps, x47)
# plt.plot(steps, x48)
# plt.plot(steps, x49)
# plt.plot(steps, x50)
# plt.plot(steps, x51)
# plt.plot(steps, x52)
# plt.plot(steps, x53)
# plt.plot(steps, x54)
# plt.plot(steps, x55)
# plt.plot(steps, x56)
# plt.plot(steps, x57)
# plt.plot(steps, x58)
# plt.plot(steps, x59)
# plt.plot(steps, x60)
# plt.plot(steps, x61)
# plt.plot(steps, x62)
# plt.plot(steps, x63)
# plt.plot(steps, x64)
# plt.plot(steps, x65)
# plt.plot(steps, x66)
# plt.plot(steps, x67)
# plt.plot(steps, x68)
# plt.plot(steps, x69)
# plt.plot(steps, x70)
# plt.plot(steps, x71)
# plt.plot(steps, x72)
# plt.plot(steps, x73)

#plt.gca().xaxis.set_major_locator(plt.MultipleLocator(10))
plt.title("Load Profile 0")
plt.xlabel("Hour")
plt.ylabel("Power (pu)")
plt.legend()
plt.grid()

plt.show()


