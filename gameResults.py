'''Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит
на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6'''


def game_result(game):  # подсчет результата игры

    # создаем словарь по счету игры {команда: голы}
    score = {}
    for i in range(0, len(game) - 1):
        if not game[i].isdigit():
            score[game[i]] = int(game[i + 1])
            # создаем список команд матча
    lst = [i for i in score.keys()]

    # проверяем победителя либо ничью, добавляем количество побед, поражений или ничьих
    if score[lst[0]] > score[lst[1]]:
        wins[lst[0]] += 1
        loses[lst[1]] += 1
    elif score[lst[0]] == score[lst[1]]:
        draws[lst[0]] += 1
        draws[lst[1]] += 1
    else:
        wins[lst[1]] += 1
        loses[lst[0]] += 1


numb_games = int(input())  # кол-во игр
games = []
# ввод результатов игры в формате 'команда1;голов;команда2;голов'
for game in range(0, numb_games):
    games += [input().split(';')]

# формируем список команд, учавствовавших в играх
teams = []
for game in games:
    for i in game:
        if not i.isdigit() and i not in teams:
            teams += [i]

# Словарь {команда: кол-во проведенных игр}
game_count = {}
for team in teams:
    count = 0
    for game in games:
        if team in game:
            count += 1
    game_count[team] = count

# Словари для кол-ва побед, поражений, ничьих и очков
wins = {team: 0 for team in teams}
loses = {team: 0 for team in teams}
draws = {team: 0 for team in teams}
points = {team: 0 for team in teams}
scores = {team: 0 for team in teams}

# подсчитываем результат каждой игры
for i in range(0, len(games)):
    game_result(games[i])

# по кол-ву побед и ничьих подсчитываем очки команд
for team in scores:
    scores[team] = (wins[team] * 3) + (draws[team] * 1)

# вывод
for team in teams:
    print(team + ':', end='')
    print(game_count[team], wins[team], draws[team], loses[team], scores[team])
