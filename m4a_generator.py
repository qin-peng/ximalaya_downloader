# -*- coding:utf-8 -*-
import math

'''
Using seed, fileID to get .m4a urls
'''

'''
From JavaScript files,
search "seed", "randomSeed", "sign", "xm_sign", "cg_hun" etc
get the method to generate .m4a urls
    i = t.seed
    o = t.fileId
    a = t.ep
    s = t.duration
    u = t.domain
    l = t.apiVersion
    c = function(t, e) {
        var r = new xt(t).cg_fun(e);
        return "/" === r[0] ? r : "/".concat(r)
        }
'''

class m4a_generator:
    def __init__(self, _randomSeed):
        self._cgStr = ""
        self._randomSeed = _randomSeed

    def cg_decode(self, t):
        e = ""
        r = 0
        for r in range(0, len(t)):
            n = t[r]
            i = self._cgStr.find(n)
            if i != -1:
                e = e + str(i) + "*"
        return e

    def cg_fun(self, fileId):
        fileId_list = fileId.split("*")
        e = ""
        for r in range(0, len(fileId_list) - 1):
            tmp_int = int(fileId_list[r])
            if tmp_int < len(self._cgStr):
                e = e + self._cgStr[tmp_int]
        return e

    def cg_hun(self):
        self._cgStr = ""
        t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/\\:._-1234567890"
        e = len(t)
        for r in range(0, e):
            n = self.ran() * len(t)
            i = math.floor(n)
            if i < len(t):
                c = t[i]
                self._cgStr = self._cgStr + c
                # Convert the elements of an array into a string
                # remove c = t[i] in t
                tmp_list = t.split(c)
                t = "".join(str(elem) for elem in tmp_list)

    def ran(self):
        self._randomSeed = (211 * self._randomSeed + 30031) % 65536
        return self._randomSeed / 65536

    def get_m4a(self, seed, fileId):
        self._randomSeed = seed
        self.cg_hun()
        r = self.cg_fun(fileId)
        if r[0] == "/":
            return r
        else:
            r = "/" + r
            return r





