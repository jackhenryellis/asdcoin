"""
A program that decrypts the multiple layers of encryption
present on the Australian Signal Directorate's
75th Anniversary Commemorative Coin.
For more information, visit:
https://www.asd.gov.au/75th-anniversary/events/2022-09-01-75th-anniversary-commemorative-coin
"""


import itertools


def split(string, n):
    """
    splits a string into a list of strings n long
    """
    string_list = [string[start:start+n] for start in range(0, len(string), n)]
    return string_list


def list2string(l, sep):
    """
    returns the string containing all elements in a list
    with a seperator of 'sep' between each value
    """
    string = sep.join(map(str, l))
    return string


def puzzle_one():
    """
    PUZZLE 1 - braille on coin side B
    Braille letters are written under certain letters
    of 'ELIZABETH II AUSTRALIA 2022'
    The letters with braille below are B, T, H, A, S, and A
    The corresponding braille letters are C, B, F, A, E, and D
    """

    p1 = ['B', 'T', 'H', 'A', 'S', 'A']
    braille = ['C', 'B', 'F', 'A', 'E', 'D']

    # zip the braille letters with their corresponding letters on the coin
    combination = zip(braille, p1)

    # sort the braille letters into alphabetical order
    sorted_combination = sorted(combination, key=lambda x: x[0])

    # create a dictionary containing
    # the sorted braille keys and their corresponding values
    p1_dict = dict(sorted_combination)

    # output PUZZLE 1 answer
    print("PUZZLE 1:")
    print("Marked letters on coin: {}".format(list2string(p1, "")))
    print("Corresponding braille letters: {}".format(list2string(braille, "")))
    print("-------------------------------------")
    print("Rearranged braille letters: {}".format(list2string(p1_dict.keys(), "")))
    print("Corresponding letters on coin: {}".format(list2string(p1_dict.values(), "")))
    print("\n")


def puzzle_two():
    """
    PUZZLE 2 - ciphertext on coin side A outer ring
    the result of puzzle 1 was ATBASH
    hinting that puzzle 2 can be decrypted using the Atbash cipher, where
    A -> Z
    B -> Y
    C -> X
    ...
    Z -> A
    """

    p2 = ".DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS"

    # create a lookup table for the atbash cipher
    atbash = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
            'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
            'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
            'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
            'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

    # set an empty string to add plaintext characters to
    p2_plaintext = ""

    # compare each character in the ciphertext to
    # its corresponding character in the atbash lookup table
    # and add them to the plaintext string
    for char in p2:
        if not char.isalpha():
            p2_plaintext += char
            continue
        p2_plaintext += atbash[char]

    # output PUZZLE 2 ciphertext and plaintext
    print("PUZZLE 2:")
    print(f"Ciphertext:\n{p2}")
    print(f"\nPlaintext:\n{p2_plaintext}\n\n")


def puzzle_three():
    """
    PUZZLE 3 - coin side A inner ring
    the plaintext from puzzle 2 hints "FINDCLARITYIN7WIDTHX5DEPTH"
    suggesting that the ciphertext for puzzle 3
    can be inserted into a 7x5 matrix
    """

    p3 = "BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5"

    # ciphertext is 70 characters long, so we must split into
    # 2 separate lists of 35 characters
    p3_first = list(p3[:35])
    p3_second = list(p3[35:])

    # create a list of lists, each containing 7 characters
    # for both halves
    p3_first_rows = split(p3_first, 7)
    p3_second_rows = split(p3_second, 7)
    # output of each of the above variables
    # is readable vertically,
    # so unpack first index of each row,
    # then the second, and so on
    # for both matrices
    p3_unpacked = []
    p3_unpacked.append([i[0] for i in p3_first_rows])
    p3_unpacked.append([i[1] for i in p3_first_rows])
    p3_unpacked.append([i[2] for i in p3_first_rows])
    p3_unpacked.append([i[3] for i in p3_first_rows])
    p3_unpacked.append([i[4] for i in p3_first_rows])
    p3_unpacked.append([i[5] for i in p3_first_rows])
    p3_unpacked.append([i[6] for i in p3_first_rows])
    p3_unpacked.append([i[0] for i in p3_second_rows])
    p3_unpacked.append([i[1] for i in p3_second_rows])
    p3_unpacked.append([i[2] for i in p3_second_rows])
    p3_unpacked.append([i[3] for i in p3_second_rows])
    p3_unpacked.append([i[4] for i in p3_second_rows])
    p3_unpacked.append([i[5] for i in p3_second_rows])
    p3_unpacked.append([i[6] for i in p3_second_rows])

    # unpack list of lists into a single list
    p3_unpacked = list(itertools.chain(*p3_unpacked))

    # convert the list to a single string
    p3_plaintext = list2string(p3_unpacked, '')

    # output PUZZLE 2 ciphertext and plaintext
    print("PUZZLE 3:")
    print(f"Ciphertext:\n{p3}")
    print(f"\nPlaintext:\n{p3_plaintext}\n\n")


def puzzle_four():
    """
    PUZZLE 4 - hexadecimal
    """

    p4 = "E3B" +\
         "8287D4" +\
         "290F723381" +\
         "4D7A47A291DC" +\
         "0F71B2806D1A53B" +\
         "311CC4B97A0E1CC2B9" +\
         "3B31068593332F10C6A335" +\
         "2F14D1B27A3514D6F7382F1A" +\
         "D0B0322955D1B83D3801CDB2" +\
         "287D05C0B82A311085A03329" +\
         "1D85A3323855D6BC333119D" +\
         "6FB7A3C11C4A72E3C17CCB" +\
         "B33290C85B6343955CCBA3" +\
         "B3A1CCBB62E341ACBF72" +\
         "E3255CAA73F2F14D1B27A" +\
         "341B85A3323855D6BB33" +\
         "3055C4A53F3C55C7B22" +\
         "E2A10C0B97A291DC0F" +\
         "73E3413C3BE392819" +\
         "D1F73B331185A33" +\
         "23855CCBA2A3" +\
         "206D6BE383" +\
         "1108B"

    p4_key = "A5D75"

    # extend key to match length of p4 hex
    p4_key *= len(p4)//5
    p4_key += p4_key[:(len(p4) % len(p4_key))] 

    # divide hex into byte sized chunks
    p4_bytes = split(p4, 2)
    p4_key_bytes = split(p4_key, 2)

    # zip puzzle bytes and key bytes together
    bytes_to_xor = zip(p4_bytes, p4_key_bytes)

    # declare a list to store the results of the xor operation
    p4_plaintext = []

    # convert hex to base 10, xor puzzle with key
    # and append byte in ascii to plaintext list
    for i in bytes_to_xor:
        # convert hex to base 10 int
        puzzle = int(i[0], base=16)
        key = int(i[1], base=16)
        # xor puzzle byte with key byte
        xor_result = puzzle ^ key
        # convert result of xor to ASCII
        ascii_result = chr(xor_result)
        p4_plaintext.append(ascii_result)

    # output PUZZLE 4 ciphertext and plaintext
    print("PUZZLE 4:")
    print(f"Ciphertext:\n{p4}")
    p4_plaintext = list2string(p4_plaintext, "")
    print(f"\nPlaintext:\n{p4_plaintext}")


def solve():
    # solve puzzle 1
    puzzle_one()
    # solve puzzle 2
    puzzle_two()
    # solve puzzle 3
    puzzle_three()
    # solve puzzle 4
    puzzle_four()


if __name__ == "__main__":
    solve()
