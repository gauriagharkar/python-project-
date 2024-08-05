import turtle
turtle .speed(0)
turtle.bgcolor('black')
color = ['yellow','red','pink',
        'cyan',' light green','blue']
for i in range (150):
    turtle. pencolor(color[i%6])
    turtle. circle(190-i/2,90)
    turtle.it(90)
    turtle.circle(190-i/3,90)
    turtle.it(60)
turtle.done()
