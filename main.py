import time
def numbers():
    a = b = 1
    elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for n in range(10):
        c = a + b
        a = b
        b = c
        elements.append(b)
    print(elements)
def speed_test():
    tiime = time.time()
    numbers()
    tiiime = time.time()
    all = tiiime-tiime
    print(all)