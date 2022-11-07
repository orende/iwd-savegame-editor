import sys

from hex_utils import toLittleEndianHex, toBigEndianHex, hexStringToIntArray


def editGoldAmount(filePath: str):
    goldAmount = input("Enter desired gold amount: ")
    if goldAmount.isnumeric() and int(goldAmount) >= 0:
        goldAmount = int(goldAmount)
    else:
        print("Invalid gold amount entered, must be a positive integer")
        sys.exit(-1)
    goldAmountHexArr = hexStringToIntArray(toBigEndianHex(goldAmount))
    if len(goldAmountHexArr) < 4:  # right pad with zeroes
        while len(goldAmountHexArr) < 4:
            goldAmountHexArr += [0]
    # print(goldAmountHexArr)
    with open(filePath, 'r+b') as fd:
        fd.seek(24)
        fd.write(bytearray(goldAmountHexArr))


def readCurrentGoldAmount(filePath: str):
    with open(filePath, 'rb') as fd:
        fd.seek(24)  # gold amount starts at offset 24 and takes up 32b or 4B (probably)
        bytesList: list[int] = list(fd.read(4))
        hexList = []
        for decVal in bytesList:
            hexVal = str(hex(decVal)[2:]).zfill(2)  # convert dec val to hex, strip '0x' prefix, left pad with 0's
            # print(hexVal + ' ', end='')
            hexList += [hexVal]
        # print('')
        print('Gold amount found: ', int(toLittleEndianHex("".join(hexList)), 16))


def main():
    filePath = sys.argv[1]  # should be the absolute path of the BALDUR.gam savefile you want to edit
    readCurrentGoldAmount(filePath)
    editGoldAmount(filePath)


if __name__ == '__main__':
    main()
