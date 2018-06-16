count = 0
for a11 in range(0, 2):
    for a12 in range(0, 2):
        for a13 in range(0, 2):
            for a21 in range(0, 2):
                for a22 in range(0, 2):
                    for a23 in range(0, 2):
                        for a31 in range(0, 2):
                            for a32 in range(0, 2):
                                for a33 in range(0, 2):
                                    if 0 < a11 + a12 + a13 < 3 and \
                                            0 < a21 + a22 + a23 < 3 and \
                                            0 < a31 + a32 + a33 < 3 and \
                                            0 < a11 + a21 + a31 < 3 and \
                                            0 < a12 + a22 + a32 < 3 and \
                                            0 < a13 + a23 + a33 < 3:
                                        count += 1

print(count)
