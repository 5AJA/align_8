from __future__ import annotations

from typing import Any, Callable, Iterable, List, MutableSequence, Optional, Sequence, TypeVar


T = TypeVar("T")


def _value(x: T, key: Optional[Callable[[T], Any]]) -> Any:
	"""정렬 비교에 사용할 값을 반환.

	- key가 주어지면 key(x)
	- 아니면 원본 x
	"""
	return key(x) if key is not None else x


def merge(
	left: Sequence[T],
	right: Sequence[T],
	key: Optional[Callable[[T], Any]] = None,
	reverse: bool = False,
) -> List[T]:
	"""두 정렬된 시퀀스를 안정적으로 병합하여 새 리스트로 반환.

	- 안정성 보장: 동일 키일 때 항상 좌측 요소가 먼저 온다.
	- reverse=True 일 때는 내림차순이 되도록 비교 방향만 바꾼다.
	"""
	i = 0
	j = 0
	len_left = len(left)
	len_right = len(right)
	result: List[T] = []

	while i < len_left and j < len_right:
		lv = _value(left[i], key)
		rv = _value(right[j], key)
		if not reverse:
			# 안정성: lv == rv 이면 왼쪽을 먼저 선택
			if lv <= rv:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		else:
			# reverse: 내림차순. 안정성 유지 위해 lv >= rv 시 왼쪽 우선
			if lv >= rv:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1

	# 남은 꼬리 추가
	if i < len_left:
		result.extend(left[i:])
	if j < len_right:
		result.extend(right[j:])

	return result


def merge_sort(
	items: Sequence[T],
	key: Optional[Callable[[T], Any]] = None,
	reverse: bool = False,
) -> List[T]:
	"""재귀적 병합 정렬. 입력을 변경하지 않고 새 리스트를 반환.

	예시:
	>>> merge_sort([3, 1, 2])
	[1, 2, 3]
	>>> merge_sort(["b", "aa", "c"], key=len)
	['b', 'c', 'aa']
	"""
	length = len(items)
	if length <= 1:
		return list(items)

	mid = length // 2
	left_sorted = merge_sort(items[:mid], key=key, reverse=reverse)
	right_sorted = merge_sort(items[mid:], key=key, reverse=reverse)
	return merge(left_sorted, right_sorted, key=key, reverse=reverse)


def merge_sort_iterative(
	items: Sequence[T],
	key: Optional[Callable[[T], Any]] = None,
	reverse: bool = False,
) -> List[T]:
	"""반복(비재귀) 방식의 병합 정렬. 새 리스트 반환.

	작동 방식: 길이 1의 런(run) 리스트들을 쌍으로 병합하며 크기를 키운다.
	"""
	runs: List[List[T]] = [[x] for x in items]
	if not runs:
		return []

	while len(runs) > 1:
		new_runs: List[List[T]] = []
		for i in range(0, len(runs), 2):
			if i + 1 < len(runs):
				new_runs.append(merge(runs[i], runs[i + 1], key=key, reverse=reverse))
			else:
				new_runs.append(runs[i])
		runs = new_runs

	return runs[0]


def merge_sort_inplace(
	items: MutableSequence[T],
	key: Optional[Callable[[T], Any]] = None,
	reverse: bool = False,
) -> None:
	"""리스트를 제자리에서 정렬. 내용만 바꾸고 반환값은 없음.

	구현 간결성을 위해 내부적으로 새 리스트를 만들어 정렬한 뒤, 슬라이스 할당으로
	원본 리스트 내용을 교체한다. (알고리즘적 의미의 in-place는 아님)
	"""
	sorted_items = merge_sort(items, key=key, reverse=reverse)
	items[:] = sorted_items


