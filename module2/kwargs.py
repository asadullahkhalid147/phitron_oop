def full_name(first,last):
    name = f'{first}{last}'
    return name

# name = full_name('Alu','Kodu')
name = full_name(last='Kodu',first ='Alu')
print(name)

def famous_name(first,last,**kwargs):
    name = f'{first}{last}'
    # print(kwargs)
    # print(kwargs['title'])
    for key,value in kwargs.items():
        print(key,value)
    return name

name = famous_name(first='Taher',last='Ali',title = 'Hujur',addition='Shayokh')
print(name)