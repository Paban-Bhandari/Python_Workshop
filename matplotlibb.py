import matplotlib.pyplot as plt
import numpy as np

# Generate data points for the sine wave
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # Sine of x

# Create the line plot
plt.plot(x, y, color='green', marker='o', linestyle='-', markersize=5, label='Sine Curve')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave Plot')

# Adding a grid
plt.grid(True)

# Adding a legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
