from ctypes import windll, wintypes, byref
import time

G_BAR_RANGE = 80

g_bar_num = 0
g_bar_max_flag = 0
g_interval = 0
g_interval_value = 81
g_interval_max_flag = 0


g_circulat_data = [[""] * 10 for i in range(10)]
g_characters_elements_bar = [[""] * 10 for i in range(4)]


def frame_circulation_indicator(characters_elements, characters_debug_elements, stop_flag, debug_flag):

    global g_bar_num
    global g_bar_max_flag
    global g_interval_value
    global g_characters_elements_bar
    global g_interval_max_flag
    global g_circulat_data
    view_data = ""
    debug_data = ""
    add_flag = 0
    p1 = characters_elements[0]
    p2 = characters_elements[1]

    bar_flag = bar_flag_detection(p1, p2)

    if bar_flag == 1:
        add_flag = 1
        g_interval_value = 0

        if g_interval_max_flag == 1:  # インターバル経過後初期化
            bar_ini()

    elif bar_flag == 0:
        g_interval_value += 1

        if g_bar_max_flag == 0:
            interval = 80

        elif g_bar_max_flag == 1:
            interval = 20

        if g_interval_value >= interval:  # インターバル問題解決
            g_interval_max_flag = 1

        if g_interval_max_flag == 0:
            add_flag = 1

    if add_flag == 1:
        if stop_flag == 0:
            g_bar_num += 1

            if g_bar_num == G_BAR_RANGE:
                g_bar_num = 0
                g_bar_max_flag = 1

        if debug_flag == 0:
            characters_debug_elements = []

        bar_add(characters_elements, characters_debug_elements, stop_flag, debug_flag)

        view_data, debug_data = view_data_cre(g_characters_elements_bar)

    elif add_flag == 0:
        view_data, debug_data = view_data_cre(g_characters_elements_bar)

    return view_data, debug_data


def bar_add(characters_elements, characters_debug_elements, stop_flag, debug_flag):

    global g_characters_elements_bar
    global g_bar_max_flag
    line_num = len(g_characters_elements_bar[0])

    if debug_flag == 1:
        p_num = 4
    else:
        p_num = 2

    for p in range(p_num):
        font_list = ["\x1b[38;2;092;092;092m\x1b[48;2;025;025;025m"] * 10
        num_list = ["  \x1b[0m"] * 10

        for el in characters_elements[p]:
            if el.val == 1:
                num_list[el.line] = str(el.num).rjust(2, " ")[-2:] + '\x1b[0m'
                font_list[el.line] = str(el.font_coler)

        if debug_flag == 1:
            for el in characters_debug_elements[p]:
                num_list[el.line] = str(el.num).rjust(2, " ")[-2:] + '\x1b[0m'
                font_list[el.line] = str(el.font_coler)

        for line in range(line_num):
            if stop_flag == 0:
                g_characters_elements_bar[p][line] += (font_list[line] + num_list[line])

            elif stop_flag == 1:
                g_characters_elements_bar[p][line] = g_characters_elements_bar[p][line][0:-44] + (font_list[line] + num_list[line])

            str_len = len(g_characters_elements_bar[p][line])

            if str_len >= 3521:
                g_characters_elements_bar[p][line] = g_characters_elements_bar[p][line][44:str_len]


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
    global g_circulat_data

    g_bar_max_flag = 0
    g_bar_num = 0
    g_interval_value = 81
    g_interval_max_flag = 0

    g_characters_elements_bar = [[""] * 10 for i in range(4)]
    g_circulat_data = [[""] * 10 for i in range(10)]


def view_data_cre(list):
    bar_p1 = list[0]
    bar_p2 = list[1]
    bar_p3 = list[2]
    bar_p4 = list[3]

    font = get_font((255, 255, 255), (255, 0, 0))

    END = '\x1b[0m\x1b[49m\x1b[K\x1b[1E'
    state_str = ''
    state_str += '  |'
    under_line = '\x1b[4m'
    flag = 0
    for i in range(1, 81):
        n_1 = str(i).rjust(2, " ")[0:1]
        n_2 = str(i).rjust(2, " ")[1:2]

        if n_2 != "0":
            n_1 = " "

            font = get_font((150, 150, 150),  (0, 0, 0))
        elif n_2 == "0":

            font = get_font((255, 255, 255), (0, 0, 0))

        state_str += under_line + font + n_1 + n_2 + '\x1b[0m'

    state_str += '\x1b[0m' + END
    # state_str += ' 1 2 3 4 5 6 7 8 91011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980' + '\x1b[0m' + END
    state_str += '1P|' + bar_p1[0] + END
    state_str += '  |' + bar_p1[1] + END

    state_str += '2P|' + bar_p2[0] + END
    state_str += '  |' + bar_p2[1] + END

    debug_str = '\x1b[1F'
    debug_str = ''
    debug_str += '3P|' + bar_p3[0] + END
    debug_str += '  |' + bar_p3[1] + END

    debug_str += '4P|' + bar_p4[0] + END
    debug_str += '  |' + bar_p4[1] + END

    debug_str += '1P|' + bar_p1[2] + END
    debug_str += '1P|' + bar_p1[3] + END
    debug_str += '1P|' + bar_p1[4] + END
    debug_str += '1P|' + bar_p1[5] + END
    debug_str += '1P|' + bar_p1[6] + END
    debug_str += '1P|' + bar_p1[7] + END
    debug_str += '1P|' + bar_p1[8] + END
    debug_str += '1P|' + bar_p1[9] + END

    debug_str += '2P|' + bar_p2[2] + END
    debug_str += '2P|' + bar_p2[3] + END
    debug_str += '2P|' + bar_p2[4] + END
    debug_str += '2P|' + bar_p2[5] + END
    debug_str += '2P|' + bar_p2[6] + END
    debug_str += '2P|' + bar_p2[7] + END
    debug_str += '2P|' + bar_p2[8] + END
    debug_str += '2P|' + bar_p2[9] + END

    return state_str, debug_str


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


def text_font(rgb):
    Text_font_str = "\x1b[38;2;" + str(rgb[0]).rjust(3, "0")[-3:] + ";" + str(rgb[1]).rjust(3, "0")[-3:] + ";" + str(rgb[2]).rjust(3, "0")[-3:] + "m"
    return Text_font_str


def bg_font(rgb):
    bg_font_str = "\x1b[48;2;" + str(rgb[0]).rjust(3, "0")[-3:] + ";" + str(rgb[1]).rjust(3, "0")[-3:] + ";" + str(rgb[2]).rjust(3, "0")[-3:] + "m"
    return bg_font_str


def get_font(text_rgb, bg_rgb):
    return text_font(text_rgb) + bg_font(bg_rgb)
