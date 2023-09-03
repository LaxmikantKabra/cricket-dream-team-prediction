def pour(jug1, jug2):
    max1, max2, fill = 3, 4, 2
    print("%d\t%d" % (jug1, jug2))
    if jug2 == fill:
        return
    elif jug2 == max2:
        pour(0, jug1)
    elif jug1 != 0 and jug2 == 0:
        pour(0, jug1)
    elif jug1 == fill:
        pour(jug1, 0)
    elif jug1 < max1:
        pour(max1, jug2)
    elif jug1 < (max2-jug2):
        pour(0, (jug1+jug2))
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2)

print("JUG1\tJUG2")
pour(0, 0)
