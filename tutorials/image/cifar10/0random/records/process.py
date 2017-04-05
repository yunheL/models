import matplotlib.pyplot as plt
import re

inputfile = "log"
step_list = []
loss_list = []

with open(inputfile) as f:
	for line in f:
		m = re.search(r'step (\d+), loss = (\d+\.\d+)', line)
		if m is None:
			print("ERROR: input line format error")
			contine
		step_list.append(m.group(1))	
		loss_list.append(m.group(2))
		#print(step_list)
		#print(loss_list)

plt.plot(step_list, loss_list)
plt.xlabel('steps')
plt.ylabel('loss')
plt.show()
