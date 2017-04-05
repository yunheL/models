import matplotlib.pyplot as plt
import re
import sys


random_list = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
time_list = [900, 3090, 820, 930, 880, 3070]


plt.plot(random_list, time_list)
plt.xlabel('corruption rate')
plt.ylabel('steps to reach loss = 2.50')

plt.show()
