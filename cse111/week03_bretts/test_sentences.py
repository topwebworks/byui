from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random  # Not needed. Randomized only in sentences.py
import pytest


single_determiners = ["a", "one", "the"]

plural_determiners = ["some", "many", "the"]

single_nouns = ["bird", "boy", "car", "cat", "child",
                "dog", "girl", "man", "rabbit", "woman"]

plural_nouns = ["birds", "boys", "cars", "cats", "children",
                "dogs", "girls", "men", "rabbits", "women"]

past_verbs = ["drank", "ate", "grew", "laughed", "thought",
              "ran", "slept", "talked", "walked", "wrote"]

present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                        "runs", "sleeps", "talks", "walks", "writes"]

present_plural_verbs = ["drink", "eat", "grow", "laugh", "think",
                        "run", "sleep", "talk", "walk", "write"]

future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                "will think", "will run", "will sleep", "will talk",
                "will walk", "will write"]

prepositions = ["about", "above", "across", "after", "along",
                "around", "at", "before", "behind", "below",
                "beyond", "by", "despite", "except", "for",
                "from", "in", "into", "near", "of",
                "off", "on", "onto", "out", "over",
                "past", "to", "under", "with", "without"]

adjectives = ["big", "young", "wrinkly", "happy", "sad",
              "plump", "tall", "short", "smelly", "round",
              "bouncy", "soft", "ghastly", "pretty", "scary"]


def test_get_determiner():
    # 1. Test the single determiners.

    # single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    # plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


# Duplicated test function structure - see comments above
def test_get_noun():

    for _ in range(4):

        word = get_noun(1)
        assert word in single_nouns

    for _ in range(4):

        word = get_noun(2)
        assert word in plural_nouns


def test_get_verb():

    for _ in range(4):

        word = get_verb(1, "past")
        assert word in past_verbs

    for _ in range(4):

        word = get_verb(1, "present")
        assert word in present_single_verbs

    for _ in range(4):

        word = get_verb(2, "present")
        assert word in present_plural_verbs

    for _ in range(4):

        word = get_verb(1, "future")
        assert word in future_verbs


def test_get_preposition():

    for _ in range(4):

        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():

    phrase = get_prepositional_phrase(1)
    phrase_list = phrase.split()
    assert len(phrase_list) == 3  # Check for 3 words
    assert phrase_list[0] in prepositions  # Check for preposition
    assert phrase_list[1] in single_determiners  # Check for single determiner
    assert phrase_list[2] in single_nouns  # Check for single noun

    phrase = get_prepositional_phrase(2)
    phrase_list = phrase.split()
    assert len(phrase_list) == 3  # Check for 3 words
    assert phrase_list[0] in prepositions  # Check for preposition
    assert phrase_list[1] in plural_determiners  # Check for plural determiner
    assert phrase_list[2] in plural_nouns  # Check for plural noun


def test_get_adjective():

    for _ in range(4):

        word = get_adjective()
        assert word in adjectives


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
