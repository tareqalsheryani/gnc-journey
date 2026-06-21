# Milestone 2 final tuned gains: Kp=25, Ki=0, Kd=1.8
# Settles within ±0.05 rad by t=0.14s, holds through 5s.

import numpy as np
import matplotlib.pyplot as plt
from pendulum import simulate
from controllers import PID

dt = 0.001
pid = PID(Kp=25.0, Ki=0, Kd=1.8, dt=dt)

s0 = np.array([0.0, 0.0, 0.1, 0.0])
def controller(state, t):
    theta = state[2]
    return pid.update(theta)
t, states, forces = simulate(s0, controller, t_end=5.0, dt=dt)

plt.plot(t, states[:,2])
plt.xlabel("time (s)")
plt.ylabel("theta (rad)")

plt.savefig("../runs/pid_response.png", dpi=150)
plt.show()

