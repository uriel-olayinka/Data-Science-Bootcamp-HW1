def count_vowels(word):
    num_vowels = 0
    for letter in word:
        if letter in "AEIOUaieou":
            num_vowels += 1
    return num_vowels


def main():
    word = "Uriel"
    print(count_vowels(word))


main()
