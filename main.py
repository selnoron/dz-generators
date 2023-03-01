import names

# # 1
print('======1======')
# 1 variant
def chet():
    for i in range(10):
        if i % 2 == 0:
            yield i
        

a = chet()

# 2 variant
for i in a:
    if i % 2 == 0:
        print(i)
print('======2======')

# # 2
def chet():
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for i in alphabet:
        yield i

a = chet()
for i in a:
    print(i)

print('======3======')

# # 3


class Random:
    """Return random name"""

    @staticmethod
    def random_name() -> str:
        return names.get_first_name()
    
print(Random.random_name())