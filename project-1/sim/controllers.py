class PID:
    def __init__ (self, Kp, Ki, Kd, dt):
        # I need to store the kp, ki, kd and dt
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        self.running_integral=0
        self.previous_error=0
    
    def update(self, theta):
        error = 0 - theta
        self.running_integral = self.running_integral + error*self.dt
        derivative = (error - self.previous_error)/self.dt
        output = self.Kp*error + self.Ki*self.running_integral + self.Kd*derivative
        self.previous_error = error
        return output