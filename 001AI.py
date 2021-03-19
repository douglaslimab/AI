import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x2 = np.arange(1, 20)

y2 = np.random.random() * x2 + np.random.random()
plt.plot(x2, y2)
plt.plot(x2, y2, 'r--')
# plt.plot(x1, y1, 'r', x2, y2, 'b--')
plt.legend(['f1', 'f2'])
