# Let us apply Coordinate Geometry. Let P be the origin, PQ be the x-axis and PR be the y-axis.

import math

R = (0, 2 * math.sqrt(3))
Q = (2, 0)
M = (Q[0] / 2, 0)  # (1,0)

# the slope of RQ
s_RQ = (Q[1] - R[1]) / (Q[0] - R[0])
print("Slope of RQ:", s_RQ)

# the slope of PL
s_PL = -1 / s_RQ
print("Slope of PL:", s_PL)

# the equation of RM: x / M[0] + y / R[1] = 1
# the equation of PL: y = s_PL * x
# Since F is on PL, let F = (F_x, s_PL * F_x)
# Since F is on RM, F_x / M[0] + (s_PL * F_x) / R[1] = 1

F_x = 1 / (1 / M[0] + s_PL / R[1])
F_y = F_x * s_PL
PF = math.sqrt(F_x * F_x + F_y * F_y)
print("PF:", PF)

print(" A:", math.sqrt(3) / 2)
print(" B:", 3 * math.sqrt(3) / 7)
print(" C:", 4 * math.sqrt(3) / 7)
print(" D:", 5 * math.sqrt(3) / 9)
print(" E:", 3 * math.sqrt(3) / 5)
