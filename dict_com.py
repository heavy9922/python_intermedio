from math import sqrt 
def run():
        my_dicts = {i: i**3 for i in range(1, 101) if 1 % 3 != 0 }

#        dict = {}
#        for i in range(1, 101):
#                if i % 3 != 0:
#                        dict[i] = i**3

#        print(my_dicts)

        dc = {i: sqrt(i) for i in range(1,1001)}
        print(dc)
if __name__ == '__main__':
        run()