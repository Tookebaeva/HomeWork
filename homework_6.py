def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(f"Элемент {target} найден в индексе {mid}")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"Элемент {target} не найден")
    return -1

unsorted_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

target = 22
binary_search(sorted_list, target)
