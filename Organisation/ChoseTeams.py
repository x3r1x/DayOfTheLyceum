# программа, которая составляет входное количество комманд в зависимости без друзей, выбранных самими пользователями
from random import choice

# список всех классов, начиная с 11 и заканчивая 8
students = {
    '11thGrade':
        [
            'Иван Березин',
            'Никита Витчуков',
            'Никита Зимин',
            'Денис Кистанов',
            'Антон Козлов',
            'Мария Луганская',
            'Роман Мокосеев',
            'Вадим Патрушев',
            'Роман Хаснулин',
            'Ростислав Шиптенко'
        ],
    '10thGrade':
        [
            'Анастасия Батухтина',
            'Иван Герасимов',
            'Илья Каракулов',
            'Арсений Попов',
            'Данил Романов',
            'Глеб Рыжов',
            'Юлия Сафина',
            'Елисей Смирнов',
            'Иван Токтаев',
            'Глеб Трофимов',
            'Артём Чепурной',
            'Роман Шихов'
        ],
    '9thGrade':
        [
            'Дмитрий Дёмин',
            'Артём Евсеев',
            'Михаил Захаров',
            'Дмитрий Зыков',
            'Михаил Иванов',
            'Дмитрий Катягин',
            'Кристина Козлова',
            'Александр Кузнецов',
            'Софья Малочка',
            'Елизавета Пуговкина',
            'Артём Садовин',
            'Павел Северин',
            'Кирилл Сидоркин',
            'Николай Стариков',
            'Семён Талипов',
            'Николай Усков'
        ],
    '8thGrade':
        [
            'Алёна Баздунова',
            'Кирилл Булыгин',
            'Рафаэль Валиев',
            'Анна Егорова',
            'Тимофей Еренков',
            'Иван Ефремов',
            'Марат Закиров',
            'Анна Зубкова',
            'Анна Зыкова',
            'Никита Иванов',
            'Иван Кашкаров',
            'Татьяна Кочакова',
            'Анастасия Лаптева',
            'Николай Мальков',
            'Дарья Никитина',
            'Егор Пряшников',
            'Тимур Сагдулин',
            'Никита Яшметов'
        ]
}


