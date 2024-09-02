import calc
import unittest


def add_test():
    if calc.add(2, 5) == 7:
        print('func "add" is OK')
    else:
        print('func "add" is fail')


def sub_test():
    if calc.sub(8, 3) == 5:
        print('func "sub" is OK')
    else:
        print('func "sub" is fail')


def mul_test():
    if calc.mul(3, 3) == 9:
        print('func "mul" is OK')
    else:
        print('func "mul" is fail')


def div_test():
    if calc.div(9, 3) == 3:
        print('func "div" is OK')
    else:
        print('func "div" is fail')


# add_test()
# sub_test()
# mul_test()
# div_test()


class Calc_test(unittest.TestCase):

    def add_test(self):
        self.assertEqual(calc.add(2, 3), 5)


if __name__ == '__main__':
    unittest.main()



