import time

from clock import *
from clock2 import *


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock2
def snooze2(seconds):
    time.sleep(seconds)


@clock2
def factorial2(n):
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

    print "<=========================>"

    print('*' * 40, 'Calling snooze(.123)')
    snooze2(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial2(6))