# счёт минимального количества людей в 1 команде в зависимости от кол-ва команд и кол-во команд, в которых на 1 человек больше, чем это число
def askTeamCount(Dictionary):
    print('Введите количесво команд')
    TeamsCount = int(input())
    AllPeople = 0

    for InfotechClass in Dictionary.values():
        AllPeople += len(InfotechClass)

    print('Получилось', TeamsCount, 'команд(ы), в которых минимум по', AllPeople // TeamsCount, 'человек(а).\n')
    return AllPeople // TeamsCount, AllPeople % TeamsCount


# печать класса(с 8 по 11) из значений словаря
def printListFromDict(Dictionary, number):
    allClasses = list(Dictionary.values())

    for i in range(1, (len(allClasses[number - 8])) + 1):
        print(str(i) + '. ' + allClasses[number - 8][i - 1])


# опрос пользователей, которые не должны быть вместе
def seperatedStudents(Dictionary):
    friends = {}
    answers = []

    while True:
        print(
            'Чтобы составить пары, которые не могут быть в 1 команде, необходимо их выбрать.\nЧтобы выбрать человека, необходимо ввести номер класса его обучения.\nЕсли все такие пары уже введены, то введите "END."')
        s = input()

        if s == 'END.':
            print('Все составленные пары:')
            if answers == []:
                print('Пар нет!\n')
            for pair in answers:
                print(pair[0], '-', pair[1])
            break
        elif s == '8' or s == '9' or s == '10' or s == '11':
            s = int(s) - 8
            print('Ученики', s + 8, 'класса:')
            printListFromDict(Dictionary, s + 8)
            print(
                '\nЕсли вы ошиблись номером класса, напишите любую строку типа String\nВыберите номер ученика, к которому хотите подобрать пару.')
            student = input()

            if student.isdigit():
                student = int(student)
            else:
                print('Создание пары начинается сначала.\n')
                continue

            print('Вы выбрали ученика', s + 8, 'класса', list(Dictionary.values())[s][student - 1],
                  '\n\nТеперь выберите этому ученику пару.\nВведите класс обучения этого ученика.')

            while True:
                r = input()
                if r == '8' or r == '9' or r == '10' or r == '11':
                    r = int(r) - 8
                    print('Ученики', r + 8, 'класса:')
                    printListFromDict(Dictionary, r + 8)
                    print(
                        '\nЕсли вы ошиблись номером класса, напишите строку типа String\nВыберите номер ученика, которого хотите поставить в пару с учеником "' + str(
                            list(Dictionary.values())[s][student - 1]) + '"')
                    pair = input()

                    if pair.isdigit():
                        pair = int(pair)
                    else:
                        print('Подберите ученику', list(Dictionary.values())[s][student - 1],
                              'пару. Для этого выберите класс его обучения')
                        continue

                    print('\nВы создали пару', list(Dictionary.values())[s][student - 1], 'и',
                          list(Dictionary.values())[r][pair - 1], '\n\n')

                    if list(Dictionary.values())[s][student - 1] in friends:
                        friends[list(Dictionary.values())[s][student - 1]].append(
                            list(Dictionary.values())[r][pair - 1])
                    else:
                        friends[list(Dictionary.values())[s][student - 1]] = [list(Dictionary.values())[r][pair - 1]]

                    if list(Dictionary.values())[r][pair - 1] in friends:
                        friends[list(Dictionary.values())[r][pair - 1]].append(
                            list(Dictionary.values())[s][student - 1])
                    else:
                        friends[list(Dictionary.values())[r][pair - 1]] = [list(Dictionary.values())[s][student - 1]]

                    answers.append([list(Dictionary.values())[s][student - 1], list(Dictionary.values())[r][pair - 1]])
                    break
                else:
                    print('\nНеправильный ввод.')
        else:
            print('\nНеправильный ввод.')

    return friends


# опрос учеников, которые должны быть в 1 команде
def toTheSameTeam(Dictionary):
    teammates = {}
    answers = []

    while True:
        print(
            'Чтобы составить пары, которые должны быть в 1 команде, необходимо их выбрать.\nЧтобы выбрать человека, необходимо ввести номер класса его обучения.\nЕсли все такие пары уже введены, то введите "END."')
        s = input()

        if s == 'END.':
            print('Все составленные пары:')
            if answers == []:
                print('Пар нет!\n')
            for pair in answers:
                print(pair[0], '-', pair[1])
            break
        elif s == '8' or s == '9' or s == '10' or s == '11':
            s = int(s) - 8
            print('Ученики', s + 8, 'класса:')
            printListFromDict(Dictionary, s + 8)
            print(
                '\nЕсли вы ошиблись номером класса, напишите любую строку типа String\nВыберите номер ученика, к которому хотите подобрать пару.')
            student = input()

            if student.isdigit():
                student = int(student)
            else:
                print('Создание пары начинается сначала.\n')
                continue

            print('Вы выбрали ученика', s + 8, 'класса', list(Dictionary.values())[s][student - 1],
                  '\n\nТеперь выберите этому ученику пару.\nВведите класс обучения этого ученика.')

            while True:
                r = input()
                if r == '8' or r == '9' or r == '10' or r == '11':
                    r = int(r) - 8
                    print('Ученики', r + 8, 'класса:')
                    printListFromDict(Dictionary, r + 8)
                    print(
                        '\nЕсли вы ошиблись номером класса, напишите строку типа String\nВыберите номер ученика, которого хотите поставить в пару с учеником "' + str(
                            list(Dictionary.values())[s][student - 1]) + '"')
                    pair = input()

                    if pair.isdigit():
                        pair = int(pair)
                    else:
                        print('Подберите ученику', list(Dictionary.values())[s][student - 1],
                              'пару. Для этого выберите класс его обучения')
                        continue

                    print('\nВы создали пару', list(Dictionary.values())[s][student - 1], 'и',
                          list(Dictionary.values())[r][pair - 1], '\n\n')

                    if list(Dictionary.values())[s][student - 1] in teammates:
                        teammates[list(Dictionary.values())[s][student - 1]].append(
                            list(Dictionary.values())[r][pair - 1])
                    else:
                        teammates[list(Dictionary.values())[s][student - 1]] = [list(Dictionary.values())[r][pair - 1]]

                    if list(Dictionary.values())[r][pair - 1] in teammates:
                        teammates[list(Dictionary.values())[r][pair - 1]].append(
                            list(Dictionary.values())[s][student - 1])
                    else:
                        teammates[list(Dictionary.values())[r][pair - 1]] = [list(Dictionary.values())[s][student - 1]]

                    answers.append([list(Dictionary.values())[s][student - 1], list(Dictionary.values())[r][pair - 1]])
                    break
                else:
                    print('\nНеправильный ввод.')
        else:
            print('\nНеправильный ввод.')

    return teammates


# создание команд
def makeTeams(Dictionary, numberOfTeams):
    teamFlag = 0
    classFlag = 0

    teams = [[] for _ in range(numberOfTeams)]
    while classFlag < len(Dictionary.keys()):
        ClassOfPeople = list(Dictionary.values())[classFlag]

        while len(ClassOfPeople) != 0:
            student = choice(ClassOfPeople)

            ClassOfPeople.remove(student)
            student += ' ' + str(11 - classFlag) + ' класс'
            teams[teamFlag].append(student)
            teamFlag = (teamFlag + 1) % numberOfTeams

        classFlag += 1

    return teams


# печать команд(на вход двумерный список, в каждом элементе которого строки по типу "ФИ ученика класс обучения")
def printTeams(listOfTeams):
    for i in range(1, len(listOfTeams) + 1):
        print(i, 'команда:')

        for j in range(1, len(listOfTeams[i - 1]) + 1):
            print(str(j) + '. ' + str(listOfTeams[i - 1][j - 1]))

        print('\n')


# main
def main():
    print('Введите количество команд')
    NumOfTeams = int(input())

    print('Составленные команды:')
    printTeams(makeTeams(students, NumOfTeams))


main()
