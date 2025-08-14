import sys

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 insertion_sort.py data.txt")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().split()))[:100]
    insertion_sort(data)
    print(data)
