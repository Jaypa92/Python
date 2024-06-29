# 1
def countDown(a):
    new_list = []
    for i in range(a, -1, -1):
        new_list.append(i)
    print(new_list)


countDown(5)

# 2


def printReturn(list):
    print(list[0])
    return list[1]


printReturn([1, 2])

# 3


def first_plus_length(list):
    x = list[0] + len(list)
    return x


z = first_plus_length([1, 2, 3])
print(z)

# 5


def length_and_value(size, value):
    x = str(value) * size
    print(x)


length_and_value(4, 7)
