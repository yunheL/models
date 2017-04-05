import matplotlib.pyplot as plt
import re
import sys

if len(sys.argv) != 3:
	print "ERROR: usage: python plot_loss.py <file_name> <file_name2>"
	sys.exit(2)

inputfile0 = sys.argv[1]
inputfile1 = sys.argv[2]
step_list = []
loss_list0 = []
loss_list1 = []

with open(inputfile0) as f:
	for line in f:
		m = re.search(r'step (\d+), loss = (\d+\.\d+)', line)
		if m is None:
			print("ERROR: input line format error")
			contine
		step_list.append(m.group(1))	
		loss_list0.append(m.group(2))

with open(inputfile1) as s:
	for line in s:
		p = re.search(r'step (\d+), loss = (\d+\.\d+)', line)
		if p is None:
			print("ERROR: input line format error")
			contine
		loss_list1.append(p.group(2))


plt.plot(step_list, loss_list0)
plt.plot(step_list, loss_list1)
plt.xlabel('steps')
plt.ylabel('loss')
plt.legend(['true label', 'random label'], loc='upper left')

plt.show()
