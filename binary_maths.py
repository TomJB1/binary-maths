from math import remainder

class binaryNum:
    def __init__(self, number) -> None:
        print("number:", number, type(number))
        self.number = int(number)

    def __str__(self) -> str:
        return self._dec_to_bin(self.number)
    
    def __add__(self, other) -> object:
        return binaryNum((self.number + other.number))
    
    def __sub__(self, other) -> object:
        return binaryNum((self.number - other.number))
    
    def __int__(self) -> int:
        return self.number
    
    def binary(self):
        return self._dec_to_bin(self.number)

    def _dec_to_bin(self, num, bin="", bits=[0, 1]):
        bits = [0, 1]
        bin = ""
        if(num < 0):
            num = (-num) -1
            bits = [1,0]
        while(num > 0):
            bin = str(bits[ (abs(int(remainder(num, 2)))) ])+bin
            num = num // 2
        return str(bits[0])+bin