import win32con
import json
import os
import chardet

window_title = "umamusume"
key_mapping = {}
ratio = 0, 0

byte_to_key = {
    win32con.VK_BACK: "BACKSPACE", win32con.VK_TAB: "TAB", win32con.VK_CLEAR: "CLEAR",
    win32con.VK_RETURN: "ENTER", win32con.VK_SHIFT: "SHIFT", win32con.VK_CONTROL: "CTRL",
    win32con.VK_MENU: "ALT", win32con.VK_PAUSE: "PAUSE", win32con.VK_CAPITAL: "CAPS_LOCK",
    win32con.VK_ESCAPE: "ESC", win32con.VK_SPACE: "SPACEBAR", win32con.VK_PRIOR: "PAGE_UP",
    win32con.VK_NEXT: "PAGE_DOWN", win32con.VK_END: "END", win32con.VK_HOME: "HOME",
    win32con.VK_LEFT: "LEFT_ARROW", win32con.VK_UP: "UP_ARROW", win32con.VK_RIGHT: "RIGHT_ARROW",
    win32con.VK_DOWN: "DOWN_ARROW", win32con.VK_SNAPSHOT: "PRINT_SCREEN", win32con.VK_INSERT: "INSERT",
    win32con.VK_DELETE: "DELETE", win32con.VK_NUMPAD0: "NUMPAD_0", win32con.VK_NUMPAD1: "NUMPAD_1",
    win32con.VK_NUMPAD2: "NUMPAD_2", win32con.VK_NUMPAD3: "NUMPAD_3", win32con.VK_NUMPAD4: "NUMPAD_4",
    win32con.VK_NUMPAD5: "NUMPAD_5", win32con.VK_NUMPAD6: "NUMPAD_6", win32con.VK_NUMPAD7: "NUMPAD_7",
    win32con.VK_NUMPAD8: "NUMPAD_8", win32con.VK_NUMPAD9: "NUMPAD_9", 48: "0", 49: "1", 50: "2",
    51: "3", 52: "4", 53: "5", 54: "6", 55: "7", 56: "8", 57: "9", ord('A'): "A", ord('B'): "B",
    ord('C'): "C", ord('D'): "D", ord('E'): "E", ord('F'): "F", ord('G'): "G", ord('H'): "H",
    ord('I'): "I", ord('J'): "J", ord('K'): "K", ord('L'): "L", ord('M'): "M", ord('N'): "N",
    ord('O'): "O", ord('P'): "P", ord('Q'): "Q", ord('R'): "R", ord('S'): "S", ord('T'): "T",
    ord('U'): "U", ord('V'): "V", ord('W'): "W", ord('X'): "X", ord('Y'): "Y", ord('Z'): "Z",
    win32con.VK_LWIN: "LEFT_WINDOWS", win32con.VK_RWIN: "RIGHT_WINDOWS", win32con.VK_APPS: "CONTEXT_MENU",
    win32con.VK_MULTIPLY: "MULTIPLY", win32con.VK_ADD: "ADD", win32con.VK_SEPARATOR: "SEPARATOR",
    win32con.VK_SUBTRACT: "SUBTRACT", win32con.VK_DECIMAL: "DECIMAL", win32con.VK_DIVIDE: "DIVIDE",
    win32con.VK_F1: "F1", win32con.VK_F2: "F2", win32con.VK_F3: "F3", win32con.VK_F4: "F4",
    win32con.VK_F5: "F5", win32con.VK_F6: "F6", win32con.VK_F7: "F7", win32con.VK_F8: "F8",
    win32con.VK_F9: "F9", win32con.VK_F10: "F10", win32con.VK_F11: "F11", win32con.VK_F12: "F12",
    win32con.VK_F13: "F13", win32con.VK_F14: "F14", win32con.VK_F15: "F15", win32con.VK_F16: "F16",
    win32con.VK_F17: "F17", win32con.VK_F18: "F18", win32con.VK_F19: "F19", win32con.VK_F20: "F20",
    win32con.VK_F21: "F21", win32con.VK_F22: "F22", win32con.VK_F23: "F23", win32con.VK_F24: "F24",
    win32con.VK_NUMLOCK: "NUM_LOCK", win32con.VK_SCROLL: "SCROLL_LOCK", win32con.VK_LSHIFT: "LEFT_SHIFT",
    win32con.VK_RSHIFT: "RIGHT_SHIFT", win32con.VK_LCONTROL: "LEFT_CTRL", win32con.VK_RCONTROL: "RIGHT_CTRL",
    win32con.VK_LMENU: "LEFT_MENU", win32con.VK_RMENU: "RIGHT_MENU", 186: ";",
    107: "+", 188: ",", 109: "-", 190: ".", 191: "/", 192: "`",
    219: "[", 220: "\\", 221: "]", 222: "'"
}

