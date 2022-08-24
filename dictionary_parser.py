try:
    file = open('file_for_parsing.txt', encoding='utf-8')
    English_file = open('English.txt', 'w', encoding='utf-8')
    Russian_file = open('Russian.txt', 'w', encoding='utf-8')
    try:
        r_alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

        for line in file:
            indx = 0
            for letter in line:

                if letter in r_alf:
                    indx = line.index(letter)
                    break

            english_part = line[:indx - 1].strip()
            russian_part = line[indx - 1:].strip()
            english_dict = english_part.split(';')
            russian_dict = russian_part.split(';')

            for eng in english_dict:
                for rus in russian_dict:
                    English_file.write(f'{eng.strip()}\n')
                    Russian_file.write(f'{rus.strip()}\n')
    finally:
        file.close()
        English_file.close()
        Russian_file.close()



except FileNotFoundError:
    print('Невозможно открыть файл')

except:
    print('Ошибка при работе с файлом')



