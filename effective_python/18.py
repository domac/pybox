def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ' '.join(str(x) for x in values)
        print('%s: %s' % (message, value_str))


log('My Number are',[1,2])
log('Hi there')

fav = [7, 33, 99]

log('My favorite color', *fav)

def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

print('-----------------------')

def log2(seq, message, *values):
    if not values:
        print('%s: %s' % (seq, message))
    else:
        value_str = ' '.join(str(x) for x in values)
        print('%s: %s: %s' % (seq, message, value_str))

log2(1,'My Number are',1,2)
log2(3,'My Number are',fav)