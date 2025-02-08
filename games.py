import tkinter as tk
import random

def move(event):
    x1, _, x2, _,  = canvas.coords(basket)
    if event.keysym == "Left" and x1 > 0:
        canvas.move(basket, -20, 0)
    if event.keysym == "Right" and x2 < 500:
        canvas.move(basket, 20, 0)

def spawn_star():
    x = random.randint(20, 480)
    star = canvas.create_oval(x, 0, x+20, 20, fill="yellow")
    stars.append(star)
    root.after(1000, spawn_star)

def update_stars():
    global score, missed
    for star in stars[:]:
        canvas.move(star, 0, 5)
        x1, y1, x2, y2 = canvas.coords(star)
        bx1, by1, bx2, by2 = canvas.coords(basket)
        if y2 >= 500:
            stars.remove(star)
            canvas.delete(star)
            missed += 1
        elif bx1 < x2 and bx2 > x1 and by1 < y2 and by2 > y1:
            stars.remove(star)
            canvas.delete(star)
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")
    if missed < 3:
        root.after(50, update_stars)
    else:
        canvas.create_text(250, 250, text="Game Over", fill="red", font=("Arial", 24))
        canvas.create_text(250, 250, text="press enter buttton",fill="white")
        root.bind("<button>",restart_game)

def restart_game(event):
    global score, missed, stars
    canvas.delete("all")
    score, missed, stars = 0, 0, 
    canvas.create_rectangle(220, 450, 280, 470, fill="blue", tags="basket")
    canvas.create_text(50, 20, text=f"Score: {score}", fill="white", font=("Arial", 16), tags="score_text")
    spawn_star()
    update_stars()
    root.bind("<Left>", move)
    root.bind("<Right>", move)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500, bg="green")
canvas.pack()
basket = canvas.create_rectangle(220, 450, 280, 470, fill="red")
stars, score, missed = [],0, 0
score_text = canvas.create_text(50, 20, text=f"Score: {score}", fill="white", font=("Arial", 16))
root.bind("<Left>", move)
root.bind("<Right>", move)
spawn_star()
update_stars()
root.mainloop()