key_to_byte = {v: k for k, v in byte_to_key.items()}

key_mapping = {
    'SPACEBAR': [99,182,0],        # 초록버튼
    '`':     [231, 231, 236],   # 흰 버튼
    'Q':     [124, 203, 42],    # 휴식
    'W':     [41, 122, 207],    # 트레이닝
    'E':     [40, 191, 214],    # 스킬
    'R':     [247, 154, 8],     # 외출
    'F':     [145, 96, 239],    # 양호실
    'T':     [235, 55, 55],     # 여신
    'G':     [244, 69, 137],    # 레이스
    'NUMPAD_0':   'MAC',        # 훈련 돌아보기 1
    'A':    [225, 255, 178],    # 1번 선택지
    'S':    [255, 247, 192],    # 2번 선택지
    'D':    [255, 228, 239],    # 3번 선택지
    '/':    (730, 1330),
    "TAB": "drag (20, 1230) (788, 1230)", # 훈련 돌아보기 2
    "1": "(130, 1310)",
    "2": "(280, 1310)",
    "3": "(430, 1310)",
    "4": "(580, 1310)",
    "5": "(630, 1310)"
}

screen_size = {
    'x': 808,
    'y': 1453
}

support_key = ["BACKSPACE, TAB, CLEAR, ENTER, SHIFT, CTRL, PAUSE, CAPS_LOCK, ESC, SPACEBAR, PAGE_UP, PAGE_DOWN, ",
            "END, HOME, LEFT_ARROW, UP_ARROW, RIGHT_ARROW, DOWN_ARROW, PRINT_SCREEN, INSERT, DELETE, NUMPAD_0, ",
            "NUMPAD_1, NUMPAD_2, NUMPAD_3, NUMPAD_4, NUMPAD_5, NUMPAD_6, NUMPAD_7, NUMPAD_8, NUMPAD_9, 0, 1, 2, ",
            "3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, ",
            "LEFT_WINDOWS, RIGHT_WINDOWS, CONTEXT_MENU, MULTIPLY, ADD, SEPARATOR, SUBTRACT, DECIMAL, DIVIDE, F1, F2, ",
            "F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, F13, F14, F15, F16, F17, F18, F19, F20, F21, F22, F23, F24, ",
            "NUM_LOCK, SCROLL_LOCK, LEFT_SHIFT, RIGHT_SHIFT, LEFT_CTRL, RIGHT_CTRL, ;, +, ,, ",
            "-, ., /, `, [, \\, ], '"]

mac = "1, sleep 0.1, 2, sleep 0.1, 3, sleep 0.1, 4, sleep 0.1, 5"

text = {
    "RGB": "[0, 0, 0]",
    "POS": "(0, 0)",
    "KEY": "KEY name",
    "DRAG": "drag (from pos) (to pos)",
    "DELAY": "sleep 0.0",
    "MACRO": "MACRO name"
}

def convert_value(value_str : str):
    """
    Converts a string representation of a value to its corresponding Python data type.

    :param value_str: The string representation of the value
    :type value_str: str
    :return: The converted value
    """
    split = value_str[1:-1].split(',')
    # 리스트 형태인 경우
    if value_str.startswith("[") and value_str.endswith("]") and len(split) == 3:
        return [int(x) for x in split]
    # 튜플 형태인 경우
    elif value_str.startswith("(") and value_str.endswith(")") and len(split) == 2:
        return tuple(int(x) for x in split)
    # 키 형태인 경우
    elif key_to_byte.get(value_str) != None:
        return key_to_byte[value_str]
    else:
        return value_str

def load_json() -> None:
    """
    Loads settings from the config file and initializes global variables.

    :return: None
    """
    global key_mapping, ratio, load, window_title, screen_size

    if not os.path.isfile('./config.json'):
        with open('./config.json', 'w') as f:
            save = {key:str(value) for key, value in key_mapping.items()}
            json.dump({"window_title":window_title, "support_key":support_key, "type":text, "key_mapping":save, "screen_size":screen_size, "MAC":mac}, f, indent=4)
    else:
        try:
            with open('./config.json', 'rb') as f:
                raw = f.read()
            with open('./config.json', 'r', encoding=chardet.detect(raw)["encoding"]) as f:
                load = json.load(f)

            if load.get('key_mapping') != None:
                key_mapping = {key:convert_value(value) for key, value in load["key_mapping"].items()}
            if load.get('screen_size') != None:
                screen_size = load["screen_size"]
            if load.get('window_title') != None:
                window_title = load['window_title']
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError("config.json has wrong syntax.", e.doc, e.pos)
        
    ratio = screen_size['x'], screen_size['y']