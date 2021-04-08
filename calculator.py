import requests

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
