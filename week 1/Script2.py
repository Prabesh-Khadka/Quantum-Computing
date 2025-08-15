import numpy as np
import matplotlib.pyplot as plt

# Initial vector (1 + 0i)
x = np.array([1, 0])

# 90-degree rotation matrix for multiplication by i (anti-clockwise)
R = np.array([[0, -1],
              [1,  0]])

# Set up the plot
plt.figure(figsize=(6, 6))
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Colors for each step
colors = ['blue', 'red', 'green', 'orange']
labels = ['1 + 0i', 'i × (1 + 0i) = i', 'i^2 × (1 + 0i) = -1', 'i^3 × (1 + 0i) = -i']

vec = x.copy()
for i in range(4):
    plt.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color=colors[i])
    # Display vector value
    plt.text(vec[0]*1.1, vec[1]*1.1, labels[i], fontsize=10, color=colors[i])
    # Rotate vector 90° counterclockwise for next step
    vec = R @ vec

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Multiplication by i: i^2 = -1 (Counterclockwise Rotation)')
plt.show()
