import shelve

shelve_name = 'first_shelve.shlv'

my_shelve = shelve.open(shelve_name, flag='c')
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}
my_shelve.close()

new_shelve = shelve.open(shelve_name)
print(new_shelve['USD'])
new_shelve.close()

second_shelve_name = 'second_shelve.shlv'
with shelve.open(second_shelve_name, flag='c') as my_second_sheve:
    my_second_sheve['EUR'] = {'code':'Euro', 'symbol': '€'}
    my_second_sheve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
    my_second_sheve['USD'] = {'code':'US dollar', 'symbol': '$'}
    my_second_sheve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

with shelve.open(second_shelve_name, flag='c') as my_second_sheve:
    print(my_second_sheve['USD'])