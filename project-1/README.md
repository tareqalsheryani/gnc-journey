# Project 1: Cart-Pole Equations of Motion

Hand derivation of the equations of motion for a pendulum on a cart.

**Method:** Newton-Euler (free body diagrams for cart and pendulum, sum of forces and moments, solved for the accelerations).

**System:**
- Cart of mass M on a frictionless track
- Pendulum of mass m, length L, angle θ from vertical
- Horizontal input force F on the cart

**Files:**
- `derivation-1.jpg` — FBDs and setup
- `derivation-2.jpg` — force/moment equations
- `derivation-3.jpg` — final EOMs

**Next:** Python simulation of the nonlinear dynamics, then linearization around the upright equilibrium for LQR control design.


Milestone #3 Ziegler-Nichols Tuning:
Applied the Ziegler-Nichols tuning method. Found ultimate gain and period as Ku=12 and Tu=4s respectively. Yielding Kp=7.2 and Ki=Kd=3.6.

Result: ZN gains failed to stabilize the pole. The response drifted slowly and never settled within the 5s window. Response drifted till -0.085 rad. The hand tuned PD controller (Kp=25, Ki=1.8) outperformed the ZN one, achieving the textbook classic overshoot then lock to zero.

**WHY**: ZN was not built for open loop unstable plants such as the inverted pendulum which is inherently unstable as it falls without control. ZN's conservative and not so aggressive gains fail to hold it up. The pole requires high proportional gain and strong damping which are the opposite of ZN.