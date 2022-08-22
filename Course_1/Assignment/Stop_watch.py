# template for "Stopwatch: The Game"
import simplegui

# define global variables
total_ticks = 0
time_display = "0:00.0"
counter = 0
total_counter = 0
test = "/"
status = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    second_down = str(t % 10)
    second_top = (t % 600)//10
    if second_top >= 10:
        second_top = str(second_top)
    else:
        second_top = "0" + str(second_top)
    minute = str(t // 600)
    return minute +":"+ second_top + "."+ second_down
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global status
    status = True
    timer.start()

def stop():
    global status, total_ticks, counter, total_counter, test
    if status and total_ticks % 10 == 0:
        counter += 1
        total_counter +=1
        status = False
    else:
        total_counter += 1
        status = False
    test = str(counter) + "/" + str(total_counter)
    timer.stop()
    
def reset():
    global total_ticks, time_display, counter, total_counter, test, status
    status = True
    total_ticks = 0
    time_display = "0:00.0"
    counter = 0
    total_counter = 0
    test = str(counter) + "/" + str(total_counter)
    

# define event handler for timer with 0.1 sec interval
def tick():
    global total_ticks, time_display
    total_ticks += 1
    time_display = format(total_ticks)
    

        
# define draw handler
def draw(canvas):
    canvas.draw_text(str(time_display), (50, 110), 40, 'White')
    canvas.draw_text(str(test), (150,20), 20, "White")
    
    
# create frame
frame = simplegui.create_frame("Stop watch", 200, 200)

# register event handlers
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()

# Please remember to review the grading rubric