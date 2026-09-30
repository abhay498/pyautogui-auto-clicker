import pyautogui
import time

def auto_move_and_click():
    print("Auto move and click started. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.moveRel(100, 0, duration=0.2)  # Move right
            pyautogui.click()
            time.sleep(0.2)

            pyautogui.moveRel(0, 100, duration=0.2)  # Move down
            pyautogui.click()
            time.sleep(0.2)

            pyautogui.moveRel(-100, 0, duration=0.2)  # Move left
            pyautogui.click()
            time.sleep(0.2)

            pyautogui.moveRel(0, -100, duration=0.2)  # Move up
            pyautogui.click()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    auto_move_and_click()
