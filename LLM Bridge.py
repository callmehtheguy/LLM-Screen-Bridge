import pyautogui
import PIL.Image
import time
import pyperclip
import ast
import ctypes
import re
import keyboard 

SETTINGS = {
    "CONFIDENCE": 0.7,
    "WRITE_INTERVAL": 0.01,
}

SCREEN_REGION = {
    "LEFT": 0,
    "TOP": 0,
    "WIDTH": 0,
    "HEIGHT": 0,
}

ASSETS = {
    "INPUT_BAR": 'ask_ai.png',
    "COPY_BTN": 'copy_text_button.png',
}

DELAYS = {
    "PASTE": 0.5,
    "TAB_SWITCH": 0.1,
    "CLICK_SEQUENCE": 0.1,
    "LOOP_COOLDOWN": 1.0,
    "POST_SEND_PAUSE": 1.5,
}

DO_NOT_TOUCH = {
    "FAILSAFE": True,
    "SCROLL_ATTEMPTS": 152,
    "SCROLL_AMOUNT": -500,
    "DPI_AWARE": True,
    "VERIFY_SEND": 0.8,
    "CLIPBOARD_SYNC": 0.3,
    "SCROLL_PAUSE": 0.5,
    "EMERGENCY_KEY": 'esc',
    "MAX_SEND_RETRIES": 1000,
    "PROMPTS": {
        "STEP_1_MAP": "Send an exact replica of what the screenshot says in your own format - text, table, etc. Also map out every button, number, and text area. List contents and 0-1000 coordinates.",
        "STEP_2_SOLVE": (
            "Based on the mapping, solve the task. ONLY CLICK ON BUTTONS VISIBLE IN THE SCREENSHOT. If you need to see what it looks like after you click something, only click parts you are certain. You will get the next screenshot after. If it involves a dropdown/multi-step question (one with parts A and B), you are only allowed one click."
            "Return ONLY: CLICK_LIST: [[x1, y1], [x2, y2]] (0-1000 scale). "
            "NO EXPLANATION."
        ),
    }
}

if DO_NOT_TOUCH["DPI_AWARE"]:
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except:
            pass

try: 
    import copykitten 
except ImportError: 
    print("[!] Copykitten not installed")

pyautogui.FAILSAFE = DO_NOT_TOUCH["FAILSAFE"]

def check_quit():
    if keyboard.is_pressed(DO_NOT_TOUCH["EMERGENCY_KEY"]):
        print(f"\n[i] '{DO_NOT_TOUCH['EMERGENCY_KEY']}' detected; program terminated.")
        exit()

def find_ui(img):
    check_quit()
    try: 
        return pyautogui.locateOnScreen(img, confidence=SETTINGS["CONFIDENCE"], grayscale=True)
    except: 
        return None

def extract_clicks(text):
    try:
        clean_list = re.search(r'\[\s*\[.*\]\s*\]', text, re.DOTALL)
        if clean_list:
            return ast.literal_eval(clean_list.group(0))
    except:
        pass
    return None

def smart_find_copy_button(bar_pos):
    target_x = bar_pos.left + (bar_pos.width // 2)
    target_y = bar_pos.top - 75
    pyautogui.moveTo(target_x, target_y)
    for i in range(DO_NOT_TOUCH["SCROLL_ATTEMPTS"]):
        check_quit()
        pyautogui.scroll(DO_NOT_TOUCH["SCROLL_AMOUNT"]) 
        btn = find_ui(ASSETS["COPY_BTN"])
        if btn:
            return btn
        time.sleep(DO_NOT_TOUCH["SCROLL_PAUSE"])
    return None

def ai_talk(bar, prompt, paste_image=False, copy_result=False):
    check_quit()
    pyautogui.click(bar)
    time.sleep(0.2)
    
    if paste_image:
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(DELAYS["PASTE"])
    
    pyperclip.copy(prompt)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pyautogui.press('enter')
    
    for attempt in range(DO_NOT_TOUCH["MAX_SEND_RETRIES"]):
        time.sleep(DO_NOT_TOUCH["VERIFY_SEND"])
        check_quit()
        
        pyperclip.copy("CHECKING_EMPTY") 
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(DO_NOT_TOUCH["CLIPBOARD_SYNC"]) 
        
        content = pyperclip.paste().strip()
        if content == "" or content == "CHECKING_EMPTY":
            break
        
        pyautogui.click(bar)
        pyautogui.press('enter')
    
    time.sleep(DELAYS["POST_SEND_PAUSE"])

    copy_btn = smart_find_copy_button(bar)
    if copy_btn and copy_result:
        pyautogui.click(copy_btn)
        time.sleep(0.5)
        return pyperclip.paste()
    
    return ""

def calibrate_region():
    print("--- CALIBRATION ---")
    print("[!] Hover to top-left and press SHIFT")
    while not keyboard.is_pressed('shift'):
        time.sleep(0.1)
    p1 = pyautogui.position()
    while keyboard.is_pressed('shift'): time.sleep(0.1)
    time.sleep(0.5)

    print("[!] Hover to bottom-right and press SHIFT")
    while not keyboard.is_pressed('shift'):
        time.sleep(0.1)
    p2 = pyautogui.position()
    while keyboard.is_pressed('shift'): time.sleep(0.1)

    SCREEN_REGION["LEFT"] = min(p1.x, p2.x)
    SCREEN_REGION["TOP"] = min(p1.y, p2.y)
    SCREEN_REGION["WIDTH"] = abs(p2.x - p1.x)
    SCREEN_REGION["HEIGHT"] = abs(p2.y - p1.y)
    print(f"[i] Screen Region: {SCREEN_REGION}")
    time.sleep(1)

def run_automation():
    print(f"--- AUTOMATION ACTIVE ---")
    print(f"[!] To stop, hold '{DO_NOT_TOUCH['EMERGENCY_KEY'].upper()}'")
    
    lx = SCREEN_REGION["LEFT"]
    ty = SCREEN_REGION["TOP"]
    w = SCREEN_REGION["WIDTH"]
    h = SCREEN_REGION["HEIGHT"]

    while True:
        check_quit()
        try:
            pyautogui.screenshot("current_task.png", region=(lx, ty, w, h))
            img = PIL.Image.open("current_task.png").convert("RGBA")
            copykitten.copy_image(img.tobytes(), img.width, img.height)

            pyautogui.hotkey('ctrl', 'pagedown')
            time.sleep(DELAYS["TAB_SWITCH"])
            
            bar = find_ui(ASSETS["INPUT_BAR"])
            if not bar: 
                pyautogui.hotkey('ctrl', 'pageup')
                time.sleep(1)
                continue

            ai_talk(bar, DO_NOT_TOUCH["PROMPTS"]["STEP_1_MAP"], paste_image=True, copy_result=False)
            response = ai_talk(bar, DO_NOT_TOUCH["PROMPTS"]["STEP_2_SOLVE"], paste_image=False, copy_result=True)
            clicks = extract_clicks(response)

            pyautogui.hotkey('ctrl', 'pageup')
            time.sleep(DO_NOT_TOUCH["VERIFY_SEND"])

            if clicks:
                for c in clicks:
                    check_quit()
                    rx = int((c[0] * w) / 1000) + lx
                    ry = int((c[1] * h) / 1000) + ty
                    pyautogui.click(rx, ry)
                    time.sleep(DELAYS["CLICK_SEQUENCE"])
            
            time.sleep(DELAYS["LOOP_COOLDOWN"])

        except Exception:
            time.sleep(DELAYS["LOOP_COOLDOWN"])

if __name__ == "__main__":
    calibrate_region()
    run_automation()
