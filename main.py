import time
import timeit


# def insertionSortRecursive(arr, n):

#     if n <= 1:
#         return

#     insertionSortRecursive(arr, n-1)

#     last = arr[n-1]
#     j = n-2

#     while (j >= 0 and arr[j] > last):
#         arr[j+1] = arr[j]
#         j = j-1

#     arr[j+1] = last


# def bubbleSortRecursive(lista, n=None):
    
#     n = None
#     if n is None:
#         n = len(lista)
#     count = 0
#     if n == 1:
#         return

#     for i in range(n - 1):
#         if lista[i] > lista[i + 1]:
#             lista[i], lista[i + 1] = lista[i + 1], lista[i]
#             count = count + 1

#     if (count == 0):
#         return

#     bubbleSortRecursive(lista, n - 1)

# def bubble_sort(arr):
#     """
#     Ordena uma lista usando Bubble Sort (recursivo).
#     """
#     n = len(arr)

#     # Função auxiliar para fazer uma passagem pelo array
#     def bubble_pass(arr, n):
#         if n == 1:
#             return  # Já está ordenado
#         for i in range(n - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Troca os elementos
#         bubble_pass(arr, n - 1)  # Chama recursivamente para o próximo passo

#     bubble_pass(arr, n) 

import sys
sys.setrecursionlimit(200000)  

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j+1] = chave
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

# Vídeo "Bubble Sort": https://youtu.be/GiNPe_678Ms
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)

# Vídeo "Selection Sort": https://youtu.be/ZT_dT8yn48s
def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

# def selection_sort(arr, start=0):

#     if start >= len(arr) - 1:
#         return

#     min_index = start
#     for i in range(start + 1, len(arr)):
#         if arr[i] < arr[min_index]:
#             min_index = i

#     arr[start], arr[min_index] = arr[min_index], arr[start]

#     recursive_selection_sort(arr, start + 1)


def merge_sort(lista):
    if len(lista) > 1:

        # encontrar o meio da lista
        meio = len(lista) // 2  # divisão inteira

        # dividindo a lista em duas sub-listas (L - R)
        # fatiamento de listas
        L = lista[:meio]
        R = lista[meio:]

        # Chamada recursiva
        merge_sort(L)
        merge_sort(R)

        # variáveis de controle
        # i - fará o controle da lista L
        # j - fará o controle da lista R
        # k - fará o controle da lista antes da recursão
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        # verificação dos elementos da lista L
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        # verificação dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1

def sortBubbleRecursive(lst, size):
    if size == 1:
        return  # Lista já ordenada

    sorted = True
    for i in range(size - 1):
        print(f'bubble falta: {i}...')
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            sorted = False
    
    if not sorted:
        sortBubbleRecursive(lst, size - 1)

def bubbleSortIterative(lst):
    size = len(lst)
    for i in range(size):
        sorted = True
        print(f'bubble falta: {size - 1}...')
        for j in range(0, size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                sorted = False
        if sorted:
            return  # Sai mais cedo se a lista já estiver ordenada
        
def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        if j == len(lista) - 1:
            return
        print(f'bubble falta: {j}...')
        for i in range(n-1):
            
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return



def get_time():
    tempo_gasto = []
    inicio = time.time()
    merge_sort(numbers_list1)
    fim = time.time()
    tempo_gasto.append(inicio - fim)

    inicio = time.time()
    bubble_sort(numbers_list2)
    fim = time.time()
    tempo_gasto.append(inicio - fim)

    inicio = time.time()
    selection_sort(numbers_list3)
    fim = time.time()
    tempo_gasto.append(inicio - fim)

    inicio = time.time()
    insertion_sort(numbers_list4)
    fim = time.time()
    tempo_gasto.append(inicio - fim)

    return tempo_gasto
    

with open('numbers.txt', 'r',  encoding='utf-8') as file:
    numbers = file.read()

numbers_list = numbers.split(',')
numbers_list_original = [int(x) for x in numbers_list]

numbers_list1 = numbers_list_original.copy()
numbers_list2 = numbers_list_original.copy()
numbers_list3 = numbers_list_original.copy()
numbers_list4 = numbers_list_original.copy() 



(r1, r2, r3, r4) = get_time()
print(f'O merge sort executou em {r1 : .3f} segundos ')
print(f'O bubble sort executou em {r2 : .3f} segundos ')
print(f'O selection sort executou em {r3 : .3f} segundos ')
print(f'O inserction sort executou em {r4 : .3f} segundos ')


# O merge sort executou em -0.496 segundos
# O bubble sort executou em -1767.369 segundos
# O selection sort executou em -402.750 segundos
# O inserction sort executou em -351.898 segundos



    
