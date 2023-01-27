g = 9.81
initialVelocity = 44
x = 0.5
heightBarrel = 1
from math import pi, tan, cos
elevation = 80
theta = elevation * (pi/180)
print(theta)

y = heightBarrel+(x*tan(theta))-(g*x*x)/(((initialVelocity*cos(theta))**2)*2)


print(y)









