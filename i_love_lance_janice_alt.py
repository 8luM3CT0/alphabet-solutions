#def solution(x):
#    dictionary = {
#        "a": "z", "b": "y", "c" : "x", "d": "w", "e": "v", "f": "u", "g": "t",
#        "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m",
#        "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u":"f", "v": "e",
#        "w": "d", "x": "c", "y": "b", "z": "a"
#    }

#    decrypted = []

#    for char in x:
#        if dictionary.__contains__(ord(char)):
#            decrypted.append(chr(dictionary[ord(char)]))
#        else:
#            decrypted.append(char)

#    decrypted = ''.join(decrypted)
#    print(decrypted)

def solution(secret):
    cipher_dict = {
                    "a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s",
                    "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k",
                    "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c",
                    "y": "b", "z": "a"
                   }
    decrypted = list()
    for char in secret:
        if char in cipher_dict:
            decrypted.append(cipher_dict[char])
        else:
            decrypted.append(char)
    decrypted = ''.join(decrypted)
    print(decrypted)

    if __name__ == "__main__":
        print('ALT FOOBAR CHALLENGE 1 SOLUTION')

        print('--------------------------------------------------')

        print('Alternative solution test for test 1:')
        
        test_1 = input("Enter the encrypted message >>>>>>")

        print(solution(test_1))

        test_2 = input("Enter the second message >>>>>>>")
        
        print('Alternative solution for test 2:')

        print(solution(test_2))