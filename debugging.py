def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric() and num < 0 , "debes ingresar un numero positivo"  
    print(divisors(int(num)))
    print("Terminó mi programa")

   # """  try:
   #     num = int(input('Ingresa un número: '))
   #     if num < 0:
   #         raise Exception("negative number i not valid")
   #     print(divisors(num))
   #     print("Terminó mi programa")
   # except  ValueError:
   #     print("Debes ingresar un numero")
   # except  Exception:
   #     print("the number can't negative") """


if __name__ == '__main__':
    run()
