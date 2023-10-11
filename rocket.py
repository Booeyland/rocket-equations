# Author = Andrew Talpins
import math
#Constant Variables
#----------------------------------------------------------------
mR = .0164 # Rocket Mass in kg
g = 9.81 # acceleration of gravity in m/s^2
A = 0.00028352873 # rocket cross-sectional area in m^2
cd = 0.75 # drag coefficient
aD = 1.223 # air density in kg/m^3
#----------------------------------------------------------------

def do_the_math(engine_type):
    match engine_type:
        case 1: # A83
            mE = .0162 # engine mass with propellant in kg
            mP = .00312 #propellant mass in kg
            t = 0.5 #motor burn time in seconds
            I = 2.5
        case 2: # B6-4
            mE = .0201 # engine mass with propellant in kg
            mP = .00624 #propellant mass in kg
            t = 0.8 #motor burn time in seconds    
            I = 5    
        case 3: # C6-3
            mE = .0249 # engine mass with propellant in kg
            mP = .01248 #propellant mass in kg
            t = 1.6 #motor burn time in seconds
            I = 10
        case 4: # C6-5
            mE = .0258 # engine mass with propellant in kg
            mP = .01248 #propellant mass in kg
            t = 1.6 #motor burn time in seconds
            I = 10
        case _:
            print("Please select a rocket engine that this program supports")
            quit()
    T = I/t
    mB = mR + mE - mP/2 # boost mass in kg
    mC = mR + mE - mP
    q = math.sqrt((T-(mB)*g)/(aD*cd*A/2)) # variable q to make equations easier on the eyes
    k = (aD*cd*A/2) # air drag coefficient in kg/m
    p = 2*k*q/mB # variable p to make equations easier on the eyes   
    q2c = (-mC*g)/k # variable q2c to make equations easier on the eyes

    vt = q * (1-math.exp(-p*t))/(1+math.exp(-p*t)) # burnout velocity in m/s

    hB = (mB)/(2*k) * math.log((q*q)/(q*q - vt*vt)) # Burnout Altitude in m

    hC = (mC)/(2*k) * math.log((q2c - vt*vt)/q2c) # Coast Altitude in m 

    print(f"Burnouy velocity: {vt} m/s")
    print(f"Burnout altitude: {hB}m ")
    print(f"Coast Altitude {hC}m")
    print(f"----\nTotal Altitude {hB + hC}m")

if __name__ == "__main__":
    engine_type = int(input("[1] A8-3\n[2] B6-4\n[3] C6-3\n[4] C6-5\nPlease input the number of the engine type: "))
    do_the_math(engine_type)