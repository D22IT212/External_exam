class NumeralConverter:
    @staticmethod
    def binary_to_decimal(binary_str):
        return int(binary_str, 2)

    @staticmethod
    def decimal_to_binary(decimal_int):
        return bin(decimal_int)[2:]

    @staticmethod
    def binary_to_octal(binary_str):
        decimal_value = NumeralConverter.binary_to_decimal(binary_str)
        return oct(decimal_value)[2:]

    @staticmethod
    def octal_to_binary(octal_str):
        decimal_value = int(octal_str, 8)
        return NumeralConverter.decimal_to_binary(decimal_value)

    @staticmethod
    def binary_to_hexadecimal(binary_str):
        decimal_value = NumeralConverter.binary_to_decimal(binary_str)
        return hex(decimal_value)[2:]

    @staticmethod
    def hexadecimal_to_binary(hexadecimal_str):
        decimal_value = int(hexadecimal_str, 16)
        return NumeralConverter.decimal_to_binary(decimal_value)
