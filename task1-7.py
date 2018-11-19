from random import randint



def bubble_sort(mass):
    a = mass
    n = 1
    while n < len(mass): 
        for i in range(len(mass)-n):
            if mass[i] < mass[i+1]:
                mass[i],mass[i+1] = mass[i+1],mass[i]
        n+=1
    return a
        
mass = [randint(-100,100) for i in range(10)]
print("исходный массив:     ",mass)

print("сортированый массив: ", bubble_sort(mass))