def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():

    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise Exception("negative number i not valid")    
        print(divisors(num))
        print("Terminó mi programa")
    except  ValueError:
        print("Debes ingresar un numero")
    except  Exception:
        print("the number can't negative")
        



if __name__ == '__main__':
    run()
