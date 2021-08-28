def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    a = []
    b = []
    c = [a, b]

    def is_even(lst):
        for n in lst:
            if n % 2 == 0:
                a.append(n)
            else:
                b.append(n)

    def is_string(lst):
        for s in lst:
            if isinstance(s, str):
                a.append(s)
            else:
                b.append(s)
    
    if fn == 'is_even':
        is_even(lst)

    elif fn == 'is_string':
        is_string(lst)
    
    elif fn != 'is_even' or fn != 'is_string':
        return None

    return c
   



    

    