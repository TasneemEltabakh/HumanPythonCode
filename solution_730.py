import numpy as np
x = np.arange(24).reshape((2,3,4))
print("Array x:")
print(x)
print("Array y:")
y = np.arange(4)
print(y)
print("Inner of x and y arrays:")
print(np.inner(x, y))
