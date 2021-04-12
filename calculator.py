import requests
import sys

def add(first_num,second_num):
    return first_num + second_num

def subtract(first_num,second_num):
    return first_num - second_num

def multiply(first_num,second_num):
    return first_num * second_num

def devide(first_num,second_num):
    return first_num / second_num

def Append_list(list):
    list=[1,2,3,4,5]
    list.append(10)
    return len(list)

def reverse_string(string):
    return string[::-1]

def url_status_code():
    url='https://www.google.com/'
    response=requests.get(url)
    return response.status_code

def string_uppercase(s):
    s = s.upper()
    return s


def remove_duplicate(string):
    unique = ''
    for i in string:
        if i not in unique:
            unique = unique + i
    return unique


def longest_prifiex():
    l = ['car', 'carbon', 'cardiode']
    result = ''
    l.sort()
    for i in range(len(l[0])):
        if l[0][i] == l[-1][i]:
            result = result + l[0][i]
    return result


def second_largest_elelemt(l):
    first = l[0]
    second = -sys.maxsize
    for i in range(len(l)):
        if l[i] > first:
            second = first
            first = l[i]
        elif l[i] > second:
            second = l[i]
    return second
