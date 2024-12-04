from rockit import *
from numpy import pi, cos, sin, tan
import yaml
from casadi import vertcat

from simulator import simulator_omega_init, simulator


if __name__ == "__main__":
    simu = simulator_omega_init()
    
    # the input is (theta1, x1, y1, theta0)
    input = vertcat(1.5707963267948966,-0.09999999999999987,0.15,1.5707963267948966)
    # u is (delta0,v0)
    u = vertcat(-0.2996355163129934,0.19976529693488188)

    output = simulator(simu, input, u, 0.5)

    print(output)