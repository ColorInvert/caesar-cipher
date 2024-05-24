# caesar-cipher


## A simple encryption, decryption, and brute-forcer for caesar ciphers

### By Casey Glidewell

#### What it is

This is a set of 3 functions, encrypt, decrypt, and crack, which use a caesar cipher to modify input strings. Description of function below:

encrypt(phrase,shift) [string, int]
Caesar shifts every alphabetical character in the input string by the input integer provided, and returns the modified string. Casing is maintained, and non-english-alphabetical characters are ignored.

decrypt(phrase,shift) [string, int]
Decrypts a Caesar shifted message, if you know what shift value was used to encrypt it. This functions exactly like encrypt, but inverts your provided int value.

crack(phrase) [string]
Attempts to brute force decrypt an encrypted input string by comparing every word in the input string with a corpus, that consists of the 10,000 most common english words, but cut down to remove any word with a letter count below 5. If a valid, common 5+ letter word is found, phrase is considered decrypted, and is returned. otherwise, an empty string is returned.

**Note that this means crack() will give false negatives for any input phrase that does not have any 5+ letter words, or any common words.**


Proper performance of the above functions can be verified through provided pytests.


##### acknowledgements

corpus.txt is lifted from [Josh Kaufman's google-10000-english repository](https://github.com/first20hours/google-10000-english?tab=License-1-ov-file),
specifically the "google-10000-english-no-swears" file, and modified by myself to remove all entries that were below 5 characters long.

The license of the aforementioned repository is as follows:

```
Data files are derived from the Google Web Trillion Word Corpus, as described by Thorsten Brants and Alex Franz, and distributed by the Linguistic Data Consortium. Subsets of this corpus distributed by Peter Novig. Corpus editing and cleanup by Josh Kaufman.

Educational and personal/research use of this data is permitted under the LDC license, Norvig's MIT license for his contributions, and US fair use doctrine. I do not recommend using this data for commercial purposes without licensing it from the Linguistic Data Consortium.
```

This repository, caesar-cipher by Casey Glidewell, was created for non-commercial educational practice.