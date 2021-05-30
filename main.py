# -*- coding:utf-8 -*-
import os
import re
import time
import json
import requests
from bs4 import BeautifulSoup
from ximalaya_downloader import ximalaya_downloader
import time
import hashlib
import random
from xm_sign_generator import xm_sign_generator
from m4a_generator import m4a_generator

from helper import *
from token_generator import *

if __name__ == '__main__':
    ximalaya = ximalaya_downloader()

    # If vip album
    #album_url = 'https://www.ximalaya.com/youshengshu/12868137/' # 美国的故事第一季season 1
    #album_url = 'https://www.ximalaya.com/youshengshu/22688506/' # 美国的故事第二季seanson 2

    #audio_list_without_seeds = ximalaya.get_trackIDs_and_titles_from_album_url_vip(album_url, need_print=True, write_to_file=False)
    #audio_list_with_seeds = ximalaya.get_seeds_fileIds_from_trackID_list_vip(audio_list_without_seeds, need_print=True, write_to_file=False)
    #m4a_list = ximalaya.get_m4a_urls_from_seed_and_fileID_list_vip(audio_list_with_seeds, need_print=True, write_to_file=False)
    #download_list = ximalaya.get_download_list_vip(audio_list_without_seeds, m4a_list, need_print=True, write_to_file=False)

    #with open('list_download.txt') as file:
    #    lines = file.readlines()
    #download_list = list_of_str_to_list_of_json(lines)

    # custom_path = ximalaya.set_saving_directory()
    # custom_path = "/Users/husky/Desktop/spider/美国的故事第一季/"
    # custom_path = "/Users/husky/Desktop/spider/美国的故事第二季/"
    # custom_path = "/Users/husky/Desktop/spider/美国宪政历程/"
    #ximalaya.write_album_from_download_list_vip(download_list, custom_path)


    # If non vip album:
    #album_url = 'https://www.ximalaya.com/youshengshu/4591765/' # 美国宪政历程：影响美国的25个司法大案
    #album_url = 'https://www.ximalaya.com/renwen/2849826/'  # 费城风云——美国宪法的诞生与我们的反思
    #album_url = 'https://www.ximalaya.com/lishi/25080857/' # 《如果历史是一群喵》作者肥志
    album_url = 'https://www.ximalaya.com/ertong/19195913/' # 不一样的卡梅拉
    audio_list_without_seeds = ximalaya.get_trackIDs_and_titles_and_srcs_from_album_url_non_vip(album_url, need_print=True, write_to_file=False)
    download_list = ximalaya.get_m4a_from_trackID_non_vip(audio_list_without_seeds, need_print=True, write_to_file=False)

    '''
    with open('non_vip_list_download.txt') as file:
        lines = file.readlines()
    download_list = list_of_str_to_list_of_json(lines)
    for i in download_list:
        print(i)
    '''

    '''
    file = open('non_vip_list_download.txt', 'w')
    print(*download_list, sep="\n", file=file)
    file.close()
    '''
    #custom_path = ximalaya.set_saving_directory()
    #custom_path = "/Users/husky/Desktop/spider/美国宪政历程/"
    #custom_path = "/Users/husky/Desktop/spider/费城风云_美国宪法的诞生与我们的反思/"
    #custom_path = "/Users/husky/Desktop/spider/如果历史是一群喵/"
    #ximalaya.write_album_from_download_list_non_vip(download_list, custom_path)



    '''
    with open('list_without_seeds.txt') as file:
        lines = file.readlines()
    audio_list_without_seeds = list_of_str_to_list_of_json(lines)
    print('audio_list_without_seeds: ------------------------')
    for i in audio_list_without_seeds[0:3]:
        print(i)

    with open('list_with_seeds.txt') as file:
        lines = file.readlines()
    audio_list_with_seeds = list_of_str_to_list_of_json(lines)
    print('audio_list_with_seeds: ------------------------')
    for i in audio_list_with_seeds[0:3]:
        print(i)

    with open('list_m4a.txt') as file:
        m4a_list = file.readlines()
    print('m4a_list: ------------------------')
    for i in m4a_list[0:3]:
        print(i)
    '''

    #download_list = ximalaya.get_download_list_vip(audio_list_without_seeds, m4a_list, need_print=True, write_to_file=False)
    #with open('list_download.txt') as file:
    #    lines = file.readlines()
    #download_list = list_of_str_to_list_of_json(lines)


    custom_path = ximalaya.set_saving_directory()
    custom_path = "/Users/husky/Desktop/spider/不一样的卡梅拉/"
    ximalaya.write_album_from_download_list_vip(download_list, custom_path)