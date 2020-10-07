# coding=utf-8
#DS study. Student: Chumak Ivan Module_0

import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number):
    '''Сначала устанавливаем любое random число в диапазоне. Для угадывания'''
    '''применяем метод "плюс-минус половина"-заданный диапазон разбивается'''
    '''на две части (по возможности равные) и сравниваем загаданное число '''
    '''с краями диапазона. В результате устанавливаем подходящую половину, '''
    '''переопределяем половину края диапазона и повторяем операцию'''
    
    range_top_limit = 101                   # верхняя граница диапазона
    count = 0                               # счетчик кол-ва попыток
    range_start = 1                         # стартовое значение текущего диапазона
    range_end = range_top_limit             # конечное значение текущего диапазона
    predict = range_start + range_end//2    # стартовое предсказание - середина известного диапазона
    
    while number != predict or count > range_top_limit: # ограничение от бесконечного цикла
        count += 1
        if number > predict: 
            range_start = predict   # загаданное число "правее" предложенного - передвигаем старт диапазона
        elif number < predict: 
            range_end = predict     # загаданное число "левее" предложенного - передвигаем конец диапазона
        predict = range_start + (range_end-range_start)//2 # вычисляем новое "предсказание"
        
    return count # выход из цикла, если угадали


score_game(game_core_v3)
