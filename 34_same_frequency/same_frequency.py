def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = list(str(num1))
    str_num2 = list(str(num2))

    count1 = {}
    count2 = {}

    for i in str_num1:
        count1[i] = str_num1.count(i)
    
    for j in str_num2:
        count2[j] = str_num2.count(j)

    count1 = dict(sorted(count1.items()))
    count2 = dict(sorted(count2.items()))

    print(count1)
    print(count2)

    if count1 == count2:
        return True
    else:
        return False
    
    


