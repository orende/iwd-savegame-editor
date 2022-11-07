def zeroPadHexStr(param: str):
    for size in [2, 4, 6, 8]:
        if len(param) < size:
            return param.zfill(size)
        elif len(param) == size:
            return param


def splitIntoPairsAndReverse(inputVal):
    return [inputVal[i] + inputVal[i + 1] for i in range(0, len(inputVal), 2)][::-1]


def fromLittleEndianHex(inputVal: str) -> int:
    return int(inputVal, 16)


def fromBigEndianHex(inputVal: str) -> int:
    # assumes input is big-endian hex string
    pairs = splitIntoPairsAndReverse(inputVal)
    return int(''.join(pairs), 16)


def toLittleEndianHex(inputVal: str | int) -> str:
    # assumes input is big-endian or integer
    if type(inputVal) == int:
        inputVal = hex(inputVal)[2:]  # remove 0x prefix
    inputVal = zeroPadHexStr(inputVal)
    pairs = splitIntoPairsAndReverse(inputVal)
    return ''.join(pairs)


def toBigEndianHex(inputVal: str | int) -> str:
    # assumes input is little-endian or integer
    if type(inputVal) == int:
        inputVal = hex(inputVal)[2:]  # remove 0x prefix
    inputVal = zeroPadHexStr(inputVal)
    pairs = splitIntoPairsAndReverse(inputVal)
    return ''.join(pairs)


def hexStringToIntArray(inputVal: str) -> list[int]:
    pairs = [int(inputVal[i]+inputVal[i+1], 16) for i in range(0, len(inputVal), 2)]
    return pairs
