def selection(data):
    data_size = len(data)
    current = 0
    while current < data_size:
        for i in range(current, data_size):
            if data[i] < data[current]:
                temp = data[i]
                data[i] = data[current]
                data[current] = temp

        current += 1

    return data
