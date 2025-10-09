# Файлы и работа с ними
# Запись

f = open('./files/info.txt', 'at', encoding='utf-8')  # f - файловый объект (или дискриптер)

num = f.write('Привет, Python!')
print(f'В файл было записано {num} байт')
print(f.readable())

f.close()
