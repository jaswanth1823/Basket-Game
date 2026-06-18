import tkinter as tk
import random
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
BASKET_WIDTH = 80
BASKET_HEIGHT = 20
OBJECT_SIZE = 20
SPEED = 10 
def move_left(event):
    x = canvas.coords(basket)[0]
    if x > 0:
        canvas.move(basket, -20, 0)
def move_right(event):
    x = canvas.coords(basket)[2]
    if x < WINDOW_WIDTH:
        canvas.move(basket, 20, 0)
def drop_object():
    global falling_object
    if falling_object is None:
        x = random.randint(0, WINDOW_WIDTH - OBJECT_SIZE)
        falling_object = canvas.create_oval(x, 0, x + OBJECT_SIZE, OBJECT_SIZE, fill="red")
    move_object()
def move_object():
    global falling_object, score
    if falling_object is not None:
        canvas.move(falling_object, 0, SPEED)
        x1, y1, x2, y2 = canvas.coords(falling_object)
        bx1, by1, bx2, by2 = canvas.coords(basket)
        if y2 >= by1 and x1 >= bx1 and x2 <= bx2:
            score += 1
            canvas.delete(falling_object)
            falling_object = None
            update_score()
        elif y2 >= WINDOW_HEIGHT:
            canvas.delete(falling_object)
            falling_object = None
        root.after(50, move_object)
    else:
        root.after(1000, drop_object)

def update_score():
    canvas.itemconfig(score_text, text=f"Score: {score}")
root = tk.Tk()
root.title("Catch the Falling Objects")

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
canvas.pack()
basket = canvas.create_rectangle(WINDOW_WIDTH//2 - BASKET_WIDTH//2,
                                 WINDOW_HEIGHT - BASKET_HEIGHT - 10,
                                 WINDOW_WIDTH//2 + BASKET_WIDTH//2,
                                 WINDOW_HEIGHT - 10,
                                 fill="brown")
score = 0
score_text = canvas.create_text(50, 20, text="Score: 0", font=("Arial", 14), fill="black")
falling_object = None
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
drop_object()
root.mainloop()