def get_initial_step(data_size):
    h = 1
    while (h < data_size / 3):
        h = h * 3 + 1
        print(h)
    return h

def insertion_step(data, size=-1, step=1, offset=0):
    data_size = size
    if data_size == -1:
        data_size = len(data)

    current = offset + step
    while current < data_size:
        element = offset
        while element < current:
            if data[current] < data[element]:
                temp = data[current]
                data[current] = data[element]
                data[element] = temp
            element += step
        current += step

    return data

def shell(data):
    data_size = len(data)
    step = get_initial_step(data_size)

    while step >= 1:
        for offset in range(step):
            data = insertion_step(data, data_size, step, offset)

        step = step / 3
    return data
