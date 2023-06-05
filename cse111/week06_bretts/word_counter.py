from datetime import datetime
import re
import os
import openai
openai.api_key = "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"


# Expected Output

# Title
# Instructions

# Inputs:
#   1. File to read (ie., filename1.txt):
#   2. Add keyword to scan? or (done)
#   3. Redundant word threshold (0-100+):

# Output:
#   Scanned Keywords:
#   'keyword1' used 5 times.
#   'keyword2' not found.
#   ...

#   Threshold Words:
#   3 - word 1
#   5 - word 6
#   ...

#   Print full word list? (yes or no):
#   Sort by: (alpha, hilow, or end):
#   8 - word 21
#   5 - word 6
#   2 words used over 5 times.
#   ...

#   200 Words scanned in article_name. Goodbye!
#   Date/Time stamp


keyword_list = []


def main():
    os.system("cls")

    # Word Counter Intro
    print("WORD COUNTER")
    print("Can be used to scan any text file for redundant words or targeted keywords.\n")

    # Try to open a txt file
    try:
        input_file = input("File to read (ie., proposal.txt): ")

        # Test file is found
        get_word_list(input_file)

        # Add multiple keywords to scan
        add_keywords(keyword_list)

        # Enter threshold of redundant words shown
        input_threshold = 0
        while input_threshold <= 0:
            try:
                input_threshold = int(
                    input("\nRedundant word threshold (1-100+): "))
            except ValueError:
                print("Use a number")

        # Create word count dictionary
        word_count_dict = word_count(get_word_list(input_file))

        print("\nScanned Keywords:")

        # Scan dictionary and show input keywords
        get_keyword_counts(word_count_dict)

        # Scan dictionary and show above threshold words
        get_threshold_words(input_threshold, word_count_dict)

        # Input if user wants full word list printed
        input_full_list = input(
            "\nPrint full word list? (yes or no): ").lower()
        get_full_list_option(input_full_list, word_count_dict)

        # ------ Added OpenAI -------

        prompt = f'Write a 3 sentence fable in "{get_word_list(input_file)}" and end it with " The End."'
        res = run_model(prompt, openai.api_key)

        # ---------------------------

        # Goodbye footer
        print(
            f"\n{len(get_word_list(input_file))} words scanned in {input_file}. Goodbye!")
        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %Y  %I:%M:%S %p}\n")

    except (FileNotFoundError, PermissionError) as error:
        print("\nError: missing file")
        print(error)
        print()


def get_word_list(input_file):

    i = 0
    with open(input_file) as f:

        if input_file.endswith(".csv"):
            word_list = f.read().split(",")
        else:
            word_list = f.read().split()

        for i in range(len(word_list)):
            word_list[i] = re.sub("[^a-zA-Z]+", "", word_list[i]).lower()

        for words in word_list:
            if len(words) == 1:
                word_list.remove(words)

    word_list = ' '.join(word_list).split()

    return word_list


def add_keywords(keyword_list):

    keyword = ""

    print()
    while keyword != "done":

        keyword = input("Add keyword to scan? or (done) ").lower()

        if keyword != "" and keyword != "done":
            keyword_list.append(keyword)
            print(
                f"'{keyword.title()}' was added to your keyword list.\n")

    return keyword_list


def word_count(word_list):

    word_count_dict = {item: word_list.count(item) for item in word_list}
    return word_count_dict


def sorted_highest_usage(word_count_dict):

    for key, value in sorted(word_count_dict.items(), key=lambda kv: kv[1], reverse=True):
        print(f"{value} - {key}")

    # Added return to test key value variables
    test_sort = {key: value}
    return test_sort


def sorted_alphabetical(word_count_dict):

    for key in sorted(word_count_dict.keys()):
        print(f"{word_count_dict[key]} - {key}")


def get_full_list_option(input_full_list, word_count_dict):

    if input_full_list == "yes":
        while input_full_list == "yes":
            input_sort_list = input(
                "\nSort by: (alpha, hilow, or done): ").lower()
            if input_sort_list == "alpha":
                sorted_alphabetical(word_count_dict)
            elif input_sort_list == "hilow":
                sorted_highest_usage(word_count_dict)
            else:
                break


def get_threshold_words(input_threshold, word_count_dict):

    print(f"\nThreshold Words")
    i = 0

    for keyword in word_count_dict:

        if int(word_count_dict[keyword]) > input_threshold:
            print(
                f"{word_count_dict[keyword]} - {keyword}")
            i += 1

    print(f"{i} words used over {input_threshold} times.")


def get_keyword_counts(word_count_dict):

    for keyword in keyword_list:
        if keyword in word_count_dict:
            if int(word_count_dict[keyword]) < 2:
                print(f"'{keyword}' used {word_count_dict[keyword]} time.")
            else:
                print(
                    f"'{keyword}' used {word_count_dict[keyword]} times.")
        else:
            print(
                f"'{keyword}' not found.")


def run_model(prompt, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    for r in response['choices']:
        print(r['text'])

    return response


if __name__ == "__main__":
    main()
