import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(1.0, 10.0,20)

plt.subplot(1,2,1)
plt.plot(x)

y = np.random.normal(2.0,20.0,20)

plt.subplot(1,2,2)
plt.plot(y)

plt.show()