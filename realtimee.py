import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    li = [random.randint(1, 50) for _ in range(4)]
    plt.bar([1, 2, 3, 4], li)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("Animate")

ani = animation.FuncAnimation(fig, animate, frames=100, interval=1000, blit=False)
plt.show()
