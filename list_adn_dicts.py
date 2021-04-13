def run():
        my_list= [1, 'hello', True, 4.5]
        my_dict = {"firtname": "yeferson", "lastname":"castiblanco"}

        super_list=[                
                {"firtname": "yeferson", "lastname":"castiblanco"},
                {"firtname": "mauricio", "lastname":"castiblanco"},
                {"firtname": "ana", "lastname":"castiblanco"},
                {"firtname": "paola", "lastname":"castiblanco"},
                {"firtname": "lucia", "lastname":"chaves"},
        ]

        super_dict = {
                "natural_number": [1,2,3,4,5,6,7,8,9],
                "integer_nums": [-1,-2,0,1,2],
                "float_nums":[1.5,2.5,3.5]
        }

        for key, value in super_dict.items():
                print(key, "-" ,value)

        for i in super_list:
                for key, v in i.items():
                        print(key, "-" ,v)
if __name__ == '__main__':
        run()