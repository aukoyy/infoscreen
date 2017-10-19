from pykeyboard import PyKeyboard
import time

k = PyKeyboard()

# k.tap_key('l',n=2,interval=5)


time.sleep(1)

# k.press_key(k.alt_key)
# k.tap_key(k.tab_key)
# k.release_key(k.alt_key)


k.press_keys([k.windows_l_key, '2'])

time.sleep(1)
#trying to control web player2
k.press_key(k.alt_key)
k.press_key(k.shift_key)
k.tap_key('.')
k.release_key(k.shift_key)
k.release_key(k.alt_key)


# k.tap_key(k.function_keys[11])


# k.press_key(k.control_l_key)
# k.tap_key(k.right_key)
# k.release_key(k.control_l_key)

# k.tab_key(k.space_key)



# https://github.com/PyUserInput/PyUserInput
