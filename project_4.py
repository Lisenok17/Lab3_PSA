import os
def task_4():
    signatures = {"0xff 0xfe": "UTF-16LE",
                  "0xfe 0xff": "UTF-16BE",
                  "0xcf 0xf0": "Windows 1251",
                  "0x8f 0xe0": "CP866"}
    files = os.listdir('WindowsTxtFiles')
    types = []
    for n in range(len(files)):
        with open('WindowsTxtFiles/' + files[n], 'rb') as f:
            file = f.read()
            types.append(hex(file[0]) + ' ' + hex(file[1]))
            with open('WindowsTxtFiles/' + files[n], 'r',
                      encoding=signatures[types[n]]) as f:
                s = f.readline()
                print(signatures[types[n]] + ' - '+ s)