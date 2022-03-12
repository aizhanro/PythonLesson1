print('\nзадание 1')
#Необходимо объединить заданные словари в одну словарь
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)

print('\nзадание 2')
#Выведите на экран значения ключа history
sampleDict = {
"class":{"student":{"name":"Mike","marks":{"physics": 70,
     "history": 80}}}
}
print(sampleDict)
#x = sampleDict['history']
#print(x) #не могу седалть

print('\nзадание 3')
#Создать функцию проверки людей на допуск людей участвовать в
#голосовании в зависимости от возраста
votersDict = {'Denis': 32,
              'Sergei': 21,
              'Elena': 18,
              'Timur': 17,
              'Oleg': 27}
print(f'Voters: {votersDict}')
if age >= 18:
    print()


print('\nзадание 4')
#Ваша задача попросить ввести имя человека и в зависимости от его имени удалить от этого словаря
studentList = {'Oleg': 'Moscow',
               'Stepan': 'Novosibirsk',
               'Olga': 'Ekaterenburg',
               'Murat': 'Bishkek',
               'David' : 'New Yourk'
}
print(f'Список имён: {studentList}')
name = input('Введите имя для удаления: ')
studentList.pop(name)
print(studentList)




