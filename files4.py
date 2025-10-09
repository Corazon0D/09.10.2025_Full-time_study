# Файлы и работа с ними
# Построчное чтение
from pydoc import stripid

f = open('./files/info.txt', 'rt', encoding='utf-8')  # f - файловый объект (или дискриптер)



# stripid() убирает пустоту (пустые строчки)

# читать файл самый лучший (оптимальный) (если нет пустых строк до конца фала)
# while line := f.readline().strip():
#     print(line)
"""
# Через map
lines = f.readlines()

lines = list(map(lambda x: x.strip(), lines))

for line in lines:
    if line:
        print(line)
"""
# print(lines)


# Через списочное выражение
lines = f.readlines()

lines = [x.strip() for x in lines]

for line in lines:
    if line:
        print(line)

f.close()

""" это топорно не делай так! ! !
line = None

while True:
    line = f.readline().strip()
    if line:
        print(line)
        
"""