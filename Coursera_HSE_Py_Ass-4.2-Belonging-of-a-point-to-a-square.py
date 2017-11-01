x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    if x <= 1 and y <= 1 and x >= -1 and y >= -1:
        return True
    else:
        return False
if IsPointInSquare(x, y):
    print('Yes')
else:
    print('No')
