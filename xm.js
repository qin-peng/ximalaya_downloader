var _t = St("xm", "Ä[ÜJ=Û3Áf÷N")


kt = [19, 1, 4, 7, 30, 14, 28, 8, 24, 17, 6, 35, 34, 16, 9, 10, 13, 22, 32, 29, 31, 21, 18, 3, 2, 23, 25, 27, 11, 20, 5, 15, 12, 0, 33, 26]

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

function Z(t, e) {
    return (/%$/.test(t) ? parseInt(t.substring(0, t.length - 1), 10) / 100 * e : parseInt(t, 10)) || 0
}

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


{
    key: "queryPayTrack",
    value: function(t) {
        var e = this;
        return new Promise((function(r, n) {
            var i, o = (i = j().IS_DEBUG ? "" : "".concat(j().PROTOCOL, "//mpay.").concat(j().IS_TEST ? "dev.test." : "", "ximalaya.com"),
            "".concat(i, "/mobile/track/pay/{soundId}/").concat(Date.now())).replace("{soundId}", t);
            I.get({
                url: o,
                data: {
                    device: "pc",
                    isBackend: !0,
                    _: Date.now()
                },
                withCredentials: !j().IS_DEBUG
            }).then((function(t) {
                if (t.ret)
                    n(t);
                else {
                    var i = t.seed
                      , o = t.fileId
                      , a = t.ep
                      , s = t.duration
                      , u = t.domain
                      , l = t.apiVersion
                      , c = function(t, e) {
                        var r = new xt(t).cg_fun(e);
                        return "/" === r[0] ? r : "/".concat(r)
                    }(i, o)
                      , f = At(a);
                    f.duration = s;
                    var d = function(t) {
                        var e = t;
                        return t.indexOf(".xmcdn.com") > -1 && !j().IS_TEST ? e = t.replace("http:", "https:") : e
                    }(u)
                      , h = "".concat(d, "/download/").concat(l).concat(c)
                      , p = "".concat(h, "?").concat(e.stringfy(f));
                    r(p)
                }
            }
            )).catch((function(t) {
                return n(t)
            }
            ))
        }
        ))
    }
}