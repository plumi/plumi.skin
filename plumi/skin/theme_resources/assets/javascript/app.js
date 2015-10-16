// /* - register_function.js - */
// // http://demo.plumi.org/portal_javascripts/register_function.js?original=1
// var bugRiddenCrashPronePieceOfJunk = (navigator.userAgent.indexOf('MSIE 5') !== -1 && navigator.userAgent.indexOf('Mac') !== -1);
// var W3CDOM = (!bugRiddenCrashPronePieceOfJunk && typeof document.getElementsByTagName !== 'undefined' && typeof document.createElement !== 'undefined');
// var registerEventListener = function(elem, event, func) {
//     jQuery(elem).bind(event, func)
// };
// var unRegisterEventListener = function(elem, event, func) {
//     jQuery(elem).unbind(event, func)
// };
// var registerPloneFunction = jQuery;

// function getContentArea() {
//     var node = jQuery('#region-content,#content');
//     return node.length ? node[0] : null
// }


// /* - plone_javascript_variables.js - */
// // http://demo.plumi.org/portal_javascripts/plone_javascript_variables.js?original=1
// var portal_url = 'http://mgogoulos.plumi.org/';
var portal_url;
// var form_modified_message = 'Your form has not been saved. All changes you have made will be lost.';
// var form_resubmit_message = 'You already clicked the submit button. Do you really want to submit this form again?';
// var external_links_open_new_window = 'false';
// var mark_special_links = 'false';
// var ajax_noresponse_message = 'No response from server. Please try again later.';
// var close_box_message = 'Close this box.';

// /* - nodeutilities.js - */
// // http://demo.plumi.org/portal_javascripts/nodeutilities.js?original=1
// function wrapNode(node, wrappertype, wrapperclass) {
//     jQuery(node).wrap('<' + wrappertype + '>').parent().addClass(wrapperclass)
// }

// function nodeContained(innernode, outernode) {
//     return jQuery(innernode).parents().filter(function() {
//         return this === outernode
//     }).length > 0
// }

// function findContainer(node, func) {
//     var p = jQuery(node).parents().filter(func);
//     return p.length ? p.get(0) : false
// }

// function hasClassName(node, class_name) {
//     return jQuery(node).hasClass(class_name)
// }

// function addClassName(node, class_name) {
//     jQuery(node).addClass(class_name)
// }

// function removeClassName(node, class_name) {
//     jQuery(node).removeClass(class_name)
// }

// function replaceClassName(node, old_class, new_class, ignore_missing) {
//     if (ignore_missing || jQuery(node).hasClass(old_class)) {
//         jQuery(node).removeClass(old_class).addClass(new_class)
//     }
// }

// function walkTextNodes(node, func, data) {
//     jQuery(node).find('*').andSelf().contents().each(function() {
//         if (this.nodeType === 3) {
//             func(this, data)
//         }
//     })
// }

// function getInnerTextCompatible(node) {
//     return jQuery(node).text()
// }

// function getInnerTextFast(node) {
//     return jQuery(node).text()
// }

// function sortNodes(nodes, fetch_func, cmp_func) {
//     var SortNodeWrapper, items;
//     SortNodeWrapper = function(node) {
//         this.value = fetch_func(node);
//         this.cloned_node = node.cloneNode(true)
//     };
//     SortNodeWrapper.prototype.toString = function() {
//         return this.value.toString ? this.value.toString() : this.value
//     };
//     items = jQuery(nodes).map(function() {
//         return new SortNodeWrapper(this)
//     });
//     if (cmp_func) {
//         items.sort(cmp_func)
//     } else {
//         items.sort()
//     }
//     jQuery.each(items, function(i) {
//         jQuery(nodes[i]).replace(this.cloned_node)
//     })
// }

// function copyChildNodes(srcNode, dstNode) {
//     jQuery(srcNode).children().clone().appendTo(jQuery(dstNode))
// }


// /* - cookie_functions.js - */
// // http://demo.plumi.org/portal_javascripts/cookie_functions.js?original=1
// function createCookie(name, value, days) {
//     var date, expires;
//     if (days) {
//         date = new Date();
//         date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
//         expires = "; expires=" + date.toGMTString()
//     } else {
//         expires = ""
//     }
//     document.cookie = name + "=" + escape(value) + expires + "; path=/;"
// }

// function readCookie(name) {
//     var nameEQ = name + "=",
//         ca = document.cookie.split(';'),
//         i, c;
//     for (i = 0; i < ca.length; i = i + 1) {
//         c = ca[i];
//         while (c.charAt(0) === ' ') {
//             c = c.substring(1, c.length)
//         }
//         if (c.indexOf(nameEQ) === 0) {
//             return unescape(c.substring(nameEQ.length, c.length))
//         }
//     }
//     return null
// }

/*
 
 jQuery Tools v1.2.5 History "Back button for AJAX apps"

 NO COPYRIGHTS OR LICENSES. DO WHAT YOU LIKE.

 http://flowplayer.org/tools/toolbox/history.html

 Since: Mar 2010
 Date: 2010-12-27 15:01 
*/
(function(b) {
    function h(c) {
        if (c) {
            var a = d.contentWindow.document;
            a.open().close();
            a.location.hash = c
        }
    }
    var g, d, f, i;
    b.tools = b.tools || {
        version: "v1.2.5"
    };
    b.tools.history = {
        init: function(c) {
            if (!i) {
                if (b.browser.msie && b.browser.version < "8") {
                    if (!d) {
                        d = b("<iframe/>").attr("src", "javascript:false;").hide().get(0);
                        b("body").append(d);
                        setInterval(function() {
                            var a = d.contentWindow.document;
                            a = a.location.hash;
                            g !== a && b.event.trigger("hash", a)
                        }, 100);
                        h(location.hash || "#")
                    }
                } else setInterval(function() {
                    var a = location.hash;
                    a !== g && b.event.trigger("hash", a)
                }, 100);
                f = !f ? c : f.add(c);
                c.click(function(a) {
                    var e = b(this).attr("href");
                    d && h(e);
                    if (e.slice(0, 1) != "#") {
                        location.href = "#" + e;
                        return a.preventDefault()
                    }
                });
                i = true
            }
        }
    };
    b(window).bind("hash", function(c, a) {
        a ? f.filter(function() {
            var e = b(this).attr("href");
            return e == a || e == a.replace("#", "")
        }).trigger("history", [a]) : f.eq(0).trigger("history", [a]);
        g = a
    });
    b.fn.history = function(c) {
        b.tools.history.init(this);
        return this.bind("history", c)
    }
})(jQuery);


