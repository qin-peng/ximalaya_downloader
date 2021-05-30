# -*- coding:utf-8 -*-
import os
import json
import requests
from bs4 import BeautifulSoup
from m4a_generator import m4a_generator
from xm_sign_generator import xm_sign_generator
from token_generator import *


class ximalaya_downloader:
    def __init__(self):
        self.base_url = 'https://www.ximalaya.com'
        self.base_api = 'https://www.ximalaya.com/revision/play/album?albumId={}&pageNum={}&sort=0&pageSize=30'
        self.time_api = 'https://www.ximalaya.com/revision/time'

        # A web scraper by default sends requests without a user agent,
        # and that’s very suspicious for servers.
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'keep-alive',
            'Accept': '*/*',
            # 'Accept': 'text/html,application/xhtml+ xml,application/xml;q = 0.9,image/webp,image/apng,*/*;q=0.8, application/signe-exchange;v = b3',
            'Host': 'www.ximalaya.com'
        }
        self.session = requests.session()
        self.saving_path = os.getcwd()

    def set_saving_directory(self):
        print("The default save location is:\n    {}".format(os.getcwd()))
        print("Now please provide your custom save location:\n")
        while True:
            custom_path = input().strip()
            if custom_path[-1] != '/':
                custom_path = custom_path + '/'
            if os.path.exists(custom_path):
                self.saving_path = custom_path
                break
            else:
                try:
                    os.mkdir(custom_path)
                    self.saving_path = custom_path
                    break
                except Exception as e:
                    print('Please provide a valid save location.')
        print("Now files will be saved to:\n    {}".format(self.saving_path))
        return custom_path

    def get_album_url(self):
        print("Now please provide the url to be download:\n")
        album_url = input()
        if album_url[-1] != '/':
            album_url = album_url + '/'
        return album_url

    def get_context(self, audio_title, src_url, saving_directory):
        self.headers = self.get_headers()
        audio_response = self.session.get(src_url, headers=self.headers, stream=True)
        audio_path = saving_directory + audio_title + '.m4a'
        if not os.path.exists(audio_path):
            with open(audio_path, 'wb') as f:
                f.write(audio_response.content)
                print(audio_title + ' saved.')
        else:
            print(audio_title + '.m4a already exists.')

    def get_trackIDs_and_titles_and_srcs_from_album_url_non_vip(self, album_url, need_print=False, write_to_file=False):
        if album_url[-1] == '/':
            album_url = album_url[:-1]
        album_id = album_url[album_url.rfind('/') + 1:]
        base_url = "https://www.ximalaya.com/revision/album/v1/getTracksList?albumId={}&pageNum=1&pageSize=1000".format(album_id)
        audio_list_with_trackIDs_only = list()
        response = self.session.get(base_url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser').text
        i = 0
        while soup.find("trackId") != -1:
            i = i + 1
            pid = "{0:0>3}".format(i)
            tmp = soup[soup.find("trackId"):soup.find("playCount")]
            tmp_track_id = tmp[tmp.find("trackId") + 9: tmp.find("isPaid") - 2]
            tmp_title = tmp[tmp.find("title") + 8: -3]
            audio_list_with_trackIDs_only.append({'pid': pid, 'trackID': tmp_track_id, 'title': tmp_title})
            soup = soup[soup.find("anchorName") + 1:]

        if write_to_file:
            print("list_without_seeds.txt")
            print("List of trackIDs and titles, NO seeds or fileIDs from album url will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*audio_list_with_trackIDs_only, sep="\n", file=file)
            file.close()

        if need_print:
            for audio in audio_list_with_trackIDs_only:
                print(audio)
        return audio_list_with_trackIDs_only


    def get_trackIDs_and_titles_from_album_url_vip(self, album_url, need_print=False, write_to_file=False):
        if album_url[-1] != '/':
            album_url = album_url + '/'
        # print(soup.prettify())
        # 观察分集名称，搜索某一集名，了解html结构
        # if have next pages:
        # find total pages of the album:
        response = self.session.get(album_url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        # inspect the website HTML that you want to crawl
        # search '请输入页码'
        # print(soup.prettify())
        if soup.find('input', 'control-input WJ_') is not None:
            total_pages = int(soup.find('input', 'control-input WJ_').attrs['max'])
        else:
            total_pages = 1

        pages_list = [album_url]
        # Currently the pattern of ximalaya's next page urls is: album_url + 'p_i/'
        for i in range(2, total_pages + 1):
            tmp_url = album_url + 'p' + str(i) + '/'
            pages_list.append(tmp_url)

        # Get audio list of trackIDs and titles from album
        audio_list_with_trackIDs_only = list()
        audio_set_with_trackIDs_only = set()
        i = 0
        # base_url = 'https://www.ximalaya.com'
        for page in pages_list:
            response = self.session.get(page, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            # soup.find_all(name, attrs, recursive, string, limit, **kwargs)
            divs = soup.find_all('div', 'text lF_')
            for div in divs:
                title = div.a.get('title')  # get audio title
                if title not in audio_set_with_trackIDs_only:
                    i = i + 1
                    pid = i
                    # get trackID
                    trackID = div.a.get('href').split('/')[-1]
                    href = self.base_url + '/' + trackID
                    audio_set_with_trackIDs_only.add(title)
                    audio_list_with_trackIDs_only.append({'pid': pid, 'title': title, 'trackID': trackID, 'href': href})

        if write_to_file:
            print("list_without_seeds.txt")
            print("List of trackIDs and titles, NO seeds or fileIDs from album url will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*audio_list_with_trackIDs_only, sep="\n", file=file)
            file.close()

        if need_print:
            for audio in audio_list_with_trackIDs_only:
                print(audio)

        return audio_list_with_trackIDs_only

    def get_m4a_from_trackID_non_vip(self, audio_list_with_trackIDs_only, need_print=False, write_to_file=False):
        for audio in audio_list_with_trackIDs_only:
            self.headers = self.get_headers()
            url = "https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1".format(audio['trackID'])
            tmp = json.loads(self.get_content_from_url(url))
            audio['url'] = tmp['data']['src']

        if need_print:
            for audio in audio_list_with_trackIDs_only:
                print(audio)

        if write_to_file:
            print("non_vip_list_download.txt")
            print("List of m4a urls of non vip will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*audio_list_with_trackIDs_only, sep="\n", file=file)
            file.close()
        return audio_list_with_trackIDs_only


    def get_seeds_fileIds_from_trackID_list_vip(self, audio_list_with_trackIDs_only, need_print=False, write_to_file=False):
        for audio in audio_list_with_trackIDs_only:
            url = 'https://mpay.ximalaya.com/mobile/track/pay/{}/?device=pc'.format(audio['trackID'])
            tmp = json.loads(self.get_content_from_url(url))
            tmp.update(AT(tmp['ep']))
            audio.update(tmp)

        if need_print:
            for audio in audio_list_with_trackIDs_only:
                print(audio)

        if write_to_file:
            print("list_with_seeds.txt")
            print("List of trackIDs and titles, HAS seeds and fileIDs from album url will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*audio_list_with_trackIDs_only, sep="\n", file=file)
            file.close()

        return audio_list_with_trackIDs_only

    def get_m4a_urls_from_seed_and_fileID_list_vip(self, audio_list_with_seeds_and_fileIDs, need_print=False, write_to_file=False):
        m4a_list = []
        for i in audio_list_with_seeds_and_fileIDs:
            base = "http://audiopay.cos.tx.xmcdn.com"
            seed = i['seed']
            fileId = i['fileId']
            n = m4a_generator(seed)
            m4a_url = n.get_m4a(seed, fileId)
            if m4a_url.find("_preview") != -1:
                m4a_url = m4a_url[0: m4a_url.find("_preview")] + ".m4a"
            m4a_url = m4a_url + "?sign={}&&token={}&timestamp={}".format(i['sign'], i['token'], i['timestamp'])
            m4a_list.append(base + m4a_url)

        if need_print:
            for m4a in m4a_list:
                print(m4a)

        if write_to_file:
            print("list_m4a.txt")
            print("List of m4a urls will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*m4a_list, sep="\n", file=file)
            file.close()
        return m4a_list

    def get_download_list_vip(self, audio_list_without_seeds, m4a_list, need_print=False, write_to_file=False):
        if len(audio_list_without_seeds) != len(m4a_list):
            print("Lengths not equal")
        else:
            download_list = []
            for i in range(0, len(audio_list_without_seeds)):
                # Left Padding/right align
                tmp_title = "{0:0>3}_{1}".format(audio_list_without_seeds[i]['pid'], audio_list_without_seeds[i]['title'])
                tmp_url = m4a_list[i].strip()
                tmp_dict = {'title': tmp_title, 'url': tmp_url}
                download_list.append(tmp_dict)

        if need_print:
            for i in download_list:
                print(i)

        if write_to_file:
            print("list_download.txt")
            print("Download list will be saved to:\n    ")
            file_name = input().strip()
            file = open(file_name, 'w')
            print(*download_list, sep="\n", file=file)
            file.close()

        return download_list




    def get_content_from_url(self, url, need_print=False):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Connection': 'keep-alive',
            'Accept': '*/*'
        }
        session = requests.session()
        response = session.get(url, headers=headers, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        if need_print:
            print(soup.text)
        return soup.text

    def write_album_from_download_list_non_vip(self, download_list, saving_directory):
        for i in download_list:
            self.get_context(i['pid'] + '_' + i['title'], i['url'], saving_directory)
            print("Saved: {}".format(i['title']))

    def write_album_from_download_list_vip(self, download_list, saving_directory):
        for i in download_list:
            self.get_context(i['title'], i['url'], saving_directory)
            print("Saved: {}".format(i['title']))

    def get_headers(self):
        xm_sign = xm_sign_generator()
        self.headers = xm_sign.get_headers()
        return xm_sign.get_headers()

