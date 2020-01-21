# most frequent item in an array
'''
arr = [3,2,1,5,6,3,2,3,1,3]
def most_frequent_item(arr):
    count = 0
    max_item = None
    max_count = -1
    for item in arr:
        if item not in count:
            arr[item] = 1
        else:
            arr[item] +=1
        if arr[item] > max_count:
            max_count = arr[item]
            max_item = item
        return  max_item

most_frequent_item(arr)
'''


def most_frequent_item(list_item):
    max_item = None
    max_count = -1
    count = {}
    #print((type(count)))
    for item in list_item:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
        if count[item]>max_count:
            max_count = count[item]
            max_item = item
    return max_item

#list_item = [2,3,4,56,2,3,2,3,2]
#list_item = [2,3,3,2]
#list_item = []
#list_item = [0]
list_item = [-1,2,10,-1,21,-1]
most = most_frequent_item(list_item)
print(most)







