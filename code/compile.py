#!usr/bin/env/python
# Compiles *.jolang to *.js files
import json


def buildLangFromJson(path):
    langDic = None
    with open(path) as file:
        langDic = json.loads(file.read())
    return langDic


def replaceKey(path, lang):
    string = None
    with open(path) as file:
        string = file.read()
        print(string)
        for symbol in lang:
            string.replace(symbol, lang[symbol])
    print(string)


def jolangToArray(path, lang):
    out = []
    with open(path) as file:
        for line in file.readlines():
            tLine = []
            for symbol in line.split(" "):
                isJolangKey = None
                for key in lang:
                    if symbol == key:
                        isJolangKey = lang[symbol]
                if isJolangKey == None:
                    tLine.append(symbol)
                else:
                    tLine.append(lang[symbol])
            out.append(tLine)
    return out


def compileTarget(path, arr):
    s = ""
    for line in arr:
        temp = ""
        for t in line:
            temp += t + " "
        s += temp + "\n"
    with open(path, "w") as file:
        file.write(s)


def main():

    lang = buildLangFromJson("jolang.json")
    #targ = jolangToArray("main.jolang", lang)

    #compileTarget("main.js", targ)
    # print(lang)

    replaceKey("main.jolang", lang)


# Test
main()
