import numpy as np

x = np.sin(np.pi / 2)  # 1.0

arr = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
x = np.sin(arr)  # [1.         0.8660254  0.70710678 0.58778525]

# radians to degrees
arr = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
x = np.rad2deg(arr)  # [ 90. 180. 270. 360.]

# inverse sin / finding angle in radian
x = np.arcsin(1.0)
# inverse sin in array
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)

# hypotenues
base, perp = 3, 4
x = np.hypot(base, perp)  # 5.0

print(x)
