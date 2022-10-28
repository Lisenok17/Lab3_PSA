import os
def task_3():
    signatures = {"0x89 0x50": ".png",
                 "0x25 0x50": ".pdf",
                 "0x4f 0x54": ".otf",
                 "0xff 0xd8": ".jpg",
                 "0x52 0x61": ".rar",
                 "0x37 0x7a": ".7z",
                 "0x50 0x4b": ".zip"}
    files = os.listdir('BinaryFiles')
    types = []
    for n in range(len(files)):
        with open('BinaryFiles/' + files[n], 'rb') as f:
            file = f.read()
            types.append(hex(file[0]) + ' ' + hex(file[1]))
    for n in range(len(types)):
        os.rename('BinaryFiles/' + files[n],
                  'BinaryFiles/' + files[n] + signatures[types[n]])