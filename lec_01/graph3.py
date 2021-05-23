import matplotlib.pyplot as plt
import numpy as np

plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
with plt.xkcd():
    plt.pie([eval(input()), eval(input()), eval(input()), eval(input())], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
    plt.title('Где ведутся самые ожесточенные бои')

plt.show()