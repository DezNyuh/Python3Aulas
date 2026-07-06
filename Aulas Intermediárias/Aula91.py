def generator(n=0, maximum=100):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

gen = generator(maximum=10000000)
for n in gen:
    print(n)