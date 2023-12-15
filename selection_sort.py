def find_smalest(arr: list):
    # find the smallest number in array
    temp = arr[0]
    number_list = len(arr)
    for i in range(1, number_list):
        if arr[i] < temp:
            temp = arr[i]

    return temp


def selection_sort(arr: list):
    number_list = len(arr)
    sort_number= []
    for i in range(number_list):
        smallest_number = find_smalest(arr)
        arr.remove(smallest_number)
        sort_number.append(smallest_number)
    
    return sort_number
    
        
    


arr = [-12, 3, 6, 4, 8, 0, -1]

print(selection_sort(arr))
