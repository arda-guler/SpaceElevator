import math
pi = math.pi

import matplotlib.pyplot as plt

from material import *
from elevator import *

h_elev = 35786000*1.5
w_max = 100000
w_min = 10000

def quadratic_profile(h):
    global h_elev
    hmax = h_elev
    x = hmax - h
    y_coeff = ((w_max - w_min)/h_elev**2)
    y = y_coeff * x**2 + w_min # 10km at tip, 100km at sea level
    A = pi * y**2
    return A

def linear_profile(h):
    global h_elev
    hmax = h_elev
    x = hmax - h
    y_coeff = (w_max - w_min)/h_elev
    y = y_coeff * x + w_min # 10km at tip, 100km at sea level
    A = pi * y**2
    return A

def constant_profile(h):
    y = w_min
    A = pi * y**2
    return A

def main():
    SS = SS304L()
    
    # angular velocity of Earth is calculated with (2pi / sideral day length)
    earth = celestial_body(5.972 * 10**24, 6371000, 7.292*10**(-5))

    # geostationary orbit for earth is 35786 km
    # this lift reaches twice the height
    Atlantic_Lift = elevator(earth, h_elev, quadratic_profile, SS)

    hs = []
    ys = []
    stresses = []
    gravitys = []
    inertials = []
    total_forces = []
    total_accels = []
    for h in range(0, int(h_elev), 100000):
        hs.append(h/1000)
        ys.append((Atlantic_Lift.A(h)/pi)**(0.5)/1000)
        stresses.append(Atlantic_Lift.get_stress_at(h)/10**9)
        gravitys.append(Atlantic_Lift.get_gravitational_pull(h-100000, h)/10**9)
        inertials.append(Atlantic_Lift.get_inertial_pull(h-100000, h)/10**9)
        total_forces.append((Atlantic_Lift.get_inertial_pull(h-100000, h) - Atlantic_Lift.get_gravitational_pull(h-100000, h))/10**9)
        total_accels.append((Atlantic_Lift.get_inertial_pull(h-100000, h) - Atlantic_Lift.get_gravitational_pull(h-100000, h)) / Atlantic_Lift.get_mass_between(h-100000, h))

    _, ax = plt.subplots()
    plt.plot(ys, hs)
    plt.grid()
    plt.xlabel("Tower Radius (km)")
    plt.ylabel("Tower Height (km)")
    plt.show()

    plt.plot(hs, stresses)
    plt.grid()
    plt.xlabel("Tower Position (km)")
    plt.ylabel("Stress (GPa)")
    plt.show()

    plt.plot(hs, gravitys)
    plt.grid()
    plt.xlabel("Tower Position (km)")
    plt.ylabel("Gravity Force About Position (GN)")
    plt.show()

    plt.plot(hs, inertials)
    plt.grid()
    plt.xlabel("Tower Position (km)")
    plt.ylabel("Inertia-induced Force About Position (GN)")
    plt.show()

    plt.plot(hs, total_forces)
    plt.grid()
    plt.xlabel("Tower Position (km)")
    plt.ylabel("Net Force About Position (GN)")
    plt.show()

    plt.plot(hs, total_accels)
    plt.grid()
    plt.xlabel("Tower Position (km)")
    plt.ylabel("Net Acceleration About Position (GN)")
    plt.show()

main()
