import pyautogui
import time
print("Starting KiwiSDR Scanner")
time.sleep(10)
pyautogui.moveTo(681, 408)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1193, 589)
pyautogui.click()
time.sleep(1)
for number in range(1000):
    pyautogui.moveTo(1193, 589)
    pyautogui.click()

print("DONE")
