def run():
        squares = [i**2 for i in range(1, 101) if i%3 != 0]

#        for i in range(1, 101):
#                if i % 3 !=  0:
#                        squares.append(i**2)
#        print(squares)

        multi = [i  for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and  i % 9 == 0]

        print(multi)

#       natural_number = [1,2,3,4,5,6,7,8,9]

#       for num in natural_number:
#              cua = num**2
#                print(cua)
                

if __name__ == '__main__':
        run()