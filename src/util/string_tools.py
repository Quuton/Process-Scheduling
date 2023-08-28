def join_all_strings(*args:str, **kwargs:str):
    sep = kwargs.get("sep", "\n")

    temp = ""
    for i in args:
        temp += i + sep
    
    return temp
