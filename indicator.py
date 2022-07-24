from ctypes import windll, wintypes, byref
import time
import cfg_tl
cfg = cfg_tl
g_bar_num = 0
g_bar_max_flag = 0
g_interval = 0
g_interval_value = 81
g_interval_max_flag = 0
g_bar_range = 80

g_bars_num = 10
g_bar_lists = []
g_font_data_list = [[""] * 10 for i in range(4)]
# 格納スペース
g_characters_elements_bar = [[[""] * g_bar_range for i in range(10)] for j in range(4)]


def frame_circulation_indicator(characters_elements, stop_flag, circulat_data):

    global g_bar_num
    global g_bar_max_flag
    global g_interval_value
    global g_characters_elements_bar
    global g_interval_max_flag
    global g_bar_lists
    add_flag = 0
    p1 = characters_elements[0]
    p2 = characters_elements[1]

    bar_flag = bar_flag_detection(p1, p2)

    if bar_flag == 1:
        add_flag = 1
        g_interval_value = 0

        if g_interval_max_flag == 1:  # インターバル経過後初期化
            circulat_data = bar_ini()

    elif bar_flag == 0:
        g_interval_value += 1

        if g_bar_max_flag == 0:
            interval = 60

        elif g_bar_max_flag == 1:
            interval = 20

        if g_interval_value >= interval:  # インターバル問題解決
            g_interval_max_flag = 1

        if g_interval_max_flag == 0:
            add_flag = 1

    if add_flag == 1:
        if stop_flag == 0:
            g_bar_num += 1

            if g_bar_num == g_bar_range:
                g_bar_num = 0
                g_bar_max_flag = 1

        bar_add(characters_elements, stop_flag)

        for p_index, p in zip(g_characters_elements_bar, range(4)):
            for line_index, line in zip(p_index, range(10)):
                index = g_bar_num + 1
                circulat_data[p][line] = ""
                for nnn in range(80):
                    if index >= 80:
                        index = 0
                    circulat_data[p][line] = circulat_data[p][line] + line_index[index]
                    index += 1

        return circulat_data

    elif add_flag == 0:

        return circulat_data


def bar_add(characters_elements, stop_flag):

    global g_characters_elements_bar
    global g_bar_max_flag
    global g_font_data_list

    index = 0
    max_len = len(g_characters_elements_bar[0])

    for p_index in range(4):
        for m in range(max_len):
            g_characters_elements_bar[p_index][m][g_bar_num] = "\x1b[38;2;92;92;92m\x1b[48;2;25;25;25m  \x1b[0m"

        elements = characters_elements[p_index]
        for el in elements:
            if el.val == 1:
                font = el.font_coler
                num = str(el.num)
                g_characters_elements_bar[p_index][el.line][g_bar_num] = font + num.rjust(2, " ")[-2:] + '\x1b[0m'



def bar_flag_detection(p1_elements_data, p2_elements_data):

    for n in p1_elements_data:
        if n.val == 1:
            return 1

    for n in p2_elements_data:
        if n.val == 1:
            return 1

    return 0


def bar_ini():
    global g_bar_max_flag
    global g_bar_num
    global g_interval_value
    global g_characters_elements_bar
    global g_interval_max_flag

    g_bar_max_flag = 0
    g_bar_num = 0
    g_interval_value = 81
    g_interval_max_flag = 0

    g_characters_elements_bar = [[[""] * 80 for i in range(10)] for j in range(4)]
    circulat_data = [[""] * 10 for i in range(10)]

    return circulat_data


def ex_cmd_enable():
    INVALID_HANDLE_VALUE = -1
    STD_INPUT_HANDLE = -10
    STD_OUTPUT_HANDLE = -11
    STD_ERROR_HANDLE = -12
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    ENABLE_LVB_GRID_WORLDWIDE = 0x0010

    hOut = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    if hOut == INVALID_HANDLE_VALUE:
        return False
    dwMode = wintypes.DWORD()
    if windll.kernel32.GetConsoleMode(hOut, byref(dwMode)) == 0:
        return False
    dwMode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    # dwMode.value |= ENABLE_LVB_GRID_WORLDWIDE
    if windll.kernel32.SetConsoleMode(hOut, dwMode) == 0:
        return False
    return True
