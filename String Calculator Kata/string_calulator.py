import re

def add(string:str) -> any:
    if string == "":
        return 0

    if len(string) == 1:
        return int(string)

    if len(string) > 1:
        string_list = re.split(",|\n", string)
        sum = 0
        
        for str in string_list:
            num = int(str)
            sum += num
        
        return sum
