import turtle


trtl = turtle.Turtle()

# Start coorinates.
top_left_corner_x: float = -200.0
top_left_corner_y: float = 200.0

# Distance between lines and columns.
distance_between_lines: int = 20

# Numbers of clolumns.
number_of_columns: int = 20
# Number of lines.
number_of_lines: int = 25


# Color of axis.
#trtl.color("green")

# Draw speed.
trtl.speed(10)


def draw_new(x_start: float, y_start: float, x_end: float, y_end: float):
    """
    Draw a line between tow points.

    Args:
        x_start (float): _description_
        y_start (float): _description_
        x_end (float): _description_
        y_end (float): _description_
    """
    trtl.penup()
    trtl.goto(x_start, y_start)
    trtl.pendown()
    trtl.goto(x_end, y_end)
    trtl.penup()

# Draw lines.
x_start = top_left_corner_x
y_start = top_left_corner_y
for i in range(number_of_lines + 1):
    draw_new(
        x_start=x_start,
        x_end=x_start + distance_between_lines * number_of_columns,
        y_start=y_start,
        y_end=y_start,
    )
    y_start -= distance_between_lines

# Drwa columns.
x_start = top_left_corner_x
y_start = top_left_corner_y
for i in range(number_of_columns + 1):
    draw_new(
        x_start=x_start,
        x_end=x_start,
        y_start=y_start,
        y_end=y_start - distance_between_lines * number_of_lines,
    )
    x_start += distance_between_lines

# hide the turtle
trtl.hideturtle()

# Wait of user close.
turtle.done()
