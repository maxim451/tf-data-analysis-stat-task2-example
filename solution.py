import pandas as pd
import numpy as np

from scipy.stats import t as t_student, chi2


chat_id = 436801091 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    t = 65
    x_sum = np.sum(x)
    alpha = 1 - p

    a = (2/(n*t**2))*x_sum
    e = x - a * t**2 / 2
    S2 = np.sum(e**2) / (n - 1)
    t_quantile = t_student.ppf(1 - alpha / 2, n - 1)
    chi2_quantile = chi2.ppf(1 - alpha / 2, 1)
    left = a - t_quantile * np.sqrt(S2 / (n * t**2)) * np.sqrt(chi2_quantile)
    right = a + t_quantile * np.sqrt(S2 / (n * t**2)) * np.sqrt(chi2_quantile)
    return (left, right)
