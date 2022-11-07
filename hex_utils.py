def zeroPadHexStr(param: str):
    lens = [2, 4, 6, 8]
    for l in lens:
        if len(param) < l:
            return param.zfill(l)
        elif len(param) == l:
            return param


def fromLittleEndianHex(inputVal: str) -> int:
    return int(inputVal, 16)


def fromBigEndianHex(inputVal: str) -> int:
    # assumes input is big-endian hex string
    pairs = []
    for i in range(0, len(inputVal) - 1, 2):
        pairs += [inputVal[i:i + 2]]
    return int(''.join(pairs[::-1]), 16)


def toLittleEndianHex(inputVal: str | int) -> str:
    # assumes input is big-endian or integer
    if type(inputVal) == int:
        inputVal = hex(inputVal)[2:]  # remove 0x prefix
    inputVal = zeroPadHexStr(inputVal)
    pairs = []
    for i in range(0, len(inputVal) - 1, 2):
        pairs += [inputVal[i:i + 2]]
    return ''.join(pairs[::-1])


def toBigEndianHex(inputVal: str | int) -> str:
    # assumes input is little-endian or integer
    if type(inputVal) == int:
        inputVal = hex(inputVal)[2:]  # remove 0x prefix
    inputVal = zeroPadHexStr(inputVal)
    pairs = []
    for i in range(0, len(inputVal) - 1, 2):
        pairs += [inputVal[i:i + 2]]
    return ''.join(pairs[::-1])


def hexStringToIntArray(inputVal: str) -> list[int]:
    pairs = []
    for i in range(0, len(inputVal) - 1, 2):
        pairs += [int(inputVal[i:i + 2], 16)]
    return pairs
