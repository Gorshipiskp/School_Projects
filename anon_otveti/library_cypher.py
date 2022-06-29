import random

symvs_min = {
    "(0(0)0))": "!",
    "(0(02": ".",
    "(0(03": ",",
    "(0(04": ":",
    "(0(05": ";",
    "(0(06": "'",
    "(0(07": '"',
    "(0(08": '?',
    "(0(09": '<',
    "(0()0))0": '>',
    "(0()0)))0))": '/',
    "(0()0))2": '-',
    "(0()0))3": '+',
    "(0()0))4": '=',
    "(0()0))5": '*',
    "(0()0))6": '^',
    "(0()0))9": '&',
    "(0(20": '&',
    "(0(2)0))": '@',
    "(0(22": '#',
    "(0(23": '№',
    "(0(24": '%',
    "(0(25": '$',
    "(0(26": '[',
    "(0(27": ']',
    "(0(28": '{',
    "(0(29": '}',
    "(0(30": '»',
    "(0(3)0))": '«',
    "(0(32": '—',
    "(0(33": '…',
    "(0(34": '_',
    "(0(35": '\n',
    "(0)0))0": "а",
    "(0)0)))0))": "А",
    "(020": "б",
    "(02)0))": "Б",
    "(030": "в",
    "(03)0))": "В",
    "(040": "г",
    "(05)0))": "Г",
    "(060": "д",
    "(06)0))": "Д",
    "(070": "е",
    "(07)0))": "Е",
    "(090": "ё",
    "(09)0))": "Ё",
    "()0))00": "ж",
    "()0))0)0))": "Ж",
    "()0)))0))0": "з",
    "()0)))0)))0))": "З",
    "()0))20": "и",
    "()0))2)0))": "И",
    "()0))30": "й",
    "()0))3)0))": "Й",
    "()0))40": "к",
    "()0))4)0))": "К",
    "()0))50": "л",
    "()0))5)0))": "Л",
    "()0))60": "м",
    "()0))6)0))": "М",
    "()0))70": "н",
    "()0))7)0))": "Н",
    "()0))80": "о",
    "()0))8)0))": "О",
    "()0))90": "п",
    "()0))9)0))": "П",
    "(200": "р",
    "(20)0))": "Р",
    "(2)0))0": "с",
    "(2)0)))0))": "С",
    "(220": "т",
    "(22)0))": "Т",
    "(230": "у",
    "(23)0))": "У",
    "(240": "ф",
    "(24)0))": "Ф",
    "(250": "х",
    "(25)0))": "Х",
    "(260": "ц",
    "(26)0))": "Ц",
    "(270": "ч",
    "(27)0))": "Ч",
    "(280": "ш",
    "(28)0))": "Ш",
    "(290": "щ",
    "(29)0))": "Щ",
    "(300": "ъ",
    "(3)0))0": "ы",
    "(3)0)))0))": "Ы",
    "(320": "ь",
    "(33)0))": "э",
    "(330": "Э",
    "(340": "ю",
    "(34)0))": "Ю",
    "(350": "я",
    "(35)0))": "Я"
}


