# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:16:39 2019

@author: Paulo Franco
"""
def periodo(hora):
    if hora > 0 and hora < 6:
        return {'descrição':"madrugada",'id':1}
    elif hora >=6 and hora < 12:
        return {'descrição':"manhã",'id':2}
    elif hora >= 12 and hora < 18:
        return {'descrição':"tarde",'id':3}
    else:
        return {'descrição':"noite",'id':4}