
arr = {}
sum = 0
for i in arr:
    sum +=i

print("sum of elements :{0} ".format(sum))

# Largest element in array

arr_1 = {34567,679087,8,345,234,908}
big_ele = 0
for i in arr_1:
    if big_ele<i:
        big_ele=i

print("The large element in array is : {0}".format(big_ele))


# 2nd leargest element in an array:

arr_2 = {45,23,789,742,820,123,72}

# Solution --> Sort the array and pick 2nd element in that array
# Impliment selection sort
def selection_sort(list_a):
    for i in range(0 , len(list_a)-1):
        max = list_a[i]
        for j in range(i+1, len(list_a)):
            if list_a[max] < list_a[j]:
                b = list_a[max]
                list_a[max]  = list_a[j]
                list_a[j] = b


list_a = {34,56,12,567,89,2345}
selection_sort(list_a)
print("Sorted Elements are:{0} ".format(list_a))
#print(list_a)















