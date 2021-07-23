import matplotlib.pyplot as plt

from common.menu import print_menu

'''
list 값은 y축이고, x축은 0부터 1까지 자동으로 증가한다.
'''
def plot_show():
    plt.title("legend")
    plt.plot([10, 20, 30, 40])
    plt.show()


'''
첫번째 list 가 x 축이고, 두번째 list 가 y 축이다.
'''
def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()
'''
그래프에 범례 넣기
'''
def plot_legend():
    plt.title("legend")
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 20, 40], label='desc')
    plt.legend()
    plt.show()
'''
그래프에 선 색 변경
'''
def plot_color():
    plt.title("linestyle")
    plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
    plt.plot([40, 30, 20, 10], 'pink', label='desc')
    plt.legend()
    plt.show()
'''
그래프에 선 모양 바꾸기
'''
def plot_linestyle():
    plt.title("color")
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
    plt.plot([40, 30, 20, 10], color='b', linestyle=':', label='dotted')
    plt.legend()
    plt.show()

'''
그래프에 마커 모양 바꾸기
'''
def plot_marker():
    plt.title("marker")
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'b^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(
            ['exit', 'Plot Show', 'Plot_two_list_show', 'Plot_legend', 'Plot_color', 'Plot_line_style', 'Plot_marker'])
        if menu == 0:
            break
        if menu == 1:
            plot_show()
        if menu == 2:
            plot_two_list_show()
        if menu == 3:
            plot_legend()
        if menu == 4:
            plot_color()
        if menu == 5:
            plot_linestyle()
        if menu == 6:
            plot_marker()