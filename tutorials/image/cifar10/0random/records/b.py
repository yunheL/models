import sys
import matplotlib.pyplot as plt


a = map(lambda l: float(l.strip()), sys.stdin)
print(a)
plt.plot(a)
plt.ylabel('some numbers')
plt.show()



