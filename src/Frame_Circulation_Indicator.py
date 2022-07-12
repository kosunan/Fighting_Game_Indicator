g_bar_num = 0
g_bar_flag = 0
g_bar80_flag = 0
g_bar_max_flag = 0

g_interval = 0
g_interval_value = 0
g_interval_max_flag = 0

g_bar_range = 80
g_bar_ini_flag = 0
g_bar_ini_flag_1 = 0
g_bar_ini_flag_2 = 0

g_bar_list_P1["", "", "", "", "", "", "", "", "", ""]
g_bar_list_P2["", "", "", "", "", "", "", "", "", ""]
g_bar_list_P3["", "", "", "", "", "", "", "", "", ""]
g_bar_list_P4["", "", "", "", "", "", "", "", "", ""]
g_bar_lists = [g_bar_list_P1,
               g_bar_list_P2,
               g_bar_list_P3,
               g_bar_list_P4]

class Element_info:
    def __init__(self):
        self.flag = 0
        self.num = 0
        self.line = 0


for n in g_bar_list_list:
    for m in n:
        m = list(range(bar_range))

    # 4キャラ分＊１０バー取得


def Frame_Circulation_Indicator(Character_lists, ini_flag):
    global g_bar_num
    global g_bar_max_flag
    global g_interval_value
    global g_bar_lists

    bar_flag = bar_flag_detection(Character_lists):

    if ini_flag == 1:  # ラウンド初期化時のバー初期化
        bar_ini()

    if g_interval_max_flag == 1 and bar_flag == 1:  # インターバル経過後かつ表示し始めバー初期化
        bar_ini()

    if g_bar_num == g_bar_range:
        g_bar_max_flag = 1
        g_bar_num = 0

    if bar_flag == True:
        bar_add(Character_lists)
        g_interval_value = 0

    elif bar_flag == False:

        g_interval_value += 1

        if g_bar_max_flag = 0:  # インターバル問題解決
            interval = 80

        elif g_bar_max_flag = 1:  # インターバル問題解決
            interval = 20

        if g_interval_value >= interval:  # インターバル問題解決
            g_interval_max_flag = 1

        if g_interval_max_flag == 0:
            bar_add(Character_lists)

    return g_bar_lists


def bar_flag_detection(Character_lists):
    Character_lists[0]
    Character_lists[1]

    if info_data.p1.action_flag == 1:
        return 1

    if info_data.p2.action_flag == 1:
        return 1

    return 0


def bar_ini():
    global g_bar_max_flag
    global g_bar_num
    global g_interval_value
    global g_bar_lists

    g_bar_max_flag = 0
    g_bar_num = 0
    g_interval_value = 0

    for bar_list in g_bar_lists:
        for bar_grain in bar_list:
            for i in bar_grain:
                i = ""


def bar_add(Character_lists):
    global g_bar_lists

    if stop_flag == 0:
        g_bar_num += 1

    for data, bar_list in zip(Character_lists, g_bar_lists):

        bar_list[g_bar_num] = create_grain(data)


def text_font(rgb):
    Text_font_str = "\x1b[38;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m"
    return Text_font_str


def bg_font(rgb):
    bg_font_str = "\x1b[48;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m"
    return bg_font_str


def get_font(text_rgb, bg_rgb):
    return text_font(text_rgb) + bg_font(bg_rgb)


def create_grain(info_data):

    for p_data in info_data

    bar_grain = ["", "", "", "", "", "", "", "", "", ""]

    for n in p_data
    if n.flag == 1:
        font = get_font(n.font_coler)
        num = n.num
        bar_grain[n.line] = font + num.rjust(2, " ")[-2:]

    return bar_grain
