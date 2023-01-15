# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 15:58:31 2023

@author: SiamPC
"""

def use_list():
    li= [10,15,4,12.2,7,25,90]
    
    #compressed code 
    even_list=[elem for elem in li if elem%2==0]
    odd_list= [elem for elem in li if elem%2!=0]
    
    print(even_list,odd_list)
    
    '''
    even_list=[]
    odd_list=[]
    
    for elem in li:
        if elem%2==0:
            even_list.append(elem)
        else:
            odd_list.append(elem)
            
    #for evenElem in even_list:
    print("even List: " ,even_list)
    print("odd List: " ,odd_list)          
    '''    
    
    '''
    for i in range(len(li)):
        print(li[i])
    '''
    '''
    for elem in li:
        print(elem)
    '''
    
    
def main():
    use_list()
    
main()