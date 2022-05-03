grav_const = 6.67430 * (10**(-11))

class celestial_body:
    def __init__(self, m, r, ang_vel):
        self.m = m # mass
        self.r = r # radius
        self.ang_vel = ang_vel
        self.tan_vel = ang_vel * r
        self.mu = grav_const * m # standard grav. param.

    def get_tan_vel_at(self, h):
        return self.ang_vel * (self.r + h)

class elevator:
    def __init__(self, body, h, A, mtl):
        self.body = body # the planet the elevator is on
        self.h = h # height
        self.A = A # area parallel to the body surface (a function)
        self.mtl = mtl # material the elevator is mainly made out of

    def get_A_at(self, h):
        return self.A(h)

    def get_gravitational_pull(self, hl, hh):
        weight = 0
        dh = (hh - hl)/1000
        for i in range(1000):
            hi = hl + i * dh
            A = self.get_A_at(hi)
            V = dh * A
            dm = V * self.mtl.get_density()
            dw = (self.body.mu * dm) / ((self.body.r + hi)**(2))
            weight += dw

        return weight

    def get_inertial_pull(self, hl, hh):
        inertial_pull = 0
        dh = (hh - hl)/1000
        for i in range(1000):
            hi = hl + i * dh
            A = self.get_A_at(hi)
            V = dh * A
            dm = V * self.mtl.get_density()
            vel = self.body.get_tan_vel_at(hi)
            dpull = (dm * vel**2)/(self.body.r + hi)
            inertial_pull += dpull

        return inertial_pull

    def get_stress_at(self, h):
        A = self.get_A_at(h)
        P_below = -self.get_gravitational_pull(0, h) + self.get_inertial_pull(0, h)
        P_above = -self.get_gravitational_pull(h, self.h) + self.get_inertial_pull(h, self.h)
        dP = P_above - P_below
        stress = dP/A
        return stress

    def get_tan_vel_at(self, h):
        return self.body.get_tan_vel_at(h)
