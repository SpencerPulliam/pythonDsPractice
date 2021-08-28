def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    def is_vowel(letter):
        vowels = 'aeiouAEIOU'
        if letter in vowels:
            return True
        else:
            return False

    vowel_count = {}
    phrase = phrase.lower()
    for letter in phrase:
        if is_vowel(letter):
                vowel_count[letter] = phrase.count(letter)
    return vowel_count
