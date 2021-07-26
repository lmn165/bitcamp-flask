from common.menu import print_menu
from modu.templete.basic_plot import plot_show, plot_two_list_show, plot_legend, plot_color, plot_linestyle, plot_scatter

if __name__ == '__main__':
    while 1:
        menu = print_menu(
            ['exit', 'Plot Show', 'Plot_two_list_show', 'Plot_legend', 'Plot_color', 'Plot_line_style', 'Plot_scatter'])
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
            plot_scatter()