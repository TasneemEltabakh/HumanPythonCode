import numpy as np 
nums = np.random.random((8,8,3))
print("Original array:")
print(nums)
print("\nExtract array of shape (6,6,3) from the said array:")
new_nums = nums[:6, :6, :]
print(new_nums)
