import numpy as np

# Convention: theta measured from upward vertical.
# Positive theta tilts bob to the LEFT (bob_x = x - L sin θ, bob_y = +L cos θ).
# theta = 0  → upright (unstable equilibrium)
# theta = π  → hanging down (stable equilibrium)

# Physical constants — tweak later if you want
m1 = 1.0      # cart mass (kg)
m2 = 0.1      # pendulum mass (kg)
L = 0.5      # pendulum length (m)
g = 9.81     # gravity (m/s^2)

def dynamics(s, F):
    """Continuous-time dynamics. Returns ds/dt given state s and force F."""
    x, x_dot, theta, theta_dot = s
    sin_t, cos_t = np.sin(theta), np.cos(theta)
    denom = m1 + m2 * sin_t**2

    x_ddot = (F - m2*L*sin_t*theta_dot**2 + m2*g*sin_t*cos_t) / denom
    theta_ddot = (F*cos_t - m2*L*theta_dot**2*sin_t*cos_t + (m1+m2)*g*sin_t) / (L*denom)

    return np.array([x_dot, x_ddot, theta_dot, theta_ddot])

def rk4_step(s, F, dt):
    """Single RK4 step."""
    k1 = dynamics(s, F)
    k2 = dynamics(s + 0.5*dt*k1, F)
    k3 = dynamics(s + 0.5*dt*k2, F)
    k4 = dynamics(s + dt*k3, F)
    return s + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

def simulate(s0, controller, t_end, dt):
    """Run sim from s0 for t_end seconds. controller(s, t) -> F."""
    n_steps = int(t_end / dt)
    ts = np.linspace(0, t_end, n_steps+1)
    ss = np.zeros((n_steps+1, 4))
    Fs = np.zeros(n_steps+1)
    ss[0] = s0
    for i in range(n_steps):
        F = controller(ss[i], ts[i])
        Fs[i] = F
        ss[i+1] = rk4_step(ss[i], F, dt)
    return ts, ss, Fs

def energy(s):
    """Total mechanical energy. Useful for validating the integrator."""
    x, x_dot, theta, theta_dot = s
    # KE: cart + bob
    bob_vx = x_dot - L*np.cos(theta)*theta_dot
    bob_vy = -L*np.sin(theta)*theta_dot
    KE = 0.5*m1*x_dot**2 + 0.5*m2*(bob_vx**2 + bob_vy**2)
    # PE: take pivot height as zero
    PE = m2*g*L*np.cos(theta)
    return KE + PE