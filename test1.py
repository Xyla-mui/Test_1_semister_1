print("Test 1 question 2")

print("_____(a)______")
my_list = [1, 2, 3]
print(my_list[2])

print("_____(b)______")
text = "Python"
print(text[1:4])
print("_____(c)______")
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.intersection(set_b))
print("_____(d)______")
colors = {"red": "#FF0000", "green": "#00FF00"}
print(colors.get("blue", "not found"))
print("_____(e)______")
result = [x*2 for x in range(3)]
print(result)
print("_____(f)______")
s = "hello"
print(s.upper())
print("_____(g)______")
tup = (5, 10, 15)
print("Immutable")

listOfNum = [3, 8, 2, 5, 9]


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]
        pivot_index = i + 1

        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)


quicksort(listOfNum)
print("printed last number :", listOfNum[-1])
