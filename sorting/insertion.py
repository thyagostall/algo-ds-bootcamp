def sort(data):
    data_size = len(data)
    current = 1
    while current < data_size:
        for i in range(current):
            if data[current] < data[i]:
                temp = data[i]
                data[i] = data[current]
                data[current] = temp

        current += 1

    return data
