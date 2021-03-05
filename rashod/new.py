import main
def NewEx():
    import time
    arEx = []
    filer = open("baseEx.txt", "r", encoding="utf-8")
    for line in filer:
        arEx.append(eval(line))

    #   Генерируем ID
    if len(arEx)!= 0:
        LastInd = arEx[-1]["ID"]
    else:
        LastInd = -1

    #   Запрашиваем плательщика
    print("Кто заплатил: ",end ="")
    Creditor = input()

    #   Запрашиваем должника
    print("За кого заплатил: ",end="")
    Debtop = input()
    if Debtop == "Все":
        Debtop = ['Миша','Лена' ,'Коля',"Наташа","Саша","Костя"]
    else:
        Debtop = Debtop.split()

    #   Запрашиваем сумму траты
    print("Сколько заплатил: ",end ="")
    Summ = int(input())

    #   Запрашиваем причину траты
    print("За что заплатил: ", end = "")
    NameText = input()

    #   Узнаем время
    Time = time.time()



    DictEx = { "Creditor": Creditor, "Debtop":Debtop, "Summ": Summ, "NameText" : NameText, "Time": Time, "ID": LastInd+1 }

    file = open("baseEx.txt", "w", encoding="utf-8")
    for i in range(0,LastInd+1):
        file.write(str(arEx[i])+"\n")
    file.writelines(str(DictEx)+"\n")

NewEx()