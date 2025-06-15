def capitalize_and_join(sentence):
    words = sentence.split()
    capitalized_letters = [word[0].upper() for word in words if word]
    return ''.join(capitalized_letters)
    