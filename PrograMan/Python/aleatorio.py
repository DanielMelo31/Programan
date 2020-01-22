import random

def run():
    numberFound = False
    randomNumber = random.randint(0, 20)
    
    while not numberFound:
        number = int(input('Adivina el numero: '))

        if number == randomNumber:
            print('Felicidades!! Encontraste el numero')
            numberFound = True
        elif number > randomNumber:
            print('El numero es mas pequeño')
        else:
            print('El numero es mas grande')
if __name__ == '__main__':
    run()