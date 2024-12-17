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
    
    def show_value(self, value):
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

class fx_market:
    def __init__(self):
        self.quotes : dict[tuple[asset, asset], float] = {}

    def _filter_quote_dict(
            self, 
            asset: asset, 
            quote_dict = None,
            filter_asset_list : list[asset] = [],
        ) -> dict[tuple[asset, asset], float]:
        if quote_dict is None:
            quote_dict = self.quotes
        return {
            k: v 
            for (k, v) in quote_dict.items() 
            if (k[0] == asset or k[1] == asset) and \
                (k[0] not in filter_asset_list and k[1] not in filter_asset_list)
        }

    def _get_quote(self, asset1: asset, asset2: asset, filter_asset_list : list[asset] = []):
        if asset1 == asset2:
            return 1.0
        asset1_dict = self._filter_quote_dict(asset1, filter_asset_list=filter_asset_list)
        if len(asset1_dict) == 0:
            return None
        direct : dict[tuple[asset, asset], float] = self._filter_quote_dict(
            asset2, 
            quote_dict=asset1_dict, 
            filter_asset_list=filter_asset_list
        )
        if len(direct) != 0:
            assert len(direct) == 1
            [(key, value)] = list(direct.items())
            if key[0] == asset1:
                return value
            else:
                return 1 / value
        for asset_key in asset1_dict.keys():
            asset_k = asset_key[1]
            asset_value = asset1_dict[asset_key]
            if asset_key[1] == asset1:
                asset_k = asset_key[0]
                asset_value = 1/asset_value
            res = self._get_quote(
                asset_k, asset2, 
                filter_asset_list = [asset1] + filter_asset_list
            )
            if not res is None:
                result = asset_value * res
                self.quotes[(asset1, asset2)] = result
                return result
            
    def get_quote(self, asset1, asset2):
        return self._get_quote(asset1, asset2)
    
    def add_quote(self, asset1, asset2, rate):
        if self.get_quote(asset1, asset2) is None:
            self.quotes[(asset1, asset2)] = rate
            return True
        return False
