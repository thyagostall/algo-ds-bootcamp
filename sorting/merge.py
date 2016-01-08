from collections import deque

import math
import queue

def merge(data, lowest, mid, highest):
    first = deque(data[lowest:mid + 1])
    second = deque(data[mid + 1:highest + 1])

    current = lowest
    while current <= highest:
    	if len(first) and len(second):
    		if second[0] < first[0]:
    			data[current] = second.popleft()
    		else: 
    			data[current] = first.popleft()
    	elif len(first):
    		data[current] = first.popleft()
    	else:
    		data[current] = second.popleft()

    	current += 1


def sort_impl(data, lowest, highest):
    if lowest == highest:
        return

    mid = lowest + math.floor((highest - lowest) / 2)

    sort_impl(data, lowest, mid)
    sort_impl(data, mid + 1, highest)

    merge(data, lowest, mid, highest)


def sort(data):
    data_size = len(data)
    sort_impl(data, 0, data_size - 1)
