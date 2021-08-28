def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = ""
    new_phrase += phrase[0].upper()

    for s in phrase[1:]:
        new_phrase += s
    return new_phrase
        
