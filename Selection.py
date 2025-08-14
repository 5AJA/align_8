
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

filename = "data.txt"
with open(filename, "r", encoding="utf-8") as f:
 
    data = [int(line.strip()) for line in f if line.strip()]

sorted_data = selection_sort(data)

print("선택 정렬:", sorted_data)
