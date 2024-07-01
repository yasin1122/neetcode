for i in range(20):
    if i % 2 == 0:
        continue
    elif i == 11:
        break
    elif i == 1:
        pass
    else:
        print(i, end = ' ')