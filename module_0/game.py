#!/usr/bin/python3
import numpy as np

def game_core(number, start=1, end=100):
    '''Ищем заданное число методом деления отрезка пополам'''
    count = 0 # счетчик попыток
    
    while True:
        count += 1
        middle = (start + end) // 2
        
        if (middle == number):
            break
        elif (middle < number):
            start = middle + 1
        else:
            end = middle - 1
       
    return count

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
        
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    
    return(score)

score_game(game_core)
