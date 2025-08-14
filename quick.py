def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 파일 읽기
with open("data.txt", "r") as f:
    raw_data = f.read()

# 콤마, 공백 제거 후 숫자로 변환 → 배열 저장
data = list(map(int, raw_data.replace(",", " ").split()))

# 데이터 개수 확인
if len(data) > 10000:
    raise ValueError("데이터 개수가 10,000개를 초과했습니다.")

# 정렬
sorted_data = quick_sort(data)

# 출력
print("퀵 정렬:", sorted_data)
