from config import MOUSE_SPEED

MOUSE_UP_KEY = 'mouse_up_key'
MOUSE_DOWN_KEY = 'mouse_down_key'
MOUSE_LEFT_KEY = 'mouse_left_key'
MOUSE_RIGHT_KEY = 'mouse_right_key'
MOUSE_CLICK_KEY = 'mouse_left_click'
MOUSE_KEYS = [MOUSE_UP_KEY, MOUSE_DOWN_KEY, MOUSE_LEFT_KEY, MOUSE_RIGHT_KEY, MOUSE_CLICK_KEY]

class VirtualMouse:
    _CALLBACK = None

    @staticmethod
    def left_click():
        pyautogui.leftclick(500, 500)

    @staticmethod
    def _move_down():
        pyautogui.moveRel(0, 1 * MOUSE_SPEED)

    @staticmethod
    def _move_up():
        pyautogui.moveRel(0, -1 * MOUSE_SPEED)

    @staticmethod
    def _move_left():
        pyautogui.moveRel(-1 * MOUSE_SPEED, 0)

    @staticmethod
    def _move_right():
        pyautogui.moveRel(1 * MOUSE_SPEED, 0)

    @classmethod
    def hold_down(cls):
        cls._CALLBACK = VirtualMouse._move_down

    @classmethod
    def hold_up(cls):
        cls._CALLBACK = VirtualMouse._move_up

    @classmethod
    def hold_left(cls):
        cls._CALLBACK = VirtualMouse._move_left

    @classmethod
    def hold_right(cls):
        cls._CALLBACK = VirtualMouse._move_right

    @classmethod
    def clear(cls):
        cls._CALLBACK = None

    @classmethod
    def run_callback(cls):
        if cls._CALLBACK:
            cls._CALLBACK()
