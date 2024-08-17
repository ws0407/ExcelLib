import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import openpyxl


x = np.arange(0, 3 * np.pi, 0.5)
print(x)
y = np.sin(x)

plt.plot(x, y, color='green', linestyle='--', linewidth=1, marker='o', markerfacecolor='blue', markersize=10)
plt.show()

x = [1,2,3,4,5]
y = [z * z for z in x]  # y : [1, 4, 9, 16, 25]


res = {}
res['name'] = 'ws'
res['Array'] = [1,23,4]
res['dict'] = {'a':1,'b':2}

print(res)
