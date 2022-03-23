import random


def guess():
    random_number = random.randint(1, 100)
    chosen_number = int(input('Elige un numero: '))

    while chosen_number != random_number:

        if chosen_number > random_number:
            print('Busca un número mas pequeño')
        elif chosen_number < random_number:
            print('Busca un número mas grande')

        chosen_number = int(input('Elige otro número: '))
    
    print('¡Felicidades! Has adivinado el número')



if __name__ == '__main__':
    guess()