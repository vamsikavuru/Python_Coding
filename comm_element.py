# '''Program for common elements in both lists'''
def common_elements(A, B):
    # A = [1,4,5,7,11,14]
    # B = [3,5,6,13,24]
    p1 = 0
    p2 = 0
    result = []
    while p1 < len(A) and p2 < len(B):
        if A[p1] == B[p2]:
            result.append(A[p1])
            p1 += 1
            p2 += 1
        elif A[p1] < B[p2]:
            p1 += 1
        elif A[p1] > B[p2]:
            p2 += 1
        else:
            print("There is no common elements in both lists.")
    return result


A = [1, 4, 5, 7, 11, 14]
B = [1, 2, 6, 7, 11]
comm = common_elements(A, B)
print("The common elements in both the lists are :{} ".format(comm))
