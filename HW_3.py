# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def res(ls):
    # print(ls)
    key = list(set(str(i[0]) for i in ls))
    # print(key)
    res={}
    # lss=[]
    for j in key:
        # for i in ls:
        #     if str(i[0]) == j:
        #         lss.append(i)
        # lss = [i for i in ls if str(i[0]) == j]
        ## lss = list(filter(lambda i: str(i[0]) == j, ls))
        # res[j] = lss
        res[j] = list(filter(lambda i: str(i[0]) == j, ls))
        lss = []
    return res

names = input('Введите имена сотрудников через пробел(!!!): ').split(" ")
print(res(names))
#                         саша маша коля петя соня мария филипп антон андрей алексей