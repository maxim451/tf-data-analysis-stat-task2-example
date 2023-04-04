import pandas as pd
import numpy as np

from scipy.stats import t as t_student, expon


chat_id = 436801091 # Ваш chat ID, не меняйте название переменной

def confidence_interval(alpha, arr):
    n = len(arr)
    t_alpha_2 = t_student.ppf(1 - alpha/2, n-1)
    s = np.std(arr, ddof=1)
    lambda_ = s/np.mean(arr)
    a = np.mean(arr) - t_alpha_2*s/np.sqrt(n*(n-1))*np.sqrt(lambda_+1/4*n*lambda_**2)
    b = np.mean(arr) + t_alpha_2*s/np.sqrt(n*(n-1))*np.sqrt(lambda_+1/4*n*lambda_**2)
    return (a, b)

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    alpha = 1 - p
   
    # Оцениваем параметр экспоненциального распределения
    lambda_ = 1/np.mean(x)
    # Генерируем n наблюдений из экспоненциального распределения
    exp_arr = expon.rvs(scale=1/lambda_, size=n)
    # Добавляем их к массиву измерений
    '''
    error = np.exp(1)
    exp_arr = np.random.normal(1/2, error, size=n)
    '''
    arr_with_errors = x + exp_arr
    #x= (at^2)/2 a= 2*x/t^2
    # Симметричный доверительный интервал для коэффициента ускорения
    conf_int = confidence_interval(alpha, (arr_with_errors*2)/65**2)
    return (conf_int)
'''
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
p = 0.95
arr = [100.5, 105.2, 101.1, 99.8, 97.3, 103.7, 98.6, 104.8, 99.9]


print(solution(p,arr))

'''