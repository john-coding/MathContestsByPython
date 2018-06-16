def is_connected(f12, f13, f14, f23, f24, f34):
    friends = {1, }

    # Add all friends of 1
    if f12:
        friends.add(2)
    if f13:
        friends.add(3)
    if f14:
        friends.add(4)

    # Add all friends of all friends of 1
    if f23:
        if 2 in friends:
            friends.add(3)
        if 3 in friends:
            friends.add(2)
    if f24:
        if 2 in friends:
            friends.add(4)
        if 4 in friends:
            friends.add(2)
    if f34:
        if 3 in friends:
            friends.add(4)
        if 4 in friends:
            friends.add(3)

    # Add all friends of all friends of all friends of 1
    # for example when we have friendship between 1 and 2, 2 and 3, 3 and 4.
    if f23:
        if 2 in friends:
            friends.add(3)
        if 3 in friends:
            friends.add(2)
    if f24:
        if 2 in friends:
            friends.add(4)
        if 4 in friends:
            friends.add(2)
    if f34:
        if 3 in friends:
            friends.add(4)
        if 4 in friends:
            friends.add(3)

    return friends == {1, 2, 3, 4}


count = 0
for a12 in (True, False):
    for a13 in (True, False):
        for a14 in (True, False):
            for a23 in (True, False):
                for a24 in (True, False):
                    for a34 in (True, False):
                        if is_connected(a12, a13, a14, a23, a24, a34):
                            count += 1

print("connected cases:", count)
print("    total cases:", 2 ** 6)
