count = 0
for a12 in [0, 1]:
    for a13 in [0, 1]:
        for a14 in [0, 1]:
            for a15 in [0, 1]:
                for a16 in [0, 1]:
                    for a23 in [0, 1]:
                        for a24 in [0, 1]:
                            for a25 in [0, 1]:
                                for a26 in [0, 1]:
                                    for a34 in [0, 1]:
                                        for a35 in [0, 1]:
                                            for a36 in [0, 1]:
                                                for a45 in [0, 1]:
                                                    for a46 in [0, 1]:
                                                        for a56 in [0, 1]:
                                                            if a12 + a13 + a14 + a15 + a16 == 3 and \
                                                                    a12 + a23 + a24 + a25 + a26 == 3 and \
                                                                    a13 + a23 + a34 + a35 + a36 == 3 and \
                                                                    a14 + a24 + a34 + a45 + a46 == 3 and \
                                                                    a15 + a25 + a35 + a45 + a56 == 3 and \
                                                                    a16 + a26 + a36 + a46 + a56 == 3:
                                                                count += 1
                                                                print(a12, a13, a14, a15, a16, a23, a24, a25, a26, a34,
                                                                      a35, a36, a45, a46, a56)

print(count)

# Here is the deduction by logic. Let us denote the 6 different teams by t1, t2, t3, t4, t5, and t6.
#
# There are C(6,3)/2 = 10 bipartite arrangements.
#
# What are the rest arrangements? Let us choose 3 teams to play against team t1, which we have 10
# ways to do. Without loss of generality, let we say the three teams are team t2, t3 and t4. How many
# ways we can we extend this choice to a non-bipartite arrangement?
#
# If team t5 does not play against team t6, then each of team t5 and team t6 must play against all of
# team t2, t3 and t4, which means we have team t1, t5, t6 as a party to play against team t2, t3 and t4 as
# a party, a bipartite arrangement that is excluded in current consideration. So team t5 must play
# with team t6. The other 2 opponents of team t5 must be chosen from team t2, t3 and t4. We have 3
# way to select those 2 opponents. Without loss of generality, let us say we select team t2 and t3.
#
# Besides team t5, the other 2 opponents of team t6 must be chosen from team t2, t3 and t4. If we choose
# team t2 and t3 just as what have chosen for team t5, then each of team t2, t3, t5 and t6 has three
# opponents, that is, each of them will not play with team t4, which means teams t4 can only against
# team t1, a violation of the requirement. So the other two opponents of team t6 cannot be team t2 and t3.
# There are 2 ways to choose these 2 opponents. We can choose them to be either team t2 and t4 or team t3
#  and t4. Without loss of generality, let us choose team t2 and team t4 to play against team t6.
#
# Note that we have chosen all three components for team t1, t2, t5 and t6. We have also arranged team t3
# to plays against team t1 and t5 and we have arranged team t4 to play against team t1 and t6. So team t3
# and team t4 have to play against each other. Now all teams are scheduled.

# So there are 10 * 3 * 2 = 60 ways to select a non-bipartite arrangement. In total, there are 10 + 60 = 70.
