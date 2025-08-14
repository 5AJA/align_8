from time import perf_counter
from typing import List
import sys

def bubble_sort(arr: List[float]) -> List[float]:
    """In-place bubble sort (오름차순)."""
    n = len(arr)
    # 조기 종료 최적화
    for i in range(n - 1):
        swapped = False
        # 마지막 i개는 이미 정렬됨
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def read_numbers_from_file(path: str) -> List[float]:
    """공백/줄바꿈으로 구분된 숫자들 읽기 (정수/실수 모두 허용)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise SystemExit(f"[에러] 파일을 찾을 수 없습니다: {path}")

    tokens = text.split()
    numbers: List[float] = []
    for idx, t in enumerate(tokens, 1):
        try:
            # 가능하면 정수로, 아니면 실수로
            if t.strip().lower() in {"+inf", "inf", "-inf", "nan"}:
                raise ValueError("비정상 숫자 토큰")
            if "." in t or "e" in t.lower():
                numbers.append(float(t))
            else:
                numbers.append(int(t))
        except ValueError:
            raise SystemExit(f"[에러] {idx}번째 토큰이 숫자가 아닙니다: {t!r}")
    return numbers

def main():
    path = sys.argv[1]
    numbers = read_numbers_from_file(path)

    start = perf_counter()
    bubble_sort(numbers)  # in-place 정렬
    elapsed = perf_counter() - start

    # 정렬 결과 출력 (공백 구분)
    # 정수/실수 섞여 있을 수 있으니 원형 유지하여 그대로 출력
    print(" ".join(str(x) for x in numbers))

    # 소요 시간 출력 (ms)
    print(f"\n정렬 소요 시간: {elapsed * 1000:.3f} ms")

if __name__ == "__main__":
    main()
