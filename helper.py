# -*- coding:utf-8 -*-
import json
import requests
from bs4 import BeautifulSoup

def list_to_file(list_name, file_name):
    file = open(file_name, 'w')
    print(*list_name, sep="\n", file=file)
    file.close()

def file_to_list_of_json(file_name):
    list_of_json = []
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.replace("\"", "\\\"")
            line = line.replace("\'", "\"")
            line = line.replace(": True", ": \"True\"")
            line = line.replace(": False", ": \"False\"")
            list_of_json.append(json.loads(line))
    return list_of_json

def list_of_str_to_list_of_json(list_name):
    list_of_json = []
    for line in list_name:
        line = line.strip()
        line = line.replace("\"", "\\\"")
        line = line.replace("\'", "\"")
        line = line.replace(": True", ": \"True\"")
        line = line.replace(": False", ": \"False\"")
        list_of_json.append(json.loads(line))
    return list_of_json

def get_content_from_url(url, need_print=False):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Connection': 'keep-alive',
        'Accept': '*/*'
    }
    session = requests.session()
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    if need_print:
        print(soup.text)
    return soup.text