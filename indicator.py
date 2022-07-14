g_bar_num = 0
g_bar_max_flag = 0
g_interval = 0
g_interval_value = 0
g_interval_max_flag = 0
g_bar_range = 80
g_bars_num = 10

g_character_elements_bar = list(range(4))

for n in range(4):
    g_character_elements_bar[n] = list(range(10))

g_characters_elements_bar = [g_character_elements_bar[0],
                             g_character_elements_bar[1],
                             g_character_elements_bar[2],
                             g_character_elements_bar[3]
                             ]


class Element_data:
    def __init__(self):
        self.flag = 0
        self.num = 0
        self.line = 0


def frame_circulation_indicator(Characters_elements_data, ini_flag, stop_flag):
    global g_bar_num
    global g_bar_max_flag
    global g_interval_value
    global g_characters_elements_bar

    bar_flag = bar_flag_detection(Characters_elements_data)

    if ini_flag == 1:  # ラウンド初期化時のバー初期化
        bar_ini()

    if bar_flag == 1 and g_interval_max_flag == 1:  # インターバル経過後初期化
        bar_ini()

    if g_bar_num == g_bar_range:
        g_bar_max_flag = 1
        g_bar_num = 0

    if bar_flag == 1:
        bar_add(Characters_elements_data, stop_flag)
        g_interval_value = 0

    elif bar_flag == 0:

        g_interval_value += 1

        if g_bar_max_flag == 0:
            interval = 80

        elif g_bar_max_flag == 1:
            interval = 20

        if g_interval_value >= interval:  # インターバル問題解決
            g_interval_max_flag = 1

        if g_interval_max_flag == 0:
            bar_add(Characters_elements_data, stop_flag)

    return g_bar_lists


def bar_flag_detection(Characters_elements_data):

    p1_elements_data = Characters_elements_data[0]
    p2_elements_data = Characters_elements_data[1]

    for element_grain_data in p1_elements_data:
        if element_grain_data.flag == 1:
            return 1

    for element_grain_data in p2_elements_data:
        if element_grain_data.flag == 1:
            return 1

    return 0


def bar_ini():
    global g_bar_max_flag
    global g_bar_num
    global g_interval_value
    global g_characters_elements_bar

    g_bar_max_flag = 0
    g_bar_num = 0
    g_interval_value = 0

    for elements_bar in g_characters_elements_bar:
        for element_bar in elements_bar:
            for grain in element_bar:
                grain = ""


def bar_add(characters_elements_data, stop_flag):
    global g_characters_elements_bar

    if stop_flag == 0:
        g_bar_num += 1

    for elements_data, elements_bar in zip(characters_elements_data, g_characters_elements_bar):

        elements_bar[g_bar_num] = create_elements(elements_data)


def text_font(rgb):
    Text_font_str = "\x1b[38;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m"
    return Text_font_str


def bg_font(rgb):
    bg_font_str = "\x1b[48;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m"
    return bg_font_str


def get_font(text_rgb, bg_rgb):
    return text_font(text_rgb) + bg_font(bg_rgb)


def create_elements(elements_data):

    elements = ["", "", "", "", "", "", "", "", "", ""]

    for element_data in elements_data:
        if element_data.flag == 1:
            font = get_font(element_data.font_coler)
            num = element_data.num
            elements[element_data.line] = font + num.rjust(2, " ")[-2:]

    return elements

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
