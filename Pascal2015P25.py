a = {1, 3, 4, 6, 8}

# 2371 = 2 * 3 * 5 * 790 + 1
for r in range(1, 2732):
    for v in range(1, 2732):
        if v not in a:
            if 2731 == v:
                print("V V=" + str(v))
            if 2731 == 2 * v + 1:
                print("W V=" + str(v))
            if 2731 == 3 * v + 1:
                print("X V=" + str(v))
            if 2731 == 5 * v + 1:
                print("Y V=" + str(v))
            if 2731 == 7 * v + 1:
                print("Z V=" + str(v))

            a.add(v)
            a.add(2 * v + 1)
            a.add(3 * v + 1)
            a.add(5 * v + 1)
            a.add(7 * v + 1)
            # print([v, 2 * v + 1, 3 * v + 1, 5 * v + 1, 7 * v + 1])
            break
