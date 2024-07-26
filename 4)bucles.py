

# for n in range(7):
#     print(n + 1)
    
# for n in range(1,13):
#     print(n + 1)

# for i in range(3,100,3):
#     print(i)
    

# for i in reversed(range(1,10)):
#     print(reversed(i))
    
# print("despegue")



import turtle
import colorsys

# Configuración inicial de la pantalla y la tortuga
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)  # Desactivar la actualización automática para mayor velocidad

# Función para determinar el color de un punto basado en su convergencia en el conjunto de Mandelbrot
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Dibujar el conjunto de Mandelbrot
def draw_mandelbrot(xmin, xmax, ymin, ymax, img_width, img_height, max_iter):
    turtle.penup()
    for x in range(img_width):
        for y in range(img_height):
            # Convertir coordenadas de píxeles a coordenadas complejas
            a = xmin + (x / img_width) * (xmax - xmin)
            b = ymin + (y / img_height) * (ymax - ymin)
            c = complex(a, b)
            m = mandelbrot(c, max_iter)
            # Determinar el color basado en el número de iteraciones
            color = colorsys.hsv_to_rgb(m / max_iter, 1.0, 0.8 if m < max_iter else 0)
            turtle.goto(x - img_width // 2, y - img_height // 2)
            turtle.pendown()
            turtle.pencolor(color)
            turtle.dot()
            turtle.penup()
    turtle.update()

# Parámetros del conjunto de Mandelbrot
xmin, xmax = -2.5, 1.5
ymin, ymax = -2, 2
img_width, img_height = 800, 800
max_iter = 100

# Dibujar el conjunto de Mandelbrot
draw_mandelbrot(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)

# Finalizar y cerrar la ventana al hacer clic
turtle.done()
