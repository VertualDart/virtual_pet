import os
import pyautogui
import random
import tkinter as tk
from PIL import Image, ImageTk  # Added for better GIF handling

# --- Constants ---
screen_width, screen_height = pyautogui.size()
x = screen_width - 150  # Start near right edge
y = screen_height - 150  # Start near bottom
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randint(1, 3)
impath = os.path.join(os.getcwd(), "image")

# --- GIF Loader with PIL ---
def load_gif_frames(filename):
    frames = []
    try:
        with Image.open(filename) as img:
            try:
                while True:
                    frame = img.copy()
                    frames.append(ImageTk.PhotoImage(frame))
                    img.seek(img.tell() + 1)
            except EOFError:
                pass
    except Exception as e:
        print(f"Error loading {filename}: {str(e)}")
    return frames

# --- Event Logic ---
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        window.after(400, update, cycle, check, event_number, x)
    elif event_number == 5:
        check = 1
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in walk_left:
        check = 4
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in walk_right:
        check = 5
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in sleep_num:
        check = 2
        window.after(1000, update, cycle, check, event_number, x)
    elif event_number == 14:
        check = 3
        window.after(100, update, cycle, check, event_number, x)

# --- GIF Frame Cycling ---
def gif_work(cycle, frames, event_number, next_min, next_max):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randint(next_min, next_max)
    return cycle, event_number

# --- Boundary Check ---
def check_boundaries(x):
    # Keep pet within screen limits
    return max(50, min(x, screen_width - 150))

# --- Main Update Loop ---
def update(cycle, check, event_number, x):
    global label
    new_x = x
    
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        new_x -= 3
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        new_x += 3

    # Apply boundary check
    new_x = check_boundaries(new_x)
    
    window.geometry(f'100x100+{int(new_x)}+{int(y)}')
    label.configure(image=frame)
    window.after_id = window.after(150, event, cycle, check, event_number, new_x)

# --- Dragging Functions ---
def start_drag(event):
    window.x = event.x
    window.y = event.y

def drag_window(event):
    deltax = event.x - window.x
    deltay = event.y - window.y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry(f"+{x}+{y}")

# --- GUI Init ---
window = tk.Tk()
window.title("Desktop Pet")
window.overrideredirect(True)
window.wm_attributes('-topmost', True)  # Always on top
window.wm_attributes('-transparentcolor', 'black')
window.config(highlightbackground='black')
window.geometry(f'100x100+{int(x)}+{int(y)}')

# Add exit button
exit_btn = tk.Button(window, text="X", command=window.destroy, 
                    bg="red", fg="white", font=("Arial", 8), 
                    bd=0, padx=2, pady=0)
exit_btn.place(x=0, y=0, anchor="nw")

label = tk.Label(window, bd=0, bg='black')
label.pack()

# Bind dragging events
label.bind("<ButtonPress-1>", start_drag)
label.bind("<B1-Motion>", drag_window)

# --- Load GIFs ---
idle = load_gif_frames(os.path.join(impath, 'idle.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'idle.gif'))]
idle_to_sleep = load_gif_frames(os.path.join(impath, 'idle_to_sleep.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'idle_to_sleep.gif'))]
sleep = load_gif_frames(os.path.join(impath, 'sleep.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'sleep.gif'))]
sleep_to_idle = load_gif_frames(os.path.join(impath, 'sleep_to_idle.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'sleep_to_idle.gif'))]
walk_positive = load_gif_frames(os.path.join(impath, 'walking_positive.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'walking_positive.gif'))]
walk_negative = load_gif_frames(os.path.join(impath, 'walking_negative.gif')) or [tk.PhotoImage(file=os.path.join(impath, 'walking_negative.gif'))]

# --- Start Loop ---
window.after_id = window.after(1, update, cycle, check, event_number, x)
window.mainloop()