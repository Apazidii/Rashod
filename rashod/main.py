from new import NewEx
import math
class man():

    def __init__(self,name,head,IDEx):
        self.Name = name
        self.IDex = IDEx
        l = len(head)
        k = {}
        if isinstance(head,list):
            for i in range(0,l):
                k.update({head[i]:0})
            self.Debs = k
        else:
            self.Debs = head

#   на вход получает словарь группы и отчищает все данные кроме имени
#   ничего не возвращает
def rebootGroup(dictGroup):
    for i in dictGroup:
        k = dictGroup[i]
        for j in k.Debs:
            k.Debs[j]=0
        k.IDEx = set()

#   на вход получает словарь группы
#   и исходя из истории транзакций в baseEX.txt записывает все долги в объекты внутри словаря
#   В конце вызывает метод RePrintDeb чтобы переписать все конечные расходы в mainEx.txt
#   ничего не возвращает
def reEXs(dictGroup):
    rebootGroup(dictGroup)
    filer = open("baseEx.txt", "r", encoding="utf-8")
    arEx = []
    for line in filer:
        arEx.append(eval(line))
    lex = len(arEx)
    for i in range(0,lex):
        Ex = arEx[i]

        ldeb = len(Ex["Debtop"])
        Summ = Ex['Summ']
        Summ = Summ / ldeb

        if Ex['Creditor'] in Ex["Debtop"]:
            Ex['Debtop'].remove(Ex['Creditor'])
        ldeb = len(Ex['Debtop'])
        for j in range(0,ldeb):

            dictGroup[Ex["Debtop"][j]].Debs[Ex["Creditor"]]+= Summ
            dictGroup[Ex["Debtop"][j]].IDEx.update({Ex["ID"]})
            dictGroup[Ex["Creditor"]].IDEx.update({Ex["ID"]})
            #Вычитаем долги друг из друга
            a = dictGroup[Ex["Debtop"][j]].Debs[Ex['Creditor']]
            b = dictGroup[Ex['Creditor']].Debs[Ex['Debtop'][j]]
            c = a - b
            if c >0:
                dictGroup[Ex["Debtop"][j]].Debs[Ex['Creditor']] = abs(c)
                dictGroup[Ex['Creditor']].Debs[Ex['Debtop'][j]] = 0
            else:
                dictGroup[Ex['Creditor']].Debs[Ex['Debtop'][j]] = abs(c)
                dictGroup[Ex["Debtop"][j]].Debs[Ex['Creditor']] = 0

    RePrintDeb(dictGroup)

#   На вход получает словарь группы
#   Выводит в консоль индексы транзакций каждого из участников
#   Ничего не возвращает
def printID(dictGroup):
    for i in dictGroup:
        print(i,dictGroup[i].IDEx)

#   Ничего не получает на вход
#   Запрашивает в консоли имена через пробел каждого из участников группы
#   Создает объекты для каждого из них и заносит их в словарь
#   В файл mainEx
#   Возвращает словарь пользователей
def NewGroup():
    print("Введите участников группы: ")
    group = input()
    group = group.split()

    l = len(group)
    filew = open("mainEx.txt", "w", encoding="utf-8")
    filew.writelines(str(group))
    dictGroup = {}
    for i in range(0,l):
        g = group.copy()
        g.pop(i)

        p = man(group[i],g,set())
        dictGroup.update({group[i]:p})
    return dictGroup



#   Получает на вход объект члена группы
#   Записывает все данные о его текущих долгах в mainEx.txt
#   Ничего не возвращает
def printDeb(man):
    filer = open("mainEx.txt", "r", encoding="utf-8")
    arMain = {}
    f = True
    for line in filer:
        if f:
            head = eval(line)
            f = False
        else:
            k = eval(line)
            arMain.update(k)

    result = {man.Name : [man.Debs,man.IDEx]}
    #result.append(man.Debs)

    filew = open("mainEx.txt", "w", encoding="utf-8")
    filew.writelines(str(head)+"\n")

    arMain.update(result)
    for i in arMain:
        filew.writelines(str({i:arMain[i]})+"\n")


#   Ничего не принимает на вход
#   Исходя из записей в mainEx.txt создает объекты для каждого из членов группы
#   и заносит их в словарь
#   Использовать для продолжения работы с уже существующей группой
#   Возвращает словарь группы
def NowGroup():
    filer = open("mainEx.txt", "r", encoding="utf-8")
    arMain = {}
    f = True
    for line in filer:
        if f:
            head = eval(line)
            f = False
        else:
            k = eval(line)
            arMain.update(k)
    dictGroup = {}
    for i in arMain:
        dictGroup.update({i:man(i,arMain[i][0],arMain[i][1])})
    return dictGroup


#   Получает на вход словарь группы
#   Вызывает метод PrintDeb для каждого члена группы
#   И прописывает все конечные долги в файле mainEx.txt
#   Ничего не возвращает
def RePrintDeb(dictGroup):
    for i in dictGroup:
        printDeb(dictGroup[i])

k = NowGroup()