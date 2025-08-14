def merge_sort(arr):
	if len(arr) < 2:
		return
	tmp = [0] * len(arr)
	def sort(l, r):
		if r - l <= 1:
			return
		m = (l + r) // 2
		sort(l, m)
		sort(m, r)
		i, j, k = l, m, l
		while i < m and j < r:
			if arr[i] <= arr[j]:
				tmp[k] = arr[i]; i += 1
			else:
				tmp[k] = arr[j]; j += 1
			k += 1
		while i < m:
			tmp[k] = arr[i]; i += 1; k += 1
		while j < r:
			tmp[k] = arr[j]; j += 1; k += 1
		arr[l:r] = tmp[l:r]
	sort(0, len(arr))

def data(f):
	data = list(map(int, f.read().split()))[:100]
	merge_sort(data)
	print(data)