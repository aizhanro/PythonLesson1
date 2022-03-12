#1 Добавьте в заданное множество, заданный список:
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
resultSample = sampleSet.union(sampleList)
print(resultSample)
print('\n')

#2 Необходимо вернуть схожий результат взятый из двух разных множеств (set1 = {10, 30})
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1.difference(set2)
print(set3)
print('\n')

#3 обновить множество с элементами, которые есть только в 1 элементе, но нет 2 элементе
set1 = {10, 20, 30}
set2 = {20, 40, 50}
setnew = set.difference(set2)
print(setnew)
print('\n')
#4.1 добавьте один новый элемент
co = {1, 3}
co.add(5)
print(co)
print('\n')
#добавьте сразу несколько элементов в множество
co.update('wolf',{14}, [15, 3])
print(co)
print('\n')

#добавьте список и еще одно множество в ваше изначально созданное set
spisok = [14, 5]
co1 = {4.5, 67,}
col = co1.union(spisok)
print(col)
resultSat = co.union(col)
print(resultSat)
print('\n')
#5.1 Создайте set и frozenset. Объедините оба множество в одно целое.
print('5 zadanie')
don1 = {1, 5}
don2 = frozenset({45, 2})
don3 = don1.union(don2)
print(don3)

# 5.1 к объединенному множеству добавьте элемент 2 и 5
don3.update({2, 5})
print(don3)

#5.2 удалите число 2, а также первый элемент в множестве
don3.remove(2)
print(don3)
don3.pop()
print(don3)