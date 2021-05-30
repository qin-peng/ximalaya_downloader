import re

# token
'''
function St(t, e) {
    for (var r, n = [], i = 0, o = "", a = 0; 256 > a; a++)
        n[a] = a;
    for (a = 0; 256 > a; a++)
        i = (i + n[a] + t.charCodeAt(a % t.length)) % 256,
        r = n[a],
        n[a] = n[i],
        n[i] = r;
    for (var s = i = a = 0; s < e.length; s++)
        i = (i + n[a = (a + 1) % 256]) % 256,
        r = n[a],
        n[a] = n[i],
        n[i] = r,
        o += String.fromCharCode(e.charCodeAt(s) ^ n[(n[a] + n[i]) % 256]);
    return o
}
'''

def St(t, e):
    n = []
    i = 0
    o = ""
    for a in range(256):
        n.append(a)

    for a in range(256):
        i = (i + n[a] + ord(t[a % len(t)])) % 256
        r = n[a]
        n[a] = n[i]
        n[i] = r

    i = 0
    a = 0
    for s in range(len(e)):
        a = (a + 1) % 256
        i = (i + n[a]) % 256
        r = n[a]
        n[a] = n[i]
        n[i] = r
        o = o + chr((ord(e[s]) ^ n[(n[a] + n[i]) % 256]))
    return o

'''
function Z(t, e) {
    return (/%$/.test(t) ? parseInt(t.substring(0, t.length - 1), 10) / 100 * e : parseInt(t, 10)) || 0
}
'''

def str_to_int(s):
    if not s[0].isdigit():
        return 0
    else:
        tmp = ""
        for i in range(len(s)):
            if (s[i].isdigit()):
                tmp = tmp + s[i]
            else:
                break
        return int(tmp)

def Z(t, e):
    if re.search("[%$]", t):
        return str_to_int(t[:-1]) / 100 * e
    else:
        return str_to_int(t) or 0

'''
AT = function(t){
    var e = St(function(t, e){...}("d" + _t + "9", kt), function(t){...}(t)).split("-"),
    r = Z(e, 4)，
    n = r[0];
    return {
        sign: r[1],
        buy_key: n,
        token: r[2],
        timestamp: r[3]
    }
}
'''

'''
function(t, e) {
    for (var r = [], n = 0; n < t.length; n++) {
        for (var i = "a" <= t[n] && "z" >= t[n] ? t[n].charCodeAt() - 97 : t[n].charCodeAt() - "0".charCodeAt() + 26, o = 0; 36 > o; o++)
            if (e[o] == i) {
                i = o;
                break
            }
        r[n] = 25 < i ? String.fromCharCode(i - 26 + "0".charCodeAt()) : String.fromCharCode(i + 97)
    }
    return r.join("")
}
'''

def fun1(t, e):
    r = ""
    for n in range(len(t)):
        if "a" <= t[n] <= "z":
            i = ord(t[n]) - 97
        else:
            i = ord(t[n]) - ord("0") + 26
        for o in range(36):
            if e[o] == i:
                i = o
                break
        if i > 25:
            r = r + chr(i - 26 + ord("0"))
        else:
            r = r + chr(i + 97)
    return r

'''
function(t) {
    if (!t)
        return "";
    var e, r, n, i, o, a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1];
    for (i = (t = t.toString()).length,
    n = 0,
    o = ""; n < i; ) {
        do {
            e = a[255 & t.charCodeAt(n++)]
        } while (n < i && -1 == e);if (-1 == e)
            break;
        do {
            r = a[255 & t.charCodeAt(n++)]
        } while (n < i && -1 == r);if (-1 == r)
            break;
        o += String.fromCharCode(e << 2 | (48 & r) >> 4);
        do {
            if (61 == (e = 255 & t.charCodeAt(n++)))
                return o;
            e = a[e]
        } while (n < i && -1 == e);if (-1 == e)
            break;
        o += String.fromCharCode((15 & r) << 4 | (60 & e) >> 2);
        do {
            if (61 == (r = 255 & t.charCodeAt(n++)))
                return o;
            r = a[r]
        } while (n < i && -1 == r);if (-1 == r)
            break;
        o += String.fromCharCode((3 & e) << 6 | r)
    }
    return o
}
'''

def fun2(t):
    if not t:
        return ""
    a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
         -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
         18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
         39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1]
    t = str(t)
    i = len(t)
    o = ""
    n = 0

    while n < i:
        while True:
            e = a[255 & ord(t[n])]
            n = n + 1
            if not (n < i and -1 == e):
                break
        if -1 == e:
            break
        if n < i:
            while True:
                r = a[255 & ord(t[n])]
                n = n + 1
                if not (n < i and -1 == r):
                    break
        else:
            r = a[0]
        if -1 == r:
            break
        o = o + chr(e << 2 | (48 & r) >> 4)

        if n < i:
            while True:
                e = 255 & ord(t[n])
                n = n + 1
                if 61 == e:
                    return o
                e = a[e]
                if not (n < i and -1 == e):
                    break
        else:
            e = a[0]
        if -1 == e:
            break
        o = o + chr((15 & r) << 4 | (60 & e) >> 2)

        if n < i:
            while True:
                r = 255 & ord(t[n])
                n = n + 1
                if 61 == r:
                    return o
                r = a[r]
                if not (n < i and -1 == r):
                    break
        else:
            r = a[0]
        if -1 == r:
            break

        o = o + chr((3 & e) << 6 | r)
    return o

'''
AT = function(t){
    var e = St(function(t, e){...}("d" + _t + "9", kt), function(t){...}(t)).split("-"),
    r = Z(e, 4)，
    n = r[0];
    return {
        sign: r[1],
        buy_key: n,
        token: r[2],
        timestamp: r[3]
    }
}
'''
def AT(t):
    t_ = St("xm", "Ä[ÜJ=Û3Áf÷N")
    kt = [19, 1, 4, 7, 30, 14, 28, 8, 24, 17, 6, 35, 34, 16, 9, 10, 13, 22, 32, 29, 31, 21, 18, 3, 2, 23, 25, 27, 11,
          20, 5, 15, 12, 0, 33, 26]
    arg1 = fun1("d" + t_ + "9", kt)
    arg2 = fun2(t)
    e = St(arg1, arg2).split("-")
    res = {'sign':e[1], 'buy_key': Z(e[0], 4), 'token': e[2], 'timestamp': e[3]}
    return res

