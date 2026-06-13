import numpy as np
import matplotlib.pyplot as plt
from pendulum import simulate, energy

# Pendulum starts near the bottom (theta = pi is straight down)
# perturbed by 0.3 rad. No force applied — pure free swing.
s0 = np.array([0.0, 0.0, np.pi - 0.3, 0.0])
no_force = lambda s, t: 0.0

ts, ss, _ = simulate(s0, no_force, t_end=10.0, dt=0.001)
E = np.array([energy(s) for s in ss])

fig, axes = plt.subplots(2, 1, figsize=(8, 6))
axes[0].plot(ts, ss[:, 2])
axes[0].set_ylabel("theta (rad)")
axes[0].set_title("Free swing — pendulum angle")
axes[0].grid(True)

axes[1].plot(ts, E)
axes[1].set_ylabel("Total energy (J)")
axes[1].set_xlabel("time (s)")
axes[1].set_title("Energy drift")
axes[1].grid(True)

plt.tight_layout()
plt.savefig("../runs/milestone-1-energy.png", dpi=120)
plt.show()

drift_pct = (E[-1] - E[0]) / E[0] * 100
print(f"Energy drift over 10s: {drift_pct:.4f}%")
print(f"Initial energy: {E[0]:.6f} J")
print(f"Final energy:   {E[-1]:.6f} J")