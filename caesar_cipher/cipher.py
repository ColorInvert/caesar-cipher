# Import Regex library
import re


# Encrypt our phrase with a caesar shift. Takes argument of phrase,
# and how many characters to caesar shift it.
def encrypt(phrase, shift):

    # Convert user's shift value into modulo 26 value, to handle
    # values over 26 gracefully.
    shift = shift % 26

    # Convert input phrase into a list of individual chars, to facilitate
    # in-place modification and for i in range iteration.
    phrase_list = list(phrase)

    # Iterate through each character of phrase_list, to look for and
    # modify any alpha characters.
    for i in range(len(phrase_list)):

        # Is our current char a-z, capital OR lowercase?
        if re.match(r"[A-z]", phrase_list[i]) is not None:

            # Is our match lowercase?
            if ord(phrase_list[i]) >= 97 and ord(phrase_list[i]) <= 122:

                # Convert our match to the char associated with the ord of
                # the char + shift value
                phrase_list[i] = chr(ord(phrase_list[i]) + shift)

                # Check for underflow, and shift again upward 26 if so
                # to get back in range.
                if ord(phrase_list[i]) < 97:
                    phrase_list[i] = chr(ord(phrase_list[i]) + 26)

                # Check for overflow, and shift again downward 26 if so
                # to get back in range.
                elif ord(phrase_list[i]) > 122:
                    phrase_list[i] = chr(ord(phrase_list[i]) - 26)

            # is our match uppercase?
            elif ord(phrase_list[i]) >= 65 and ord(phrase_list[i]) <= 90:

                # Convert our match to the char associated with the ord of
                # the char + shift value
                phrase_list[i] = chr(ord(phrase_list[i]) + shift)

                # Check for underflow, and shift again upward 26 if so
                # to get back in range.
                if ord(phrase_list[i]) < 65:
                    phrase_list[i] = chr(ord(phrase_list[i]) + 26)

                # Check for overflow, and shift again downward 26 if so
                # to get back in range.
                elif ord(phrase_list[i]) > 90:
                    phrase_list[i] = chr(ord(phrase_list[i]) - 26)

    # With forloop complete, list is fully modified. Stringify it and return.
    output = "".join(phrase_list)
    return output


# Decryption is just running encrypt(), but with the shift value inverted
def decrypt(phrase, shift):

    decryption = encrypt(phrase, -shift)
    return decryption


# Brute force cipher with a dictionary "attack".
# Using a corpus of 10,000 most common english words, check if any
# possible shifted version of the phrase has at least 1 5 letter english
# word contained within.
#! THIS FUNCTION WILL RETURN NEGATIVE ON ANY INPUT THAT HAS NO 5 LETTER WORDS
def crack(phrase):

    # Open corpus
    with open("corpus.txt") as fp:
        contents = fp.read()

    # Convert corpus to a set for speed of iteration, split on newline
    corpus_words = set(contents.split("\n"))

    # Loop 26 times, encrypt-shifting by one each time, and checking
    # if we ever end up with a common english word as defined by our corpus.
    i = 0
    while i < 26:

        phrase = encrypt(phrase, 1)

        # Split the phrase into words, and compare against corpus list.
        phrase_words = re.findall(r"\b\w+\b", phrase)

        # Iterate through our phrase words, and check if any of them
        # are present in our corpus, if so, return the phrase.
        for word in phrase_words:
            if word in corpus_words:
                return phrase

        i += 1

    # Sensible version of phrase not found, return empty string.
    return ""
