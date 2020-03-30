import numpy as np


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1, 100)
    while number != predict:
        count += 1
        if number >= predict + 25:
            predict += 25
        elif number >= predict + 20:
            predict += 20
        elif number >= predict + 15:
            predict += 15           
        elif number >= predict + 10:
            predict += 10
        elif number >= predict + 5:
            predict += 5
        elif number >= predict + 3:
            predict += 3
        elif number >= predict:
            predict += 1

        elif number + 25 <= predict:
            predict -= 25
        elif number + 20 <= predict:
            predict -= 20
        elif number + 15 <= predict:
            predict -= 15    
        elif number + 10 <= predict:
            predict -= 10
        elif number + 5 <= predict:
            predict -= 5
        elif number + 3 <= predict:
            predict -= 3
        elif number < predict:
            predict -= 1

    return count  # выход из цикла, если угадали


def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
score_game(game_core_v2)