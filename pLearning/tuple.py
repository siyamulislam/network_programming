# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 16:23:25 2023

@author: SiamPC
"""

def use_tuple():
    tp= (10,15,4,12.2,7,25,90,'siam')
    
    #compressed code 
    #even_list=[elem for elem in tp if elem%2==0]
    #odd_list= [elem for elem in tp if elem%2!=0]
    
    #print(even_list,odd_list)
    a,b,c,d,e,f,g,h=tp
    print('a->',a)
    print('d->',d)
    print('h->',h)
    print(tp)
    '''
    for elem in tp:
        print(elem)
    ''' 
    
  
    
    
    
def main():
    use_tuple()
    
main()