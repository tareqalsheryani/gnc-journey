# Milestone 2 final tuned gains: Kp=25, Ki=0, Kd=1.8
# Settles within ±0.05 rad by t=0.14s, holds through 5s.
# Conclusion: Ku = 12, Tu = 4, and "ZN underperforms hand-tuned on this open loop unstable system"

import numpy as np
import matplotlib.pyplot as plt
from pendulum import simulate
from controllers import PID

dt = 0.001
pid = PID(Kp=7.2, Ki=3.6, Kd=3.6, dt=dt)

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



# Second run for the hand tuned gains

pid_hand = PID(Kp=25, Ki=0, Kd=1.8, dt=dt)
def controller_hand(state, t):
    theta=state[2]
    return pid_hand.update(theta)
t, states_hand, forces = simulate(s0, controller_hand, t_end=5.0, dt=dt)



plt.plot(t, states[:,2], label='Ziegler-Nichols (Kp=7.2, Ki=3.6, Kd=3.6)')
plt.plot(t, states_hand[:,2], label='Hand-tuned (Kp=25, Kd=1.8)')
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.xlabel("Time (s)")
plt.ylabel('theta (rad)')
plt.legend()
plt.savefig("../runs/zn_vs_hand.png", dpi=150)
plt.show()