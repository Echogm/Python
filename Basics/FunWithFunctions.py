# Fun With Functions
# def odd_even(start,end):
#     for i in range(start, end):
#         if i %2 == 1:
#             print "Number",i,"This",i,"is an odd number"
#         elif i %2 == 0:
#             print "Number",i,"This",i,"is an even number"
#     return
#
# odd_even(0,2001)

# Multiply
# def multiply(arr,x):
#     for i in range(0, len(arr)):
#         arr[i] *= x
#     return arr
#
# a = [2,4,10,16]
# print multiply(a,5)

# Hacker Challenge

# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
y = [2,4,5]

def layered_multiples(arr1,numb):
    for x in range(0, len(arr1)):
        arr1[x] *= numb
    print arr1
    return arr1
layered_multiples(y,5)
