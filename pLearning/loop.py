# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 14:52:32 2023

@author: SiamPC
"""

def use_loop(n):
    #range(initial value , limit , step/iteration)
    for i in range(1,n+1,1):
        if(i%2==0):
            print(i," is Even")
        else:
            print(i, "is Odd")
            
def use_whileLoop(n):
    i=1
    while(i<=n):
        if(i%2==0):
            print(i," is Even") 
        else:
            print(i,"  is Odd")
        i=i+1
        
def show_10():
    i=0
    while True:
        if (i>=3 and i<=6):
            i+=1
            continue
        if i==10:
            break
        print(i)
        i+=1
        
def main():
    x=15
    #use_loop(x)
    #use_whileLoop(x)
    show_10()
    
main()