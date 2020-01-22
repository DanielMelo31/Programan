import turtle 

def main():
    jk = turtle.Screen()
    Rafael = turtle.Turtle()
    
    make_square(Rafael)
    turtle.mainloop()

def make_square(Rafael):
    length = int(input('Tamaño del cuadrado:')) 

    for i in range(4):
        makeLineAndTurn(Rafael, length)

def makeLineAndTurn(Rafael, length):
    Rafael.forward(length)
    Rafael.left(90)

if __name__ == '__main__':
    main