
YELLOW = color(255, 255, 0)
ORANGE = color(255, 102, 0)
RED = color(200, 0, 0)
DARK_BROWN = color(40, 20, 10)
CENTER_RED = color(255, 128, 128)

YELLOW1 = color(255, 204, 0)
YELLOW2 = color(255, 255, 128)
YELLOW3 = color(255, 255, 153)

WHITE = color(255, 255, 255)
DARK_RED = color(153, 0, 51)
PINK = color(255, 0, 102)
VIOLET = color(153, 0, 153)
LIGHT_VIOLET = color(255, 0, 255)
LIGHT_ORANGE = color(255, 136, 77)
GREEN = color(0, 102, 34)

ellipse1 = ellipse(w=110, h=100, fill=YELLOW)| translate(x=160)
ellipse2 = ellipse(w=95, h=86, fill=ORANGE)| translate(x=155)
ellipse3 = ellipse(w=80, h=72, fill=WHITE)| translate(x=150)
petal_unit = (
    ellipse1 +
    ellipse2 +
    ellipse3
)

diamond_unit = (
    rectangle(w=60, h=60, fill=ORANGE) +
    rectangle(w=45, h=45, fill=YELLOW) +
    rectangle(w=30, h=30, fill=WHITE)
) | rotate(45)

petal_ring = petal_unit | repeat(36, rotate(10))

star = diamond_unit | translate(x=35) | repeat(8, rotate(45))| scale(0.9)

fringe_unit = rectangle(w=18, h=22, fill=GREEN)
fringe = fringe_unit | translate(x=181) | repeat(36, rotate(10))

shapeP1 = rectangle(w=250, h=250, fill=DARK_RED) | repeat(10, rotate(angle=10))
shapeP2 = rectangle(w=235, h=235, fill=RED) |rotate(angle=5) | repeat(10, rotate(angle=10))
shapeP3 = rectangle(w=220, h=220, fill=ORANGE) | rotate(angle=10)| repeat(10, rotate(angle=10))
shapeP4 = rectangle(w=205, h=205, fill=LIGHT_ORANGE) |rotate(angle=5) | repeat(10, rotate(angle=10))
shapeP5 = rectangle(w=190, h=190, fill=YELLOW1) |rotate(angle=10)| repeat(10, rotate(angle=10))
shapeP6 = rectangle(w=178, h=178, fill=YELLOW) |rotate(angle=5) | repeat(10, rotate(angle=10))
shapeP7 = rectangle(w=165, h=165, fill=YELLOW2) |rotate(angle=10) | repeat(10, rotate(angle=10))
shapeP8 = rectangle(w=152, h=152, fill=YELLOW3) |rotate(angle=5) | repeat(10, rotate(angle=10))
shapeP9 = rectangle(w=140, h=140, fill=WHITE) | rotate(angle=10)| repeat(10, rotate(angle=10))
shapeP10 = rectangle(w=128, h=128, fill=VIOLET) |rotate(angle=5) | repeat(10, rotate(angle=10))

shapePP = rectangle(w=60, h=5, fill=WHITE) | rotate(angle=10)| repeat(10, rotate(angle=30))

white_petal = circle(x=105, y=0, r=8, fill=WHITE)
white_ring = white_petal | repeat(72, rotate(5))

dopetal = circle(x=20, y=0, r=5, fill=RED)
doring = dopetal | repeat(12, rotate(30))

pookalam = (
    circle(r=195, fill=DARK_BROWN) +
    circle(r=190, fill=DARK_RED) +
    fringe +
    circle(r=175, fill=DARK_BROWN) +
    shapeP1 + 
    shapeP2 + 
    shapeP3 + 
    shapeP4 + 
    shapeP5 + 
    shapeP6 + 
    shapeP7 +
    shapeP8 +
    shapeP9 +
    shapeP10 +
    circle(r=80, fill=DARK_BROWN) +
    circle(r=70, fill=YELLOW2) +
    star +
    circle(r=36, fill=YELLOW) +
    shapePP +
    doring +
    circle(r=15, fill=CENTER_RED) 
) | scale(0.7)

show(pookalam)