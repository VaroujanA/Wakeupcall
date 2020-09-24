num = [4,3,2,1]


def bubble_sort(array):
    n = len(array)
    while 1 < n:
        for i in range(n - 1):
            j = i + 1
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                print(array)


bubble_sort(num)