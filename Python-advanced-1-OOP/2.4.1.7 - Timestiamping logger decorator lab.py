from timeit import default_timer as timer

def func_timer(func):
    def wrapper(*args, **kwargs):
        start = timer()
        r = func(*args, **kwargs)
        end = timer()
        print(f'Execution time was {end-start} s.')
        return r
    return wrapper    
        
@func_timer
def sum(a, b):
    return a+b
    
print('sum(3, 4): ', sum(3, 4))
print('sum(10, 4): ', sum(10, 4))