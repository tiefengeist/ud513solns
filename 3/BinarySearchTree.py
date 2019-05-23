def binary_search(input_array, value):
    mid = len(input_array)/2
    pos = mid
    list = input_array
    while len(list) > 0:
        result = list[mid]
        if value > result:
            list = list[mid+1:len(list)]
            pos += len(list)//2
        elif value < result:
            list = list[0:mid]
            pos -= len(list)//2
        elif result == value:
            return pos
        mid = len(list)//2
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
