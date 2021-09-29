import re

def add(string:str) -> any:
    if string == "":
        return 0

    if len(string) == 1:
        return int(string)

    if len(string) > 1:
        string_list = re.split(",|\n|;", string)
        sum = 0
        negatives = []
        
        for str in string_list:
            if "-" in str:
                negatives.append(str)
                break
            if str.isdigit():
                num = int(str)
                sum += num

        if negatives != []:
            raise ValueError(f"Negatives not allowed {negatives}")
        return sum
