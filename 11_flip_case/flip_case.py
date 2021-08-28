def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ''
    for s in phrase:
        if s == to_swap and s.isupper():
           new_phrase += s.lower()

        elif s == to_swap and s.islower():
           new_phrase += s.upper()

        else:
            new_phrase += s
    return new_phrase
            
        
    
