def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    count = str(search_term)
    str_lst = []
    for x in lst:
        str_lst.append(str(x))

    return str_lst.count(count)