def do_something(work):
    print('work started')
    work()
    print('work ended')


def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)

