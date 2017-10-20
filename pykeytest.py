from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

print('it worked')

time.sleep(5)

k.press_key(k.alt_key)
k.press_key(k.shift_key)
k.tap_key('.')
k.release_key(k.shift_key)
k.release_key(k.alt_key)


