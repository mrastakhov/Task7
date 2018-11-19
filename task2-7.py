import random
 
len_l = int(input("введите размер массива: "))
lst = [(random.randint(0,50)) for i in range(len_l)]
lst.append(0)
 
print ("Исходный массив:        ", lst)


def randdel(left, right):

    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst
    
def randsort(lst):

    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = randdel(randsort(lst[:mid]), randsort(lst[mid:]))
    return lst

print("Отсортированный массив: ", randsort(lst))