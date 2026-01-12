import time
import random
from pynput.keyboard import Controller, Key
import messages

MIN_INTERVAL = 5    
MAX_INTERVAL = 15 

keyboard = Controller()

print("Chaliy suru krte hai!")
time.sleep(3)

minute = int(input("How long this should run? Tell me duration in minutes: "))
start_time = time.time()
MAX_RUN_TIME = 60*minute

try:
    while True:
        if time.time() - start_time >= MAX_RUN_TIME:
            break
        keyboard.press(Key.caps_lock)
        keyboard.release(Key.caps_lock)
        msg = random.choice(messages.messages)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(f"{current_time} - {msg}")

        sleep_time = random.randint(MIN_INTERVAL, MAX_INTERVAL)
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("\nBss ho gya kya?")