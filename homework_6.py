def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"элемент {target} найден на позиции {mid}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f"элемент {target} не найден"


unsorted_list = [64, 25, 12, 22, 11]

sorted_list = bubble_sort(unsorted_list)

print("отсортированный список:", sorted_list)

result = binary_search(sorted_list, 22)

print(result)
