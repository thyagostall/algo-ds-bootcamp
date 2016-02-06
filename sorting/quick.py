import random

def swap(data, i, j):
	temp = data[j]
	data[j] = data[i]
	data[i] = temp

def partition(data, start, end):
	p = random.randint(start, end)
	i = start
	j = end
	
	while True:
		while data[i] < data[p]:
			i += 1

		while data[j] > data[p]:
			j -= 1

		if j <= i:
			break

		swap(data, i, j)
	return j


def sort_impl(data, start, end):
	if start >= end:
		return

	p = partition(data, start, end)
	sort_impl(data, start, p - 1)
	sort_impl(data, p + 1, end)

def sort(data):
	sort_impl(data, 0, len(data) - 1)