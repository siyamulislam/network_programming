# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 13:06:28 2023

@author: SiamPC
"""

def add(num1,num2):
  sum=num1+num2
  return sum

def sub(num1,num2):
  sum=num1+num2
  return sum

def main():
    num1 =100
    num2=50.65
    substraction=sub(num1,num2)
    
    print("Sum is: {} ".format(add(num1,num2)), end=' & ')
    print("Sub is: {} ".format(substraction))

main()

