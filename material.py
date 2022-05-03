import math

class material:
    pass

# stainless steel 304L
# References: Choong S. Kim - Thermophysical Properties of Stainless Steels
class SS304L(material):
    def __init__(self):
        self.name = "Stainless Steel 304L"

    def get_name(self):
        return self.name

    def get_melting_point(self, unit="K"):
        if unit == "C":
            return 1400
        else:
            return 1673

    def get_thermal_conductivity(self, temp):
        # takes temperature in K
        # returns thermal conductivity in (W m-1 K-1)
        if temp < 1673:
            return (0.08116 + 0.0001618 * temp) * 100
        else:
            #print("304L melting!")
            return (0.1229 + (3.279 * 10**(-5)) * temp) * 100

    def get_thermal_diffusivity(self, temp):
        # takes temperature in K
        # returns thermal diffusivity in (m2 s-1)
        if temp < 1673:
            return (0.02276 + 3.285*10**(-5) * temp + 2.762*10**(-9) * (temp**2)) / 10000
        else:
            #print("304L melting!")
            return (0.02514 + 1.996*10**(-7) * temp + 2.386*10**(-9) * (temp**2)) / 10000

    def get_specific_heat(self, temp):
        # takes temperature in K
        # returns specific heat in J kg-1 K-1

        # initially calculated in cal g-1 K-1
        cgk = (0.1122 + 3.222*10**(-5) * temp)

        # do conversion when returning final value
        return cgk * 4.184 * 1000

    def get_density(self):
        # returns density in kg m-3
        return 8050

# copper chromium zirconium
# References: G. Pintsuk - Interlaboratory Test on Thermophysical Properties of the
#                          ITER Grade Heat Sink Material Copper–Chromium–Zirconium
#
# (Only data available was between 25 - 500 degrees C)
class CuCrZr(material):
    def __init__(self):
        self.name = "Copper-Chromium-Zirconium"

    def get_name(self):
        return self.name

    def get_melting_point(self, unit="K"):
        if unit == "C":
            return 1020
        else:
            return 1293

    def get_thermal_conductivity(self, temp):
        # takes temperature in K
        # returns thermal conductivity in W m-1 K-1
        return 358.07 * temp ** (-0.005)
        #return 353

    def get_specific_heat(self, temp):
        # takes temperature in K
        # returns specific heat in J kg-1 K-1
        return 0.0948 * temp + 367.97

    def get_density(self):
        # returns density in kg m-3
        return 8.75 * 1000

class water(material):
    def __init__(self):
        self.name = "water"

    def get_name(self):
        return self.name

    def get_density(self):
        return 997.77 # kg m-3
