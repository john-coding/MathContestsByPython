# Dolly, Molly and Polly start at S
# Dolly and Molly drive to A, when Polly gets to B
# Dolly drives back to meet Polly at C, when Molly gets to D.
# Dolly and Polly catches up with Molly at E.

# Let A be 90km away.
SA = 90
SA_time = SA/90
SB = 6 * SA_time

BA = SA-SB
AC_time = BA/(90+6)

SC = 6 + AC_time * 6
SD = 90 + AC_time * 6

DE_time = (SD-SC)/(90-6)  # which must be SA/90
SE = SD + DE_time * 6

total_time = SA_time + AC_time + DE_time
total_distance = SE

# Let us scale to desired distance
t = total_time / total_distance * 135
print(t)
