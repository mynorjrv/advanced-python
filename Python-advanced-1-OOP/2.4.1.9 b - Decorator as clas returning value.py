from timeit import default_timer as timer

class FuncTimer:
    def __init__(self, dummy):
        self.dummy = dummy

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f'Dummy value is: ', self.dummy)
            start = timer()
            r = func(*args, **kwargs)
            end = timer()
            print(f'Execution time was {end-start} s.')
            return r
        return wrapper


@FuncTimer(3)
def sum(a, b):
    return a+b
    
print('sum(3, 4): ', sum(3, 4))
print('sum(10, 4): ', sum(10, 4))