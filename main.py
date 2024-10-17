#
# Made by SG-Products
#

# Нужные библиотеки
import turtle as tl
import time as tm
import keyboard as kb

# Название окна
tl.title('SG Engine')

# Управление
kb.add_hotkey("w", lambda: wmove())
kb.add_hotkey("a", lambda: amove())
kb.add_hotkey("s", lambda: smove())
kb.add_hotkey("d", lambda: dmove())
kb.add_hotkey("e", lambda: home())
kb.add_hotkey("1", lambda: redcolor())
kb.add_hotkey("2", lambda: bluecolor())
kb.add_hotkey("3", lambda: greencolor())
kb.add_hotkey("4", lambda: yellowcolor())
kb.add_hotkey("5", lambda: blackcolor())
kb.add_hotkey("q", lambda: safe())

# Персонаж
tl.color('yellow')
tl.width(5)

# Передвижение
def wmove():
	tl.forward(1)

def amove():
	tl.right(1)

def smove():
	tl.backward()

def dmove():
	tl.left(1)

def home():
	tl.home()

def redcolor():
	tl.color('red')

def bluecolor():
	tl.color('blue')

def greencolor():
	tl.color('green')

def yellowcolor():
	tl.color('yellow')

def blackcolor():
	tl.coloe('black')

def safe():
	tl.goto(0,0)
