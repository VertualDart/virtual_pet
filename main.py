import random
import tkinter as tk
import pyautogui


#define variables
x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1,3,1)
impath = 'C:\\your\\path\\to\\file'

#create tkinter winodw
window = tk.Tk()


#call catto's action (.gif) to an array
idle = [tk.PhotoImage(file=impath + 'cat_idle.gif', format = 'gif - index %i' %(i)) for i in range(5)] #idle gid, 5 frames

idle_to_sleep = [tk.PhotoImage(file = impath + 'cat_idle_to_sleep.gif', format = 'gif - index %i' %(i)) for i in range(8)] #idle to sleep, 8 frames here

sleep = [tk.PhotoImage(file = impath + 'cat_sleeping.gif', format = 'gif - index %i' %(i)) for i in range(3)]

sleep_to_idle = [tk.PhotoImage(file = impath + 'cat_wake_up.gif', format = 'gif - index %i' %(i)) for i in range(8)]

walk_right = [tk.PhotoImage(file = impath + 'cat_walk_right.gif', format = 'gif - index %i' %(i)) for i in range(8)]

walk_left = [tk.PhotoImage(file = impath + 'cat_walk_left.gif', format = 'gif - index %i' %(i)) for i in range(8)]



#make bg transparent
window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributed('-transparentcolor','black')

#assign label
label = tk.Label(window, bd=0, bg='black')
label.pack()
window.mainloo()
