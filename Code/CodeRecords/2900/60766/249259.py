# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:53:53 2020

@author: Lenovo
"""

if __name__ == '__main__':
    app=[]
    try:
        while True:
            app.append(input())
    except EOFError:
        pass
    
    title=''
    for i in range(len(app)):
        app[i]=app[i].replace(' ', '#')
        title=title+app[i]
    ans=len(title)-title.count('#')
    print(ans, end='')