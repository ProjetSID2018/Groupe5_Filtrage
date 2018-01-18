"""============================================================================
-*- coding: utf-8 -*-
Created on Tue Jan 11 2018

@author: Maxime BRIENS

============================================================================"""
import requests

SERVER_URL = 'http://localhost:5005'

def post_filtering(json):
    url_POS = SERVER_URL+'/filtering'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, data=json)
    return response

def post_tfidf(json):
    url_POS = SERVER_URL+'/tfidf'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url_POS, headers=headers, data=json)
    return response
