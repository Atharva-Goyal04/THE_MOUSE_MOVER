import random, pyautogui, time, os

x = random.randint(500, 500)
y = random.randint(500, 700)

mins = 120
times = 0
os.system("CLS")
print("__Welcome to mouse mover__")

while mins > times:
    time.sleep(60)
    pyautogui.moveTo(x, y, 0.5)
    pyautogui.click()
    times += 1
    os.system("CLS")
    print("****** PROGRAMME RUNNING ******")
    print("\nProgramme has been running for: ", times, 'mins' )
    # print("Time remaining for programme to end: ", mins - times, 'mins')
