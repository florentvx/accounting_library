from __future__ import annotations
import math

class asset:
    def __init__(
            self, 
            name = "USD", symbol = "$", 
            decimal_symbol = ".", separator_symbol = ",", 
            decimal_param = 2, separator_param = 3
        ):
        self.name = name
        self.symbol = symbol
        self.decimal_symbol = decimal_symbol
        self.separator_symbol = separator_symbol
        self.decimal_param = decimal_param
        self.separator_param = separator_param
    
    def __repr__(self):
        return self.name
    
    def __hash__(self):
        return (self.name + self.symbol + self.decimal_symbol + self.separator_symbol + \
            str(self.decimal_param)+ str(self.separator_param)).__hash__()

    def __eq__(self, other: asset):
        return self.__hash__() == other.__hash__()

    def copy(self) -> asset:
        return asset(
            self.name + '',
            self.symbol + '',
            self.decimal_symbol + '',
            self.separator_symbol + '',
            self.decimal_param + 0,
            self.separator_param + 0,
        )
    
    def show_value(self, value):
        if value == 0:
            return f'{self.symbol} 0'
        factor = 1 if value >= 0 else -1
        value = abs(value)
        remainer = int(round(value * 10 ** self.decimal_param - int(value)* 10 ** self.decimal_param,0))
        delta = 0
        if remainer == 10 ** self.decimal_param:
            remainer = 0
            delta = 1
        n = int(math.log(value + delta, 10)) + 1
        m = n % self.separator_param
        value_list = list(str(int(value) + delta))
        res = ''.join(value_list[:m])
        for i in range(int((n - m) / self.separator_param)):
            if res != '':
                res += self.separator_symbol
            res += ''.join(value_list[(m+i*self.separator_param):(m+(i+1)*self.separator_param)])
        return f"{'- ' if factor<0 else ''}{self.symbol} {res}{'.' + str(remainer) if remainer !=0 else ''}"
