def GraterThenFive(num):
    if num > 5:
        return True
    else:
        return False


l1 = [10, 20, 30, 40, 33, 34, 23, 56, 1, 4, 6]

print(list(filter(GraterThenFive,l1)))