class cypher_minimum:

    def __init__(self):
        self.syms = symvs_min = {
    "(0(0)0))": "!",
    "(0(02": ".",
    "(0(03": ",",
    "(0(04": ":",
    "(0(05": ";",
    "(0(06": "'",
    "(0(07": '"',
    "(0(08": '?',
    "(0(09": '<',
    "(0()0))0": '>',
    "(0()0)))0))": '/',
    "(0()0))2": '-',
    "(0()0))3": '+',
    "(0()0))4": '=',
    "(0()0))5": '*',
    "(0()0))6": '^',
    "(0()0))9": '&',
    "(0(20": '&',
    "(0(2)0))": '@',
    "(0(22": '#',
    "(0(23": '№',
    "(0(24": '%',
    "(0(25": '$',
    "(0(26": '[',
    "(0(27": ']',
    "(0(28": '{',
    "(0(29": '}',
    "(0(30": '»',
    "(0(3)0))": '«',
    "(0(32": '—',
    "(0(33": '…',
    "(0(34": '_',
    "(0(35": '\n',
    "(0)0))0": "а",
    "(0)0)))0))": "А",
    "(020": "б",
    "(02)0))": "Б",
    "(030": "в",
    "(03)0))": "В",
    "(040": "г",
    "(05)0))": "Г",
    "(060": "д",
    "(06)0))": "Д",
    "(070": "е",
    "(07)0))": "Е",
    "(090": "ё",
    "(09)0))": "Ё",
    "()0))00": "ж",
    "()0))0)0))": "Ж",
    "()0)))0))0": "з",
    "()0)))0)))0))": "З",
    "()0))20": "и",
    "()0))2)0))": "И",
    "()0))30": "й",
    "()0))3)0))": "Й",
    "()0))40": "к",
    "()0))4)0))": "К",
    "()0))50": "л",
    "()0))5)0))": "Л",
    "()0))60": "м",
    "()0))6)0))": "М",
    "()0))70": "н",
    "()0))7)0))": "Н",
    "()0))80": "о",
    "()0))8)0))": "О",
    "()0))90": "п",
    "()0))9)0))": "П",
    "(200": "р",
    "(20)0))": "Р",
    "(2)0))0": "с",
    "(2)0)))0))": "С",
    "(220": "т",
    "(22)0))": "Т",
    "(230": "у",
    "(23)0))": "У",
    "(240": "ф",
    "(24)0))": "Ф",
    "(250": "х",
    "(25)0))": "Х",
    "(260": "ц",
    "(26)0))": "Ц",
    "(270": "ч",
    "(27)0))": "Ч",
    "(280": "ш",
    "(28)0))": "Ш",
    "(290": "щ",
    "(29)0))": "Щ",
    "(300": "ъ",
    "(3)0))0": "ы",
    "(3)0)))0))": "Ы",
    "(320": "ь",
    "(33)0))": "э",
    "(330": "Э",
    "(340": "ю",
    "(34)0))": "Ю",
    "(350": "я",
    "(35)0))": "Я"
}

    def incph(text: str, bll: bool):
        for i in symvs_min.keys():
            if not bll:
                if symvs_min.get(i) == "\n":
                    continue
            text = text.replace(symvs_min.get(i), i)
        return text

    def outcph(text: str):
        for i in symvs_min.keys():
            text = text.replace(i, symvs_min.get(i))
        return text

    def incphkrypto(text: str, bll: bool, krpt: bool):
        massletters, krypto = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'), ""
        for p in range(0, 15):
            krypto += massletters[random.randint(0, len(massletters) - 1)]
        dictp, kryptolist, smv, smv2 = {}, list(krypto)[::-1], list(symvs_min), list(symvs_min.values())[::-1]
        for u, i in enumerate(smv2):
            x, mass = 0, list(smv[u])[::-1]
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 2
            dictp.update({f"{smv[u]}{krypto}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs_min.get(i) == "\n"):
                continue
            text = text.replace(dictp.get(i), i)
        if krpt:
            return krypto, text
        return text

    def outcphkrypto(text: str, bll: bool, krpt):
        dictp, kryptolist, smv, smv2 = {}, list(krpt)[::-1], list(symvs_min), list(symvs_min.values())[::-1]
        for u, i in enumerate(smv2):
            mass, x = list(smv[u])[::-1], 0
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 2
            dictp.update({f"{smv[u]}{krpt}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs_min.get(i) == "\n"):
                continue
            text = text.replace(i, dictp.get(i))
        return text

symvs = {
    "fxx0bf0xiu001": "!",
    "fxx0bf0xiu002": ".",
    "fxx0bf0xiu003": ",",
    "fxx0bf0xiu004": ":",
    "fxx0bf0xiu005": ";",
    "fxx0bf0xiu006": "'",
    "fxx0bf0xiu007": '"',
    "fxx0bf0xiu008": '?',
    "fxx0bf0xiu009": '<',
    "fxx0bf0xiu010": '>',
    "fxx0bf0xiu011": '/',
    "fxx0bf0xiu012": '-',
    "fxx0bf0xiu013": '+',
    "fxx0bf0xiu014": '=',
    "fxx0bf0xiu015": '*',
    "fxx0bf0xiu016": '^',
    "fxx0bf0xiu017": ')',
    "fxx0bf0xiu018": ')',
    "fxx0bf0xiu019": '&',
    "fxx0bf0xiu020": '&',
    "fxx0bf0xiu021": '@',
    "fxx0bf0xiu022": '#',
    "fxx0bf0xiu023": '№',
    "fxx0bf0xiu024": '%',
    "fxx0bf0xiu025": '$',
    "fxx0bf0xiu026": '[',
    "fxx0bf0xiu027": ']',
    "fxx0bf0xiu028": '{',
    "fxx0bf0xiu029": '}',
    "fxx0bf0xiu030": '»',
    "fxx0bf0xiu031": '«',
    "fxx0bf0xiu032": '—',
    "fxx0bf0xiu033": '…',
    "fxx0bf0xiu034": '_',
    "fxx0bf0xiu035": '\n',
    "fxx0bf010": "а",
    "fxx0bf011": "А",
    "fxx0bf020": "б",
    "fxx0bf021": "Б",
    "fxx0bf030": "в",
    "fxx0bf031": "В",
    "fxx0bf040": "г",
    "fxx0bf051": "Г",
    "fxx0bf060": "д",
    "fxx0bf061": "Д",
    "fxx0bf070": "е",
    "fxx0bf071": "Е",
    "fxx0bf090": "ё",
    "fxx0bf091": "Ё",
    "fxx0bf100": "ж",
    "fxx0bf101": "Ж",
    "fxx0bf110": "з",
    "fxx0bf111": "З",
    "fxx0bf120": "и",
    "fxx0bf121": "И",
    "fxx0bf130": "й",
    "fxx0bf131": "Й",
    "fxx0bf140": "к",
    "fxx0bf141": "К",
    "fxx0bf150": "л",
    "fxx0bf151": "Л",
    "fxx0bf160": "м",
    "fxx0bf161": "М",
    "fxx0bf170": "н",
    "fxx0bf171": "Н",
    "fxx0bf180": "о",
    "fxx0bf181": "О",
    "fxx0bf190": "п",
    "fxx0bf191": "П",
    "fxx0bf200": "р",
    "fxx0bf201": "Р",
    "fxx0bf210": "с",
    "fxx0bf211": "С",
    "fxx0bf220": "т",
    "fxx0bf221": "Т",
    "fxx0bf230": "у",
    "fxx0bf231": "У",
    "fxx0bf240": "ф",
    "fxx0bf241": "Ф",
    "fxx0bf250": "х",
    "fxx0bf251": "Х",
    "fxx0bf260": "ц",
    "fxx0bf261": "Ц",
    "fxx0bf270": "ч",
    "fxx0bf271": "Ч",
    "fxx0bf280": "ш",
    "fxx0bf281": "Ш",
    "fxx0bf290": "щ",
    "fxx0bf291": "Щ",
    "fxx0bf300": "ъ",
    "fxx0bf310": "ы",
    "fxx0bf311": "Ы",
    "fxx0bf320": "ь",
    "fxx0bf331": "э",
    "fxx0bf330": "Э",
    "fxx0bf340": "ю",
    "fxx0bf341": "Ю",
    "fxx0bf350": "я",
    "fxx0bf351": "Я"
}


class cypher:

    def incph(text: str, bll: bool):
        for i in symvs.keys():
            if not bll:
                if symvs.get(i) == "\n":
                    continue
            text = text.replace(symvs.get(i), i)
        return text

    def outcph(text: str):
        for i in symvs.keys():
            text = text.replace(i, symvs.get(i))
        return text

    def incphkrypto(text: str, bll: bool, krpt: bool):
        massletters, krypto = list('nxA1x)9@#___s15&)[{]Р)'), ""
        for p in range(0, 15):
            krypto += massletters[random.randint(0, len(massletters) - 1)]
        dictp, kryptolist, smv, smv2 = {}, list(krypto)[::-1], list(symvs), list(symvs.values())[::-1]
        for u, i in enumerate(smv2):
            x, mass = 0, list(smv[u])[::-1]
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 1
            dictp.update({f"{smv[u]}{krypto}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs.get(i) == "\n"):
                continue
            text = text.replace(dictp.get(i), i)
        if krpt:
            return krypto, text
        return text

    def outcphkrypto(text: str, bll: bool, krpt):
        dictp, kryptolist, smv, smv2 = {}, list(krpt)[::-1], list(symvs), list(symvs.values())[::-1]
        for u, i in enumerate(smv2):
            mass, x = list(smv[u])[::-1], 0
            for p in range(0, len(mass)):
                mass.insert(p + x, kryptolist[p])
                x += 1
            dictp.update({f"{smv[u]}{krpt}": f"{smv2[u]}"})
        for i in dictp.keys():
            if not bll and (symvs.get(i) == "\n"):
                continue
            text = text.replace(i, dictp.get(i))
        return text
