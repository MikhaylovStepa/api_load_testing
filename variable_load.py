from random import uniform, randint


def split_on_difference_parts(time_duration, number_of_parts):
    arr = [0, time_duration]
    arr_difference = [0]
    i = 0
    while i < number_of_parts-2:
        j = 0
        count = len(arr)
        arr.sort()
        while j < count-1 and i < number_of_parts - 2:
            value = uniform(arr[j], arr[j+1])
            arr.append(value)
            j = j+1
            i = i+1
    arr.sort()
    i = 1
    while i < number_of_parts:
        arr_difference.append(arr[i] - arr[i-1])
        i = i+1
    return arr_difference


def split_on_equal_parts(time_duration, number_of_parts):
    return time_duration/(number_of_parts-1)