/* - modernizr.js - */
// http://demo.plumi.org/portal_javascripts/modernizr.js?original=1
;window.Modernizr = function(a, b, c) {
    function H() {
        e.input = function(a) {
            for (var b = 0, c = a.length; b < c; b++) t[a[b]] = a[b] in l;
            return t
        }("autocomplete autofocus list placeholder max min multiple pattern required step".split(" ")), e.inputtypes = function(a) {
            for (var d = 0, e, f, h, i = a.length; d < i; d++) l.setAttribute("type", f = a[d]), e = l.type !== "text", e && (l.value = m, l.style.cssText = "position:absolute;visibility:hidden;", /^range$/.test(f) && l.style.WebkitAppearance !== c ? (g.appendChild(l), h = b.defaultView, e = h.getComputedStyle && h.getComputedStyle(l, null).WebkitAppearance !== "textfield" && l.offsetHeight !== 0, g.removeChild(l)) : /^(search|tel)$/.test(f) || (/^(url|email)$/.test(f) ? e = l.checkValidity && l.checkValidity() === !1 : /^color$/.test(f) ? (g.appendChild(l), g.offsetWidth, e = l.value != m, g.removeChild(l)) : e = l.value != m)), s[a[d]] = !!e;
            return s
        }("search tel url email datetime date month week time datetime-local number range color".split(" "))
    }

    function F(a, b) {
        var c = a.charAt(0).toUpperCase() + a.substr(1),
            d = (a + " " + p.join(c + " ") + c).split(" ");
        return E(d, b)
    }

    function E(a, b) {
        for (var d in a)
            if (k[a[d]] !== c) return b == "pfx" ? a[d] : !0;
        return !1
    }

    function D(a, b) {

        return !!~("" + a).indexOf(b)
    }

    function C(a, b) {

        return typeof a === b
    }

    function B(a, b) {

        return A(o.join(a + ";") + (b || ""))
    }

    function A(a) {

        k.cssText = a
    }

    var d = "2.0.4",
        e = {},
        f = !0,
        g = b.documentElement,
        h = b.head || b.getElementsByTagName("head")[0],
        i = "modernizr",
        j = b.createElement(i),
        k = j.style,
        l = b.createElement("input"),
        m = ":)",
        n = Object.prototype.toString,
        o = " -webkit- -moz- -o- -ms- -khtml- ".split(" "),
        p = "Webkit Moz O ms Khtml".split(" "),
        q = {
            svg: "http://www.w3.org/2000/svg"
        },
        r = {},
        s = {},
        t = {},
        u = [],
        v = function(a, c, d, e) {
            var f, h, j, k = b.createElement("div");
            if (parseInt(d, 10))
                while (d--) j = b.createElement("div"), j.id = e ? e[d] : i + (d + 1), k.appendChild(j);
            f = ["&shy;", "<style>", a, "</style>"].join(""), k.id = i, k.innerHTML += f, g.appendChild(k), h = c(k, a), k.parentNode.removeChild(k);
            return !!h
        },
        w = function() {
            function d(d, e) {
                e = e || b.createElement(a[d] || "div"), d = "on" + d;
                var f = d in e;
                f || (e.setAttribute || (e = b.createElement("div")), e.setAttribute && e.removeAttribute && (e.setAttribute(d, ""), f = C(e[d], "function"), C(e[d], c) || (e[d] = c), e.removeAttribute(d))), e = null;
                return f
            }
            var a = {
                select: "input",
                change: "input",
                submit: "form",
                reset: "form",
                error: "img",
                load: "img",
                abort: "img"
            };
            return d
        }(),
        x, y = {}.hasOwnProperty,
        z;

    !C(y, c) && !C(y.call, c) ? z = function(a, b) {
        return y.call(a, b)
    } : z = function(a, b) {
        return b in a && C(a.constructor.prototype[b], c)
    };

    var G = function(c, d) {
        var f = c.join(""),
            g = d.length;
        v(f, function(c, d) {
            var f = b.styleSheets[b.styleSheets.length - 1],
                h = f.cssRules && f.cssRules[0] ? f.cssRules[0].cssText : f.cssText || "",
                i = c.childNodes,
                j = {};
            while (g--) j[i[g].id] = i[g];
            e.touch = "ontouchstart" in a || j.touch.offsetTop === 9, e.csstransforms3d = j.csstransforms3d.offsetLeft === 9, e.generatedcontent = j.generatedcontent.offsetHeight >= 1, e.fontface = /src/i.test(h) && h.indexOf(d.split(" ")[0]) === 0
        }, g, d)
    }(['@font-face {font-family:"font";src:url("https://")}', ["@media (", o.join("touch-enabled),("), i, ")", "{#touch{top:9px;position:absolute}}"].join(""), ["@media (", o.join("transform-3d),("), i, ")", "{#csstransforms3d{left:9px;position:absolute}}"].join(""), ['#generatedcontent:after{content:"', m, '"}'].join("")], ["fontface", "touch", "csstransforms3d", "generatedcontent"]);
    r.flexbox = function() {
        function c(a, b, c, d) {
            a.style.cssText = o.join(b + ":" + c + ";") + (d || "")
        }

        function a(a, b, c, d) {
            b += ":", a.style.cssText = (b + o.join(c + ";" + b)).slice(0, -b.length) + (d || "")
        }
        var d = b.createElement("div"),
            e = b.createElement("div");
        a(d, "display", "box", "width:42px;padding:0;"), c(e, "box-flex", "1", "width:10px;"), d.appendChild(e), g.appendChild(d);
        var f = e.offsetWidth === 42;
        d.removeChild(e), g.removeChild(d);
        return f
    }, r.canvas = function() {
        var a = b.createElement("canvas");
        return !!a.getContext && !!a.getContext("2d")
    }, r.canvastext = function() {
        return !!e.canvas && !!C(b.createElement("canvas").getContext("2d").fillText, "function")
    }, r.webgl = function() {
        return !!a.WebGLRenderingContext
    }, r.touch = function() {
        return e.touch
    }, r.geolocation = function() {
        return !!navigator.geolocation
    }, r.postmessage = function() {
        return !!a.postMessage
    }, r.websqldatabase = function() {
        var b = !!a.openDatabase;
        return b
    }, r.indexedDB = function() {
        for (var b = -1, c = p.length; ++b < c;)
            if (a[p[b].toLowerCase() + "IndexedDB"]) return !0;
        return !!a.indexedDB
    }, r.hashchange = function() {
        return w("hashchange", a) && (b.documentMode === c || b.documentMode > 7)
    }, r.history = function() {
        return !!a.history && !!history.pushState
    }, r.draganddrop = function() {
        return w("dragstart") && w("drop")
    }, r.websockets = function() {
        for (var b = -1, c = p.length; ++b < c;)
            if (a[p[b] + "WebSocket"]) return !0;
        return "WebSocket" in a
    }, r.rgba = function() {
        A("background-color:rgba(150,255,150,.5)");
        return D(k.backgroundColor, "rgba")
    }, r.hsla = function() {
        A("background-color:hsla(120,40%,100%,.5)");
        return D(k.backgroundColor, "rgba") || D(k.backgroundColor, "hsla")
    }, r.multiplebgs = function() {
        A("background:url(https://),url(https://),red url(https://)");
        return /(url\s*\(.*?){3}/.test(k.background)
    }, r.backgroundsize = function() {
        return F("backgroundSize")
    }, r.borderimage = function() {
        return F("borderImage")
    }, r.borderradius = function() {
        return F("borderRadius")
    }, r.boxshadow = function() {
        return F("boxShadow")
    }, r.textshadow = function() {
        return b.createElement("div").style.textShadow === ""
    }, r.opacity = function() {
        B("opacity:.55");
        return /^0.55$/.test(k.opacity)
    }, r.cssanimations = function() {
        return F("animationName")
    }, r.csscolumns = function() {
        return F("columnCount")
    }, r.cssgradients = function() {
        var a = "background-image:",
            b = "gradient(linear,left top,right bottom,from(#9f9),to(white));",
            c = "linear-gradient(left top,#9f9, white);";
        A((a + o.join(b + a) + o.join(c + a)).slice(0, -a.length));
        return D(k.backgroundImage, "gradient")
    }, r.cssreflections = function() {
        return F("boxReflect")
    }, r.csstransforms = function() {
        return !!E(["transformProperty", "WebkitTransform", "MozTransform", "OTransform", "msTransform"])
    }, r.csstransforms3d = function() {
        var a = !!E(["perspectiveProperty", "WebkitPerspective", "MozPerspective", "OPerspective", "msPerspective"]);
        a && "webkitPerspective" in g.style && (a = e.csstransforms3d);
        return a
    }, r.csstransitions = function() {
        return F("transitionProperty")
    }, r.fontface = function() {
        return e.fontface
    }, r.generatedcontent = function() {
        return e.generatedcontent
    }, r.video = function() {
        var a = b.createElement("video"),
            c = !1;
        try {
            if (c = !!a.canPlayType) {
                c = new Boolean(c), c.ogg = a.canPlayType('video/ogg; codecs="theora"');
                var d = 'video/mp4; codecs="avc1.42E01E';
                c.h264 = a.canPlayType(d + '"') || a.canPlayType(d + ', mp4a.40.2"'), c.webm = a.canPlayType('video/webm; codecs="vp8, vorbis"')
            }
        } catch (e) {}
        return c
    }, r.audio = function() {
        var a = b.createElement("audio"),
            c = !1;
        try {
            if (c = !!a.canPlayType) c = new Boolean(c), c.ogg = a.canPlayType('audio/ogg; codecs="vorbis"'), c.mp3 = a.canPlayType("audio/mpeg;"), c.wav = a.canPlayType('audio/wav; codecs="1"'), c.m4a = a.canPlayType("audio/x-m4a;") || a.canPlayType("audio/aac;")
        } catch (d) {}
        return c
    }, r.localstorage = function() {
        try {
            return !!localStorage.getItem
        } catch (a) {
            return !1
        }
    }, r.sessionstorage = function() {
        try {
            return !!sessionStorage.getItem
        } catch (a) {
            return !1
        }
    }, r.webworkers = function() {
        return !!a.Worker
    }, r.applicationcache = function() {
        return !!a.applicationCache
    }, r.svg = function() {
        return !!b.createElementNS && !!b.createElementNS(q.svg, "svg").createSVGRect
    }, r.inlinesvg = function() {
        var a = b.createElement("div");
        a.innerHTML = "<svg/>";
        return (a.firstChild && a.firstChild.namespaceURI) == q.svg
    }, r.smil = function() {
        return !!b.createElementNS && /SVG/.test(n.call(b.createElementNS(q.svg, "animate")))
    }, r.svgclippaths = function() {
        return !!b.createElementNS && /SVG/.test(n.call(b.createElementNS(q.svg, "clipPath")))
    };
    for (var I in r) z(r, I) && (x = I.toLowerCase(), e[x] = r[I](), u.push((e[x] ? "" : "no-") + x));
    e.input || H(), e.addTest = function(a, b) {
        if (typeof a == "object")
            for (var d in a) z(a, d) && e.addTest(d, a[d]);
        else {
            a = a.toLowerCase();
            if (e[a] !== c) return;
            b = typeof b == "boolean" ? b : !!b(), g.className += " " + (b ? "" : "no-") + a, e[a] = b
        }
        return e
    }, A(""), j = l = null, a.attachEvent && function() {
        var a = b.createElement("div");
        a.innerHTML = "<elem></elem>";
        return a.childNodes.length !== 1
    }() && function(a, b) {
        function s(a) {
            var b = -1;
            while (++b < g) a.createElement(f[b])
        }
        a.iepp = a.iepp || {};
        var d = a.iepp,
            e = d.html5elements || "abbr|article|aside|audio|canvas|datalist|details|figcaption|figure|footer|header|hgroup|mark|meter|nav|output|progress|section|summary|time|video",
            f = e.split("|"),
            g = f.length,
            h = new RegExp("(^|\\s)(" + e + ")", "gi"),
            i = new RegExp("<(/*)(" + e + ")", "gi"),
            j = /^\s*[\{\}]\s*$/,
            k = new RegExp("(^|[^\\n]*?\\s)(" + e + ")([^\\n]*)({[\\n\\w\\W]*?})", "gi"),
            l = b.createDocumentFragment(),
            m = b.documentElement,
            n = m.firstChild,
            o = b.createElement("body"),
            p = b.createElement("style"),
            q = /print|all/,
            r;
        d.getCSS = function(a, b) {
            if (a + "" === c) return "";
            var e = -1,
                f = a.length,
                g, h = [];
            while (++e < f) {
                g = a[e];
                if (g.disabled) continue;
                b = g.media || b, q.test(b) && h.push(d.getCSS(g.imports, b), g.cssText), b = "all"
            }
            return h.join("")
        }, d.parseCSS = function(a) {
            var b = [],
                c;
            while ((c = k.exec(a)) != null) b.push(((j.exec(c[1]) ? "\n" : c[1]) + c[2] + c[3]).replace(h, "$1.iepp_$2") + c[4]);
            return b.join("\n")
        }, d.writeHTML = function() {
            var a = -1;
            r = r || b.body;
            while (++a < g) {
                var c = b.getElementsByTagName(f[a]),
                    d = c.length,
                    e = -1;
                while (++e < d) c[e].className.indexOf("iepp_") < 0 && (c[e].className += " iepp_" + f[a])
            }
            l.appendChild(r), m.appendChild(o), o.className = r.className, o.id = r.id, o.innerHTML = r.innerHTML.replace(i, "<$1font")
        }, d._beforePrint = function() {
            p.styleSheet.cssText = d.parseCSS(d.getCSS(b.styleSheets, "all")), d.writeHTML()
        }, d.restoreHTML = function() {
            o.innerHTML = "", m.removeChild(o), m.appendChild(r)
        }, d._afterPrint = function() {
            d.restoreHTML(), p.styleSheet.cssText = ""
        }, s(b), s(l);
        d.disablePP || (n.insertBefore(p, n.firstChild), p.media = "print", p.className = "iepp-printshim", a.attachEvent("onbeforeprint", d._beforePrint), a.attachEvent("onafterprint", d._afterPrint))
    }(a, b), e._version = d, e._prefixes = o, e._domPrefixes = p, e.hasEvent = w, e.testProp = function(a) {
        return E([a])
    }, e.testAllProps = F, e.testStyles = v, g.className = g.className.replace(/\bno-js\b/, "") + (f ? " js " + u.join(" ") : "");
    return e
}(this, this.document),
function(a, b, c) {
    function k(a) {
        return !a || a == "loaded" || a == "complete"
    }

    function j() {
        var a = 1,
            b = -1;
        while (p.length - ++b)
            if (p[b].s && !(a = p[b].r)) break;
        a && g()
    }

    function i(a) {
        var c = b.createElement("script"),
            d;
        c.src = a.s, c.onreadystatechange = c.onload = function() {
            !d && k(c.readyState) && (d = 1, j(), c.onload = c.onreadystatechange = null)
        }, m(function() {
            d || (d = 1, j())
        }, H.errorTimeout), a.e ? c.onload() : n.parentNode.insertBefore(c, n)
    }

    function h(a) {
        var c = b.createElement("link"),
            d;
        c.href = a.s, c.rel = "stylesheet", c.type = "text/css", !a.e && (w || r) ? function a(b) {
            m(function() {
                if (!d) try {
                    b.sheet.cssRules.length ? (d = 1, j()) : a(b)
                } catch (c) {
                    c.code == 1e3 || c.message == "security" || c.message == "denied" ? (d = 1, m(function() {
                        j()
                    }, 0)) : a(b)
                }
            }, 0)
        }(c) : (c.onload = function() {
            d || (d = 1, m(function() {
                j()
            }, 0))
        }, a.e && c.onload()), m(function() {
            d || (d = 1, j())
        }, H.errorTimeout), !a.e && n.parentNode.insertBefore(c, n)
    }

    function g() {
        var a = p.shift();
        q = 1, a ? a.t ? m(function() {
            a.t == "c" ? h(a) : i(a)
        }, 0) : (a(), j()) : q = 0
    }

    function f(a, c, d, e, f, h) {
        function i() {
            !o && k(l.readyState) && (r.r = o = 1, !q && j(), l.onload = l.onreadystatechange = null, m(function() {
                u.removeChild(l)
            }, 0))
        }
        var l = b.createElement(a),
            o = 0,
            r = {
                t: d,
                s: c,
                e: h
            };
        l.src = l.data = c, !s && (l.style.display = "none"), l.width = l.height = "0", a != "object" && (l.type = d), l.onload = l.onreadystatechange = i, a == "img" ? l.onerror = i : a == "script" && (l.onerror = function() {
            r.e = r.r = 1, g()
        }), p.splice(e, 0, r), u.insertBefore(l, s ? null : n), m(function() {
            o || (u.removeChild(l), r.r = r.e = o = 1, j())
        }, H.errorTimeout)
    }

    function e(a, b, c) {
        var d = b == "c" ? z : y;
        q = 0, b = b || "j", C(a) ? f(d, a, b, this.i++, l, c) : (p.splice(this.i++, 0, a), p.length == 1 && g());
        return this
    }

    function d() {
        var a = H;
        a.loader = {
            load: e,
            i: 0
        };
        return a
    }
    var l = b.documentElement,
        m = a.setTimeout,
        n = b.getElementsByTagName("script")[0],
        o = {}.toString,
        p = [],
        q = 0,
        r = "MozAppearance" in l.style,
        s = r && !!b.createRange().compareNode,
        t = r && !s,
        u = s ? l : n.parentNode,
        v = a.opera && o.call(a.opera) == "[object Opera]",
        w = "webkitAppearance" in l.style,
        x = w && "async" in b.createElement("script"),
        y = r ? "object" : v || x ? "img" : "script",
        z = w ? "img" : y,
        A = Array.isArray || function(a) {
            return o.call(a) == "[object Array]"
        },
        B = function(a) {
            return typeof a == "object"
        },
        C = function(a) {
            return typeof a == "string"
        },
        D = function(a) {
            return o.call(a) == "[object Function]"
        },
        E = [],
        F = {},
        G, H;
    H = function(a) {
        function f(a) {
            var b = a.split("!"),
                c = E.length,
                d = b.pop(),
                e = b.length,
                f = {
                    url: d,
                    origUrl: d,
                    prefixes: b
                },
                g, h;
            for (h = 0; h < e; h++) g = F[b[h]], g && (f = g(f));
            for (h = 0; h < c; h++) f = E[h](f);
            return f
        }

        function e(a, b, e, g, h) {
            var i = f(a),
                j = i.autoCallback;
            if (!i.bypass) {
                b && (b = D(b) ? b : b[a] || b[g] || b[a.split("/").pop().split("?")[0]]);
                if (i.instead) return i.instead(a, b, e, g, h);
                e.load(i.url, i.forceCSS || !i.forceJS && /css$/.test(i.url) ? "c" : c, i.noexec), (D(b) || D(j)) && e.load(function() {
                    d(), b && b(i.origUrl, h, g), j && j(i.origUrl, h, g)
                })
            }
        }

        function b(a, b) {
            function c(a) {
                if (C(a)) e(a, h, b, 0, d);
                else if (B(a))
                    for (i in a) a.hasOwnProperty(i) && e(a[i], h, b, i, d)
            }
            var d = !!a.test,
                f = d ? a.yep : a.nope,
                g = a.load || a.both,
                h = a.callback,
                i;
            c(f), c(g), a.complete && b.load(a.complete)
        }
        var g, h, i = this.yepnope.loader;
        if (C(a)) e(a, 0, i, 0);
        else if (A(a))
            for (g = 0; g < a.length; g++) h = a[g], C(h) ? e(h, 0, i, 0) : A(h) ? H(h) : B(h) && b(h, i);
        else B(a) && b(a, i)
    }, H.addPrefix = function(a, b) {
        F[a] = b
    }, H.addFilter = function(a) {
        E.push(a)
    }, H.errorTimeout = 1e4, b.readyState == null && b.addEventListener && (b.readyState = "loading", b.addEventListener("DOMContentLoaded", G = function() {
        b.removeEventListener("DOMContentLoaded", G, 0), b.readyState = "complete"
    }, 0)), a.yepnope = d()
}(this, this.document), Modernizr.load = function() {
    yepnope.apply(window, [].slice.call(arguments, 0))
};

/* - livesearch.js - */
// http://demo.plumi.org/portal_javascripts/livesearch.js?original=1
// var livesearch = (function() {
//     var _2 = 400,
//         _7 = 400,
//         _0 = {},
//         _1 = "LSHighlight";

//     function _5(f, i) {
//         var l = null,
//             r = null,
//             c = {},
//             q = f.attr('action').replace(/@@search$/g, "") + "livesearch_reply",
//             re = f.find('div.LSResult'),
//             s = f.find('div.LSShadow'),
//             p = f.find('input[name="path"]');

//         function _12() {
//             re.hide();
//             l = null
//         }

//         function _6() {
//             window.setTimeout('livesearch.hide("' + f.attr('id') + '")', _7)
//         }

//         function _11(d) {
//             re.show();
//             s.html(d)
//         }

//         function _14() {
//             if (l === i.value) {
//                 return
//             }
//             l = i.value;
//             if (r && r.readyState < 4) {
//                 r.abort()
//             }
//             if (i.value.length < 2) {
//                 _12();
//                 return
//             }
//             var qu = {
//                 q: i.value
//             };
//             if (p.length && p[0].checked) {
//                 qu.path = p.val()
//             }
//             qu = jQuery.param(qu);
//             if (c[qu]) {
//                 _11(c[qu]);
//                 return
//             }
//             r = jQuery.get(q, qu, function(d) {
//                 _11(d);
//                 c[qu] = d
//             }, 'text')
//         }

//         function _4() {
//             window.setTimeout('livesearch.search("' + f.attr('id') + '")', _2)
//         }
//         return {
//             hide: _12,
//             hide_delayed: _6,
//             search: _14,
//             search_delayed: _4
//         }
//     }

//     function _3(f) {
//         var t = null,
//             re = f.find('div.LSResult'),
//             s = f.find('div.LSShadow');

//         function _16() {
//             var c = s.find('li.LSHighlight').removeClass(_1),
//                 p = c.prev('li');
//             if (!p.length) {
//                 p = s.find('li:last')
//             }
//             p.addClass(_1);
//             return false
//         }

//         function _9() {
//             var c = s.find('li.LSHighlight').removeClass(_1),
//                 n = c.next('li');
//             if (!n.length) {
//                 n = s.find('li:first')
//             }
//             n.addClass(_1);
//             return false
//         }

//         function _8() {
//             s.find('li.LSHighlight').removeClass(_1);
//             re.hide()
//         }

//         function _10(e) {
//             window.clearTimeout(t);
//             switch (e.keyCode) {
//                 case 38:
//                     return _16();
//                 case 40:
//                     return _9();
//                 case 27:
//                     return _8();
//                 case 37:
//                     break;
//                 case 39:
//                     break;
//                 default:
//                     t = window.setTimeout('livesearch.search("' + f.attr('id') + '")', _2)
//             }
//         }

//         function _13() {
//             var t = s.find('li.LSHighlight a').attr('href');
//             if (!t) {
//                 return
//             }
//             window.location = t;
//             return false
//         }
//         return {
//             handler: _10,
//             submit: _13
//         }
//     }

//     function _15(i) {
//         var i = 'livesearch' + i,
//             f = jQuery(this).parents('form:first'),
//             k = _3(f);
//         _0[i] = _5(f, this);
//         f.attr('id', i).submit(k.submit);
//         jQuery(this).attr('autocomplete', 'off').keydown(k.handler).focus(_0[i].search_delayed).blur(_0[i].hide_delayed)
//     }
//     jQuery(function() {
//         jQuery("#searchGadget,input.portlet-search-gadget").each(_15)
//     });
//     return {
//         search: function(id) {
//             _0[id].search()
//         },
//         hide: function(id) {
//             _0[id].hide()
//         }
//     }
// }());

/* - ++resource++search.js - */
// http://demo.plumi.org/portal_javascripts/++resource++search.js?original=1
jQuery(function(jQuery) {
    var query,
        pushState,
        popState,
        popped,
        initialURL,
        Search = {},
        $default_res_container = jQuery('#search-results'),
        // navigation_root_url = jQuery('meta[name=navigation_root_url]').attr('content') || window.navigation_root_url || window.portal_url;
        navigation_root_url = window.location.origin?window.location.origin+'/':window.location.protocol+'/'+window.location.host+'/';
        portal_url = navigation_root_url;

    jQuery.fn.pullSearchResults = function(query) {
        return this.each(function() {
            var $container = jQuery(this);
            $.get('@@updated_search', query,

                function(data) {

                    var retRes,
                        toDisplay,
                        resultsNum,
                        currentSortTxt,
                        sortLinks,
                        sortLinksList,
                        searchTerm;

                    $container.hide();

                    if (jQuery('#ajax-search-res').length === 0) {
                        jQuery('body').append('<div id="ajax-search-res" style="display:block;"></div>')
                    }

                    jQuery('#ajax-search-res').html(data);

                    toDisplay = '';
                    sortLinksList = '';
                    retRes = jQuery('#ajax-search-res dl.searchResults > div.search-results');
                    resultsNum = jQuery('#ajax-search-res #updated-search-results-number');
                    currentSortTxt = jQuery("#updated-sorting-options strong").text();
                    sortLinks = jQuery("#updated-sorting-options a");
                    searchTerm = jQuery("#ajax-search-res #updated-search-term").text();
                    
                    if(!searchTerm){
                        searchTerm = jQuery("#searchGadget").val();
                    }

                    retRes.each(function(i, el) {

                        var $el = jQuery(el),
                            resType,
                            resHeader = $el.find('dt'),
                            resImg = $el.find(".search-img img"),
                            resLink = resHeader.find("a"),
                            resLinkSrc = resLink.attr("href"),
                            resTitle = resLink.text(),
                            resDocAuthor = $el.find('.documentAuthor').html(),
                            resDescr = $el.find('dd > span').text(),
                            noThumbClass;

                        if (resHeader[0].className.indexOf('contenttype-plumivideo') > -1) {
                            resType = 'video';
                        } else if (resHeader[0].className.indexOf('contenttype-news-item') > -1) {
                            resType = 'news-item';
                            noThumbClass = 'newsitem';
                        } else if (resHeader[0].className.indexOf('contenttype-folder') > -1) {
                            resType = 'folder';
                            noThumbClass = 'folder';
                        } else if (resHeader[0].className.indexOf('contenttype-event') > -1) {
                            resType = 'event';
                            noThumbClass = 'event';
                        } else if (resHeader[0].className.indexOf('contenttype-image') > -1) {
                            resType = 'image';
                            noThumbClass = 'picture';
                        } else if (resHeader[0].className.indexOf('contenttype-document') > -1) {
                            resType = 'document';
                            noThumbClass = 'page';
                        } else if (resHeader[0].className.indexOf('contenttype-collection') > -1) {
                            resType = 'collection';
                            noThumbClass = 'collection';
                        } else if (resHeader[0].className.indexOf('contenttype-file') > -1) {
                            resType = 'file';
                            noThumbClass = 'file';
                        } else if (resHeader[0].className.indexOf('contenttype-link') > -1) {
                            resType = 'link';
                            noThumbClass = 'link';
                        } else if (resHeader[0].className.indexOf('contenttype-plumiexternalvideo') > -1) {
                            resType = 'external-video';
                            noThumbClass = 'external-video';
                        } else if (resHeader[0].className.indexOf('contenttype-video-folder') > -1) {
                            resType = 'video-folder';
                            noThumbClass = 'plumi-video-folder';
                        }

                        toDisplay += '<div class="video-thumb list gutter-bottom-half">';

                        if (resType === 'video') {
                            toDisplay += '\
                            <span class="video-thumb-img">\
                                <a href="' + resLinkSrc + '" title="">\
                                    <img src="' + resImg.attr('src') + '" alt="" />\
                                </a>\
                            </span>';
                        } else {
                            toDisplay += '\
                            <span class="video-thumb-img no-img-thumb">\
                                <a href="' + resLinkSrc + '" title="" class="' + noThumbClass + '"></a>\
                            </span>';
                        }

                        toDisplay += '\
                            <span class="video-thumb-title"><a href="' + resLinkSrc + '" title="">' + resTitle + '</a></span>\
                            <span class="video-thumb-meta">' + resDocAuthor + '</span>\
                            <span class="video-thumb-descr">' + resDescr + '</span>\
                            ';

                        toDisplay += '</div>';
                    });

                    sortLinks.each(function(i, el) {
                        sortLinksList += "<li>" + el.outerHTML + "</li>";
                    });

                    jQuery("#search-results-number").html(resultsNum.text());
                    jQuery(".results-sort .dropdown-toggle strong").html(currentSortTxt);
                    jQuery(".results-sort .dropdown-menu").html(sortLinksList);
                    jQuery("#SearchableText, #searchGadget").val(searchTerm);

                    jQuery('#rss-subscription a.link-feed').attr('href', function() {
                        var v = navigation_root_url + '/search_rss?' + query;
                        return v;
                    });

                    bindSearchSort();

                    // TODO: Update page title
                    /*if (jQuery('#search-term').length === 0) {
                        jQuery('h1.documentFirstHeading').append('<strong id="search-term" />')
                    }*/

                    $container.html(toDisplay).fadeIn('slow');

                    jQuery('#ajax-search-res').empty();
                }
            );
        });
    };

    pushState = function(query) {
        if (Modernizr.history) {
            var url = navigation_root_url + '/@@search?' + query;
            history.pushState(null, null, url)
        }
    };

    bindSearchSort = function() {
        jQuery('.results-sort .dropdown-menu li > a').on('click', function(e) {

            if (jQuery(this).attr('data-sort')) {
                jQuery("form.searchPage input[name='sort_on']").val($(this).attr('data-sort'))
            } else {
                jQuery("form.searchPage input[name='sort_on']").val('')
            }

            query = this.search.split('?')[1];

            $default_res_container.pullSearchResults(query);
            pushState(query);

            e.preventDefault();
        });
    };

    popped = ('state' in window.history);

    initialURL = location.href;

    jQuery(window).bind('popstate', function(event) {

        var initialPop, str;

        initialPop = !popped && location.href === initialURL;
        popped = true;
        
        if (initialPop) {
            return false;
        }
        
        if (!location.search) {
            return false;
        }
        
        query = location.search.split('?')[1];
        
        var results = query.match(/SearchableText=[^&]*/);
        
        if (results) {
            str = results[0];
            str = str.replace(/\+/g, ' '); // we remove '+' used between words
            jQuery("#SearchableText, #searchGadget").val(str.substr(15, str.length));
            $default_res_container.pullSearchResults(query)
        }
    });

    jQuery('form.searchPage').submit(function(e) {
        query = jQuery('form.searchPage').serialize();
        $default_res_container.pullSearchResults(query);
        pushState(query);
        e.preventDefault()
    });

    /* --------------- // TODO: not need ? --------------- */

    // $('#search-filter input.searchPage[type="submit"]').hide();

    // $('#search-field input.searchButton').click(function(e) {
    //     var st, queryString = location.search.substring(1),
    //         re = /([^&=]+)=([^&]*)/g,
    //         m, queryParameters = {};
    //     while (m = re.exec(queryString)) {
    //         queryParameters[decodeURIComponent(m[1])] = decodeURIComponent(m[2])
    //     }
    //     st = $('#search-field input[name="SearchableText"]').val();
    //     queryParameters['SearchableText'] = st;
    //     queryString = $.param(queryParameters);
    //     $default_res_container.pullSearchResults(queryString);
    //     pushState(queryString);
    //     e.preventDefault()
    // });

    /* --------------- // Search Bar --------------- */

    /*$('#search-field input[name="SearchableText"]').keyup(function() {
        $('input#searchGadget').val($(this).val())
    });*/

    /* --------------- Search Bar // --------------- */

    /*$('#search-results-bar dl.actionMenu > dd.actionMenuContent').click(function(e) {
        e.stopImmediatePropagation()
    });*/

    /* --------------- TODO: not need ? // --------------- */

    jQuery('.results-filter input').not('input#pt_toggle').on('change', function(e) {
        query = jQuery('form.searchPage').serialize();
        $default_res_container.pullSearchResults(query);
        pushState(query);
        e.preventDefault();
    });

    // TODO: Need for search results pagination
    /* 
    $('#search-results .listingBar a').on('click', function(e) {
        query = this.search.split('?')[1];
        $default_res_container.pullSearchResults(query);
        pushState(query);
        e.preventDefault()
    });
    */
   
    bindSearchSort();
});

/* - select_all.js - */
// http://demo.plumi.org/portal_javascripts/select_all.js?original=1
function toggleSelect(selectbutton, id, initialState, formName) {
    var fid, state, base, i, checks, check, len;

    fid = id || 'ids:list';
    state = selectbutton.isSelected;
    
    if (state === undefined) {
        state = Boolean(initialState)
    }
    
    selectbutton.isSelected = !state;
    
    jQuery(selectbutton).attr('src', portal_url + '/select_' + (state ? 'all' : 'none') + '_icon.png');
    
    // base = formName ? jQuery(document.forms[formName]) : jQuery(document);   // TODO: also 'formName' parameter not used
    base = jQuery('.results-filter');
    
    /*console.log( 'input[name="' + fid + '"]:checkbox' );
    console.log( state );*/

    // console.log( base );
    // console.log( base.find('input[name="' + fid + '"]:checkbox') );

    checks = base[0].querySelectorAll('input[name="' + fid + '"][type="checkbox"]');
    len = checks.length;

    for(i =0; i<len;i++){
        check = checks[i];
        if( i+1 < len ){
            check.checked = !state;
        }
        else{
            check.checked = state;
        }
    }

    checks[len-1].click();

    return false;
}

(function() {

    (function($) {

        'use strict';

        var $videoElem, $playerHighLink, $playerLowLink, $videoDLinksWrapper, $videoDLinksEl, videoExtension, videoPlayer, $videoShareWrapper, $shareBoxLi, $shareBoxTexts;

        /* General */

        jQuery('.dropdown-toggle').dropdown();

        jQuery('.show-more-text a').on("click", function(e) {
            e.preventDefault();
            var a = jQuery(this).parent().parent();

            if (a.hasClass("show-the-text")) {
                a.find('.more-text').slideUp(300, function() {
                    a.toggleClass("show-the-text");
                });
            } else {
                a.find('.more-text').slideDown(300, function() {
                    a.toggleClass("show-the-text");
                });
            }
        });

        /* Search results (pages) */

        jQuery('.results-filter .dropdown-menu').on('click', function(event) {
            var events = jQuery._data(document, 'events') || {};
            events = events.click || [];
            for (var i = 0; i < events.length; i++) {
                if (events[i].selector) {

                    //Check if the clicked element matches the event selector
                    if (jQuery(event.target).is(events[i].selector)) {
                        events[i].handler.call(event.target, event);
                    }

                    // Check if any of the clicked element parents matches the 
                    // delegated event selector (Emulating propagation)
                    jQuery(event.target).parents(events[i].selector).each(function() {
                        events[i].handler.call(this, event);
                    });
                }
            }
            event.stopPropagation(); //Always stop propagation
        });

        /* Latest videos load(ajax) */

        jQuery('.load-latest-videos').on('click', function() {

            jQuery('.load-latest-videos').addClass('loading');

            var b_start = 12,
                b_size = 12;

            $.ajax({
                url: 'latestvideos/JSON?b_size=' + b_size + '&b_start=' + b_start,
                type: 'GET',
                contentType: 'application/json',
                success: function(data) {
                    var i = 0;
                    b_start += b_size;
                    if (data.length < b_size) {
                        jQuery('.load-latest-videos').parent().parent().fadeOut('slow');
                    }
                    data.forEach(function(item) {
                        i += 1;
                        if (i > b_size) {
                            return;
                        }
                        var block = jQuery('.lv-wrapper .video-thumb:first').clone();

                        block.find('a.featured-video-image').attr('href', item.url);
                        block.find('a.featured-video-image img').attr('src', item.url + '/thumbnailImage_thumb');

                        block.find('a.featuredItemTitle').text(item.title);
                        block.find('a.featuredItemTitle').attr('href', item.url);
                        block.find('a.featuredItemTitle').attr('title', item.description.substr(0, 130));

                        block.find('.featuredItemDate').text(item.date);

                        if (item.countries) {
                            block.find('.featuredItemCountry').css('display', 'inline-block');
                            block.find('.featuredItemCountry').text(item.countries.title);
                            block.find('.featuredItemCountry').attr('href', item.countries.url);
                        } else {
                            block.find('.featuredItemCountry').css('display', 'none');
                        }

                        block.find('.video-thumb-descr a').attr('href', item.url);
                        block.find('.video-thumb-descr a').text(item.description.substr(0, 130) + '...');
                        block.find('.video-duration .discreet').text(item.duration);

                        block.insertAfter(jQuery('.lv-wrapper .video-thumb:last'));

                        jQuery('.load-latest-videos.loading').removeClass('loading');
                    });

                },
                error: function(jqXHR, textstate, errorThrown) {
                    jQuery('.load-latest-video.loading').removeClass('loading');
                    jQuery('.load-latest-video').parent().parent().fadeOut('slow');
                }
            });
            return false;
        });

        /* Video player */

        var $videoElem = jQuery("#main-video");

        if ($videoElem.length) {

            $playerHighLink = jQuery('#player-high');
            $playerLowLink = jQuery("#player-low");
            $videoDLinksWrapper = jQuery("#dl-links");
            $videoDLinksEl = $videoDLinksWrapper.find("li a");
            videoExtension = $videoElem[0].currentSrc.split('.')[$videoElem[0].currentSrc.split('.').length - 1];
            videoPlayer = new MediaElementPlayer("#main-video", {
                success: function(mediaElement, domObject) {}
            });
            $videoShareWrapper = jQuery("#share-box");
            $shareBoxLi = jQuery("div#share-box li.embed-links");
            $shareBoxTexts = jQuery("div#share-box textarea");

            $videoDLinksWrapper.addClass('default-display').addClass("hidden");
            $videoShareWrapper.addClass('default-display').addClass('hidden');

            jQuery($shareBoxLi[0]).find('a').addClass("active");
            jQuery($shareBoxTexts[0]).addClass("visible");

            jQuery('.videobar .hi-lo a').on('click', function(e) {

                var $this = jQuery(this),
                    newVideoSrc;

                $videoDLinksWrapper.addClass('hidden');
                $videoShareWrapper.addClass('hidden');
                jQuery('.videobar .download a').removeClass("active");
                jQuery('.videobar .share a').removeClass("active");

                videoPlayer.pause();

                if ($this.attr('id') === 'player-high') {
                    docCookies.setItem('videores', 'high');
                    $playerLowLink[0].style.display = '';
                    $playerHighLink[0].style.display = 'none';

                    if (videoExtension === 'webm') {
                        newVideoSrc = $videoDLinksEl[4].href;
                    } else {
                        newVideoSrc = $videoDLinksEl[2].href;
                    }
                } else if ($this.attr('id') === 'player-low') {
                    docCookies.setItem('videores', 'low');
                    $playerHighLink[0].style.display = '';
                    $playerLowLink[0].style.display = 'none';

                    if (videoExtension === 'webm') {
                        newVideoSrc = $videoDLinksEl[3].href;
                    } else {
                        newVideoSrc = $videoDLinksEl[1].href;
                    }
                }

                videoPlayer.setSrc(newVideoSrc);
                videoPlayer.play();

                return false;
            });

            jQuery('.videobar .download a').on('click', function(e) {

                var $this = jQuery(this);

                $videoShareWrapper.addClass('hidden');
                jQuery('.videobar .share a').removeClass("active");

                $videoDLinksWrapper.toggleClass('hidden');
                $this.toggleClass('active');

                return false;
            });

            jQuery('.videobar .share a').on('click', function(e) {

                var $this = jQuery(this);
                $videoDLinksWrapper.addClass('hidden');
                jQuery('.videobar .download a').removeClass("active");
                $videoShareWrapper.toggleClass('hidden');
                $this.toggleClass('active');

                return false;
            });

            $shareBoxLi.find('a').on('click', function() {

                return false;
            });

            $shareBoxLi.on("mouseenter", function(e, i) {

                var $this = jQuery(this),
                    linkEl = $this.find('a'),
                    t = linkEl.attr('id');

                t = t.replace("-link-", "-text-");

                $shareBoxLi.find('a').removeClass('active');
                linkEl.addClass('active');

                $shareBoxTexts.removeClass('visible');
                jQuery(".embed-box").find("textarea#" + t).addClass('visible');
            });

            jQuery(document).on('click', function(e) {
                var t = jQuery(e.target);

                if (t !== $videoShareWrapper && !$videoShareWrapper[0].contains(t[0])) {
                    jQuery('.videobar .share a').removeClass("active");
                    $videoShareWrapper.addClass('hidden');
                }

                if (t !== $videoDLinksWrapper && !$videoDLinksWrapper[0].contains(t[0])) {
                    jQuery('.videobar .download a').removeClass("active");
                    $videoDLinksWrapper.addClass('hidden');
                }
            });
        }

    }(jQuery));

})();

/*\
|*|
|*|  :: cookies.js ::
|*|
|*|  A complete cookies reader/writer framework with full unicode support.
|*|
|*|  Revision #1 - September 4, 2014
|*|
|*|  https://developer.mozilla.org/en-US/docs/Web/API/document.cookie
|*|  https://developer.mozilla.org/User:fusionchess
|*|
|*|  This framework is released under the GNU Public License, version 3 or later.
|*|  http://www.gnu.org/licenses/gpl-3.0-standalone.html
|*|
|*|  Syntaxes:
|*|
|*|  * docCookies.setItem(name, value[, end[, path[, domain[, secure]]]])
|*|  * docCookies.getItem(name)
|*|  * docCookies.removeItem(name[, path[, domain]])
|*|  * docCookies.hasItem(name)
|*|  * docCookies.keys()
|*|
\*/

var docCookies = {
    getItem: function(sKey) {
        if (!sKey) {
            return null;
        }
        return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
    },
    setItem: function(sKey, sValue, vEnd, sPath, sDomain, bSecure) {
        if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) {
            return false;
        }
        var sExpires = "";
        if (vEnd) {
            switch (vEnd.constructor) {
                case Number:
                    sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
                    break;
                case String:
                    sExpires = "; expires=" + vEnd;
                    break;
                case Date:
                    sExpires = "; expires=" + vEnd.toUTCString();
                    break;
            }
        }
        document.cookie = encodeURIComponent(sKey) + "=" + encodeURIComponent(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
        return true;
    },
    removeItem: function(sKey, sPath, sDomain) {
        if (!this.hasItem(sKey)) {
            return false;
        }
        document.cookie = encodeURIComponent(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT" + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "");
        return true;
    },
    hasItem: function(sKey) {
        if (!sKey) {
            return false;
        }
        return (new RegExp("(?:^|;\\s*)" + encodeURIComponent(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie);
    },
    keys: function() {
        var aKeys = document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g, "").split(/\s*(?:\=[^;]*)?;\s*/);
        for (var nLen = aKeys.length, nIdx = 0; nIdx < nLen; nIdx++) {
            aKeys[nIdx] = decodeURIComponent(aKeys[nIdx]);
        }
        return aKeys;
    }
};
