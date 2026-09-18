import turtle as t, math as m, random as r, time

s = t.Screen()
s.setup(800, 800)
s.bgcolor("black")
s.title("Una sorpresa para Alee")
s.tracer(0)

p = t.Turtle()
p.hideturtle()

text_turtle = t.Turtle()
text_turtle.hideturtle()

def heart(a, scale):
    x = 16 * (m.sin(a)**3) * scale
    y = (13*m.cos(a) - 5*m.cos(2*a) - 2*m.cos(3*a) - m.cos(4*a)) * scale
    return x, y

def draw_glowing_heart():
    # Primer ciclo de partículas
    for i in range(5000):
        a = r.uniform(0, 2 * m.pi)
        sc = r.uniform(0.5, 15.5)
        x, y = heart(a, sc)
        
        ang = m.atan2(y, x) + r.uniform(-0.5, 0.5)
        length = r.uniform(4, 14)
        
        p.pencolor(1.0, r.uniform(0.25, 0.55), r.uniform(0.65, 0.85))
        p.width(r.uniform(0.5, 1.2))
        p.penup(); p.goto(x, y)
        p.pendown(); p.goto(x + length * m.cos(ang), y + length * m.sin(ang))
        
        if i % 200 == 0: s.update()
    
    # Segundo ciclo de destellos exteriores
    for i in range(1500):
        a = r.uniform(0, 2 * m.pi)
        x, y = heart(a, 16.0)
        
        ang = m.atan2(y, x) + r.uniform(-0.35, 0.35)
        length = r.uniform(10, 32)
        
        p.pencolor(1.0, r.uniform(0.45, 0.75), r.uniform(0.75, 0.95))
        p.width(r.uniform(0.4, 0.9))
        p.penup(); p.goto(x + r.uniform(-2, 2), y + r.uniform(-2, 2))
        p.pendown(); p.goto(x + length * m.cos(ang), y + length * m.sin(ang))
        
        if i % 150 == 0: s.update()
    s.update()

def draw_rose():
    p.clear()
    text_turtle.clear()
    
    # Dibujar tallo
    p.penup()
    p.goto(0, -300)
    p.setheading(90)
    p.color("forest green")
    p.width(6)
    p.pendown()
    
    s.tracer(1)
    p.speed(4)
    for _ in range(30):
        p.forward(5)
        p.left(m.sin(_) * 0.1)
        
    p.goto(0, -50)
    
    # Dibujar pétalos de la rosa
    s.tracer(0)
    p.color("crimson")
    p.width(2)
    
    for i in range(180):
        p.circle(120 - i * 0.5, 90)
        p.left(90)
        p.circle(120 - i * 0.5, 90)
        p.left(100) 
        if i % 8 == 0:
            s.update()
            time.sleep(0.02)
            
    # Mensaje final
    text_turtle.penup()
    text_turtle.goto(0, -280)
    text_turtle.color("white")
    text_turtle.write("¡Te amo!", align="center", font=("Arial", 24, "bold"))
    s.update()

# 1. Dibujar el corazón inicial
draw_glowing_heart()

# 2. Mostrar la pregunta en el centro
text_turtle.penup()
text_turtle.goto(0, 0)
text_turtle.color("white")
text_turtle.write("¿Quieres ser mi novia, Ale?", align="center", font=("Arial", 28, "bold"))
s.update()

# 3. Lanzar la ventana de respuesta
time.sleep(1)
respuesta = s.textinput("Pregunta Importante", "Escribe 'si' o 'no':")

# 4. Evaluar respuesta y dibujar la rosa
if respuesta and respuesta.lower() in ["si", "sí", "s", "yes"]:
    draw_rose()
else:
    text_turtle.clear()
    p.clear()
    text_turtle.goto(0, 0)
    text_turtle.color("gray")
    text_turtle.write("Entiendo...", align="center", font=("Arial", 24, "italic"))
    s.update()

t.done()