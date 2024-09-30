with open ('numbers.txt', 'r',  encoding='utf-8') as file:
  numbers = file.read()

numbers_list = numbers.split(',')
numbers_list = [int(x) for x in numbers_list] 
print (numbers_list)


def insertionSortRecursive(arr,n): 
    
    if n<=1: 
        return
      
    
    insertionSortRecursive(arr,n-1) 

    last = arr[n-1] 
    j = n-2
      
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last


def bubbleSortRecursive(lista): 
    n = None
    if n is None: 
        n = lista.length 
    count = 0
    if n == 1: 
        return

    for i in range(n - 1): 
        if lista[i] > lista[i + 1]: 
            lista[i], lista[i +1] = lista[i + 1], lista[i] 
            count = count + 1
  

    if (count==0): 
        return

    lista.bubbleSortRecursive(n - 1) 

def recursive_selection_sort(arr, start=0):

    if start >= len(arr) - 1:
        return

    min_index = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

  
    arr[start], arr[min_index] = arr[min_index], arr[start]

 
    recursive_selection_sort(arr, start + 1)