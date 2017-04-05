import matplotlib.pyplot as plt
import re
import sys

if len(sys.argv) != 2:
	print "ERROR: usage: python plot_precision.py <file_name>"
	sys.exit(2)

inputfile = sys.argv[1]
random_list = []
precision_list = []

with open(inputfile) as f:
	for line in f:
		m = re.search(r'(\d+\.\d+)_precision', line)
		p = re.search(r'@ 1 = (\d+\.\d+)', line)
		if p == None:
			random_list.append(m.group(1))
		else: 
			precision_list.append(p.group(1))

		print random_list
		print precision_list

plt.plot(random_list, precision_list)
plt.xlabel('corruption rate')
plt.ylabel('precision @ 16k steps')

plt.show()
