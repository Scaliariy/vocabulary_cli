import random


def get_data(filepath_local="vocabulary.txt"):
    with open(filepath_local, 'r', encoding='utf-8-sig') as file_local:
        data_local = file_local.readlines()
    return data_local


def convert(data_local):
    cleared_data_local = [word.strip('\n') for word in data_local]
    words_local = {}
    for key, value in zip(cleared_data_local[::2], cleared_data_local[1::2]):
        words_local[f"{key}"] = value
    print("Loaded words: ", len(words_local.keys()))
    return words_local


def get_words_set(words_local, amount_local):
    keys = list(words_local.keys())
    random_keys = random.sample(keys, amount_local)
    random_words_set = {key: words_local[key] for key in random_keys}
    return random_words_set


def interactive_printout(words_set_local):
    for key, val in words_set_local.items():
        print(f"W: \"{key}\"")
        input("Show translation? (Enter)")
        print(f"T: \"{val}\"")
        input("Next? (Enter)")
        print("-------------------------")


def reverse_interactive_printout(words_set_local):
    for key, val in words_set_local.items():
        print(f"T: \"{val}\"")
        input("Show word? (Enter)")
        print(f"W: \"{key}\"")
        input("Next? (Enter)")
        print("-------------------------")


def writing_printout(words_set_local):
    for key, val in words_set_local.items():
        print(f"T: \"{val}\"")
        answer = input("Word: ")
        try:
            if answer == key:
                print(f"Correct!")
            else:
                print(f"wrong: '{answer}' right: '{key}'")
        except ValueError:
            print("Incorrect value.")
            continue
        input("Next? (Enter)")
        print("-------------------------")


art = """
************************
*                      *
*                      *
*      Automatic       *
*      Vocabulary      *
*                      *
*                      *
************************
"""
print('\n\t', art)

data = get_data()
words = convert(data)
print("Hello! \nYou have two options: (1) word -> translate, (2) translate -> word, (3) writing.")

while True:
    try:
        amount = int(input("\nEnter size of word set: "))
    except ValueError:
        print("Incorrect value.")
        continue

    user_action = input("Chose (1),(2),(3): ")
    print('')

    words_set = get_words_set(words, amount)

    if user_action.startswith('1'):
        interactive_printout(words_set)
    elif user_action.startswith('2'):
        reverse_interactive_printout(words_set)
    elif user_action.startswith('3'):
        writing_printout(words_set)
    else:
        print("Incorrect value.")
