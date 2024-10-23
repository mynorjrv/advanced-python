import random

def random_list(
        length:int=1, 
        rang:list[int, int]=None
    ) -> list[int]:
    """ Returns a list of length "len", containing non repiting
    random integers in range "rang".
    """
    if rang is None:
        rang = [1, 100]
    if len(rang)!=2:
        raise ValueError("rang needs 2 arguments")
    if rang[0]>rang[1]:
        raise ValueError("The second value should be grater")
    if rang[1]-rang[0]<length:
        raise ValueError("range in rang must be grater than length")

    random_list = []

    while len(random_list)<length:
        random_number = random.randint(rang[0], rang[1])
        if random_number in random_list:
            continue
        random_list.append(random_number)

    return random_list

print(random_list(25, [1, 1000]))