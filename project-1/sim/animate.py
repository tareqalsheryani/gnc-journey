import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pendulum import simulate, L

s0 = np.array([0.0, 0.0, np.pi - 0.3, 0.0])
no_force = lambda s, t: 0.0
ts, ss, _ = simulate(s0, no_force, t_end=10.0, dt=0.02)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.0, 1.0)
ax.set_aspect("equal")
ax.grid(True)
ax.set_title("Cart-pole free swing")

cart, = ax.plot([], [], "s", markersize=25, color="steelblue")
rod, = ax.plot([], [], "-", lw=2, color="black")
bob, = ax.plot([], [], "o", markersize=15, color="crimson")

def update(i):
    x, _, theta, _ = ss[i]
    bob_x = x - L * np.sin(theta)
    bob_y = L * np.cos(theta)
    cart.set_data([x], [0])
    rod.set_data([x, bob_x], [0, bob_y])
    bob.set_data([bob_x], [bob_y])
    return cart, rod, bob

ani = animation.FuncAnimation(fig, update, frames=len(ts), interval=20, blit=True)
plt.show()