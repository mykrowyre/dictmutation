

import argparse
import codecs

def alternate_case(word, upperfirst=True):
    if upperfirst:
        c = 1
    else:
        c = 0
    newword = ""
    for char in word:
        if c == 1:
            if char.isnumeric() is False:
                char = char.upper()
            c = 0
        else:
            if char.isnumeric() is False:
                char = char.lower()
            c = 1
        newword += char

    return newword

def run(args):

    cfile = codecs.open(filename=args.chars, mode="r")
    file = codecs.open(filename=args.words, mode="r")
    chars = {}
    for word in cfile:
        chars[word[0]] = word.replace("\n","")

    cfile.close()
    for word in file:
        word = word.replace("\n","")
        if word is None or word == "":
            continue
        current = None
        while True:
            current = incremement_word(args, word, current, chars)
            if current is None:
                break
            print(current)
            if args.altcase:
                print(alternate_case(current, True))
                print(alternate_case(current, False))
            if args.rev:
                print(current[::-1])
                if args.altcase:
                    print(alternate_case(current[::-1], True))
                    print(alternate_case(current[::-1], False))
            if args.add:
                print(current+args.add)
                if args.altcase:
                    print(alternate_case(current+args.add, True))
                    print(alternate_case(current+args.add, False))
                if args.rev:
                    print((current+args.add)[::-1])
                    if args.altcase:
                        print(alternate_case((current+args.add)[::-1], True))
                        print(alternate_case((current+args.add)[::-1], False))

            if args.adde:
                print(current+"!")
                if args.altcase:
                    print(alternate_case(current+"!", True))
                    print(alternate_case(current+"!", False))
                if args.rev:
                    print((current+"!")[::-1])
                    if args.altcase:
                        print(alternate_case((current+"!")[::-1], True))
                        print(alternate_case((current+"!")[::-1], False))

            if args.adde and args.addq:
                print(current+"!?")
                if args.altcase:
                    print(alternate_case(current+"!?", True))
                    print(alternate_case(current+"!?", False))
                if args.rev:
                    print((current+"!?")[::-1])
                    if args.altcase:
                        print(alternate_case((current+"!?")[::-1], True))
                        print(alternate_case((current+"!?")[::-1], False))

                print(current+"?!")
                if args.altcase:
                    print(alternate_case(current+"?!", True))
                    print(alternate_case(current+"?!", False))
                if args.rev:
                    print((current+"?!")[::-1])
                    if args.altcase:
                        print(alternate_case((current+"?!")[::-1], True))
                        print(alternate_case((current+"?!")[::-1], False))


    file.close()


def replace_character (word, position, newchar):
    temp = list(word)
    temp[position] = newchar
    word = "".join(temp)
    return word

def incremement_word(args, original, current, chars):

    if current is None:
        if original is None:
            return None
        current = original
        return current

    l = len(original)
    l2 = len(chars)-1
    for i in range(l,0,-1):
        co = original[i-1:i]
        cc = current[i-1:i]
        if co not in chars:
            if i == 1:
                return None
            continue

        p = chars[co].find(cc)

        if p == -1:
            continue
        if p == len(chars[co])-1:
            current = replace_character(current, i-1, chars[co][0])
            if i == 1:
                return None
        else:
            current = replace_character(current, i-1, chars[co][p+1])
            break
    return current

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mykrowyres word twister')
    parser.add_argument('words', nargs='?', help='words file', default='words.txt')
    parser.add_argument('chars', nargs='?', help='characters file', default='chars.txt')
    parser.add_argument('--rev', action='store_true', help='include reverse of resulting word', default=False)
    parser.add_argument('-add',  nargs='?', help='append again with string. multiple chars one at a time', default=None)
    parser.add_argument('--addq', action='store_true', help='append again with question mark', default=False)
    parser.add_argument('--adde', action='store_true', help='append again with exclamation mark', default=False)
    parser.add_argument('--altcase', action='store_true', help='Alternate upper and lower', default=False)

    args = parser.parse_args()
    run(args)

# Template
# a = alpha lower case only
# A = alpha upper case only
# # = numeric only
# c = any from characters


