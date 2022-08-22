# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [0,0]
ball_pos = [0,0]
score1 = 0
score2 = 0
paddle1_vel = 0
paddle2_vel = 0


# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    # Ball in the middle of canvas
    ball_pos = [WIDTH//2, HEIGHT//2]
    
    # Assign random value to velocity
    ball_vel[0] = random.randrange(120, 240) / 60
    ball_vel[1] = - random.randrange(60, 180) / 60
    
    # if direction is left, direction is upper left
    if not direction:
        ball_vel[0]= - ball_vel[0]

   
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global ball_pos, ball_vel # these are lists
    
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    score1 = 0
    score2 = 0
    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(random.choice([LEFT,RIGHT]))
    
        
        
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
   
    # update paddle's vertical position, keep paddle on the screen
    if HEIGHT -HALF_PAD_HEIGHT >= paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if HEIGHT -HALF_PAD_HEIGHT >= paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
    
          
    # draw paddles
    canvas.draw_line((8, paddle1_pos-40), (8, paddle1_pos+40),PAD_WIDTH, 'white')
    canvas.draw_line((592, paddle2_pos-40), (592, paddle2_pos+40), PAD_WIDTH, 'white')
    
    # determine whether paddle and ball collide 
    # Paddle 1 left
    if ball_pos[0] - BALL_RADIUS <= 8:
        if paddle1_pos + 40 >= ball_pos[1] >= paddle1_pos -40:
            ball_vel[0] = - ball_vel[0]
            # Increase difficulties
            ball_vel[1] = 1.1 * ball_vel[1]
            ball_vel[0] = 1.1 * ball_vel[0]
        else:
            spawn_ball(RIGHT)
            score2 +=1
            
    # Paddle 2 right
    elif ball_pos[0] + BALL_RADIUS >= 592:
        if paddle2_pos + 40 >= ball_pos[1] >= paddle2_pos -40:
            ball_vel[0] = - ball_vel[0]
            # Increase difficulties
            ball_vel[1] = 1.1 * ball_vel[1]
            ball_vel[0] = 1.1 * ball_vel[0]
        else:
            spawn_ball(LEFT)
            score1 +=1
    
    # draw scores
    canvas.draw_text(str(score1), (150, 100), 36, 'White')
    canvas.draw_text(str(score2), (450, 100), 36, 'White')
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 5
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Restart', new_game)

# start frame
new_game()
frame.start()