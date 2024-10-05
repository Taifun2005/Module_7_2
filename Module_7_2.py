from pprint import pprint
import io
def custom_write(file_name, strings):    #file_name - название файла # strings - список строк
    file = open(file_name, 'w', encoding='utf-8') #
    strings_positions = {}
    nstr = 1
    for i in strings:
        file.write(i)
        file.write('\n')
        # print(nstr)
        # print(file.tell())
        # print(i)
        # print(f"(({nstr}, {file.tell()}) '{i}')")
        key = f'({nstr}, {file.tell()})'
        strings_positions.update({key: i})    #, nsrt
        # strings_positions[file.tell] = i
        nstr += 1
    file.close()
    # print(strings_positions)
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)













# from io




# «R»-это чтение от слова «read»,
# «w»-это «write» от слова записать, запись и
# «а»-это «append» добавление
# tell текушее положение курсова
# seek установка курсора на
#
#
#

# name = "sample2.txt"
# file = open(name, 'a')
# print(file.tell())
# # pprint(file.read())
# print(file.seek(15))
# file.write('\nnew Text')
# print(file.tell())
# file.close()

# name = '1234.txt'
# file = open(name, 'a  ', encoding='UTF-8')
# print(file.write('Privet \nРоман\nЯ молодец'))
# # pprint(file.read())
# # print(file)
# file.close()