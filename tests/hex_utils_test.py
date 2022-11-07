import unittest

from hex_utils import fromLittleEndianHex, fromBigEndianHex, toLittleEndianHex, toBigEndianHex, hexStringToIntArray


class HexUtilsTestCase(unittest.TestCase):
    def test_fromLittleEndianHex_convertsHexStringToIntCorrectly(self):
        result = fromLittleEndianHex("057C")
        self.assertEqual(1404, result)

    def test_fromBigEndianHex_convertsHexStringToIntCorrectly(self):
        result = fromBigEndianHex("7C05")
        self.assertEqual(1404, result)

    def test_toLittleEndianHex_convertsHexStringToIntCorrectly(self):
        result = toLittleEndianHex("7C05")
        self.assertEqual("057C", result)

    def test_toLittleEndianHex_convertsHexStringToIntCorrectlyForInt(self):
        result = toLittleEndianHex(1404)
        self.assertEqual("7c05", result)

    def test_toLittleEndianHex_transformsEndianessCorrectlyForStringMissingLeadingZero(self):
        result = toLittleEndianHex("57C")
        self.assertEqual("7C05", result)

    def test_toBigEndianHex_transformsEndianessCorrectly(self):
        result = toBigEndianHex("057C")
        self.assertEqual("7C05", result)

    def test_toBigEndianHex_transformsEndianessCorrectlyForInt(self):
        result = toBigEndianHex(1404)
        self.assertEqual("7c05", result)

    def test_toBigEndianHex_transformsEndianessCorrectlyForStringMissingLeadingZero(self):
        result = toBigEndianHex("57C")
        self.assertEqual("7C05", result)

    def test_hexStringToInArray_convertsStringCorrectly(self):
        result = hexStringToIntArray("057C")
        self.assertEqual([5, 124], result)


if __name__ == '__main__':
    unittest.main()
