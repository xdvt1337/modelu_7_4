# Использование %:

# 1
print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': 5})

# 2
print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': 5, 'team2_num': 6})

# Использование format():

#1
print('Команда Волшебники данных решила задач: {score_2}'.format(score_2= 42))

#2
print('Волшебники данных решили задачи за {team1_time}'.format(team1_time= 18015.2)+' с!')

# Использование f-строк:
# 1
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

# 2
team1_time = 1552.512
team2_time = 2153.31451

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}!')

# 3
tasks_total = 82
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

