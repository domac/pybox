def chain(*iteralbes):
    for i in iteralbes:
        yield from i


s = 'ABC'
t = tuple(range(3))

# python3 iter.py
print(list(chain(s, t)))