def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


def binary_search(lst, value):
    print(lst)
    print(value)
    mid = len(lst) // 2
    low = 0
    high = len(lst) - 1
    while lst[mid] != value and low <= high:
        if value > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if low > high:
        return "No value"
    else:
        return mid


def catch(lst, counter):
    if lst[0] <= lst[-1]:
        return counter

    else:
        return catch(lst[0:len(lst) - 1], counter + 1)


def weird_search(lst):
    count = catch(lst, 0)
    data = len(lst)-count-1
    if count == 0:
        return len(lst)-1
    else:
        return data


def my_search(lst, value):
    left = lst[0]
    right = lst[-1]
    mid = len(lst) // 2
    if left < right:
        output = binary_search(lst, value)
        return output

    foo = weird_search(lst[:mid])
    bar = weird_search(lst[mid-1:])
    if lst[foo] > lst[bar+mid-1]:
        return foo
    else:
        return bar+mid-1


def LinearSearch(lys, element):
    for i in range(len(lys)):
        if lys[i] == element:
            return i
    return -1


a = []

for i in range(1, 200):
    a.append(i)

for i in range(1, 200):
    a = sorted(a)
    point = a[-1]

    shift(a, i)
    print(a)

    print(my_search(a, point), LinearSearch(a, point))

