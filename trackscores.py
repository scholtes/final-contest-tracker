import sys
import requests
import re
from time import sleep

def teamify(name):
    teamdict = {
        "TEJAS" : 1,
        "GARRETT" : 1,
        "LAXMI" : 1,

        "JIL1LIIILLILIIIII0IO" : 2,
        "CIL1LIIILLILIIIII0IO" : 2,
        "AIL1LIIILLILIIIII0IO" : 2,

        "KORRAPATI" : 3,
        "THADIBSA" : 3,
        "PEDDIREDDY" : 3,

        "SYNERGY-1" : 4,
        "SYNERGY-2" : 4,
        "SYNERGY-3" : 4,

        "CDARK-1" : 5,
        "CDARK-2" : 5,
        "CDARK-3" : 5,

        "MARS2017-1" : 6,
        "MARS2017-2" : 6,
        "MARS2017-3" : 6,

        "GNARLY" : 7,
        "BARLY" : 7,
        "FARLY" : 7,

        "JASH-1" : 8,
        "JASH-2" : 8,
        "JASH-3" : 8,

        "HSK-1" : 9,
        "HSK-2" : 9,
        "HSK-3" : 9,

        "REED-1" : 10,
        "REED-2" : 10,
        "REED-3" : 10,

        "FAB5-1" : 11,
        "FAB5-2" : 11,
        "FAB5-3" : 11,

        "KALAN" : 12,
        "JAABHI" : 12,
        "AMIKA" : 12
    }
    return teamdict[name]

def getNextLog(idx):
    try:
        resp = requests.get("http://gauss.ececs.uc.edu/standings8150.html")
        raw = resp.content.decode()
        raw = raw.strip().split("\n")[22:]
        raw = raw[:36]
        raw = "\n".join(raw).strip()
        raw = re.sub(r'</?tr>', '', raw)
        raw = re.sub(r'</?td.*?>', ' ', raw)
        raw = re.sub(r' +', ' ', raw)
        raw = re.sub(r'^\s|\s$', '', raw)
        raw = [line.strip() for line in raw.split("\n")]
        raw = [re.compile('\s+').split(line) for line in raw]

        for line in raw:
            line[0] = str(teamify(line[0]))

        raw = [" ".join(line) for line in raw]
        raw = ";\n".join(raw)
        raw = "data" + str(idx) + " = [\n" + raw + "\n];"

        with open("logs\\datum" + str(idx) + ".m", 'w') as f:
            f.write(raw)

        return True
    except Exception as e:
        print(e)
        return False


def createMasterMatlab(count):
    code = "".join(["datum"+str(i)+";\n" for i in range(1, count+1)])
    code += "data = zeros(36, 8, " + str(count) + ");\n"
    for i in range(1, count+1):
        code += "data(:,:," + str(i) + ") = data" + str(i) + ";\n"
        code += "clear data"+str(i) + ";\n"
    with open("logs\\alldata.m", 'w') as f:
        f.write(code)


if __name__ == "__main__":
    count = int(sys.argv[1])
    sys.stdout.write('Starting ' + str(count) + "... ")
    while True:
        success = getNextLog(count)
        if success:
            print("X")
            count += 1
        else:
            print("!")
        createMasterMatlab(count-1)
        sys.stdout.write('Starting ' + str(count) + "... ")
        sys.stdout.flush()
        sleep(60)