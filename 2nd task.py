import sys
import math

def inp_ut(x):
    while True:
      try:
          text = '{} {} {} '.format("Введите число",x,'>>>')
          a = float(input(text))
          return a
      except ValueError:
          print("Please reinsert")


def calc_A(a,b,c,d):  
    all_inputs = (a, b, c, d)

    for j in all_inputs:
      
      if math.fabs(j)!=0:
        try:
          summ = (a + b) / (c + d)
          
        except ZeroDivisionError:
          print("Division by zero")
      else:
        summ = 'None'
        
        break

    return summ


calc_A(a = inp_ut('a'),b = inp_ut('b'),c = inp_ut('c'),d = inp_ut('d'))
# Так как программу написал с учетом исключения возможности ввода некоректного типа данных
import unittest

class ConverterTest(unittest.TestCase):
    def test_task1234(self):
        self.assertEqual(calc_A(1,2,3,4), (0.42857142857142855))
    def test_task0(self):
        self.assertEqual(calc_A(1,2,3,0), ("None"))
    


if __name__ == '__main__':
    unittest.main()
