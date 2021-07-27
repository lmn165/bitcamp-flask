import matplotlib.pyplot as plt
import random


def hist_show(dice: []):
    plt.hist(dice)
    plt.show()


def get_dice(bins: int) -> []:
    return [random.randint(1, 6) for i in range(bins)]


if __name__ == '__main__':
    hist_show(get_dice(int(input(print('생성할 난수 갯수 입력: ')))))
