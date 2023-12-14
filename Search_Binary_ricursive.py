def search_binery(li, num, low, hight):
    if low <= hight: 

        mid = int((hight+low)/2)

        if li[mid] == num:
            # if find.
            return mid
        if li[mid] > num:
            # If the desired value is greater.
            return search_binery(li, num, low, mid-1)
        else:
            # If the desired value is smaller.
            return search_binery(li, num, mid+1, hight)


li = [2, 3, 4, 5, 6]

num = search_binery(li, 10, 0, 4)
if num:
    print("find :", num)
else:
    print("not finded.....")
