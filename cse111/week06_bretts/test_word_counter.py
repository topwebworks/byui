from word_counter import word_count, sorted_highest_usage
import pytest

"""First test checks the word count function for unique entries. The second test checks duplicate word entries. The third test checks that key and value are being passed properly in the sort function."""


def test_word_count_returns_dictionary_of_single_words():
    word_list = ['see', 'john', 'run', 'up', 'the', 'hill']
    actual_dictionary = word_count(word_list)
    expected_dictionary = {"see": 1, "john": 1,
                           "run": 1, "up": 1, "the": 1, "hill": 1}

    assert "up" in word_count(word_list)
    assert "john" in expected_dictionary
    assert expected_dictionary == actual_dictionary


def test_word_count_returns_dictionary_of_duplicate_words():
    word_list = ['see', 'see', 'see', 'run', 'run', 'hill']
    actual_dictionary = word_count(word_list)
    expected_dictionary = {"see": 3, "run": 2, "hill": 1}

    assert "hill" in word_count(word_list)
    assert "run" in expected_dictionary
    assert expected_dictionary == actual_dictionary


def test_sorted_key_value_are_working():
    word_count_dict = {"see": 3}
    actual_key_value = sorted_highest_usage(word_count_dict)
    expected_key_value = {"see": 3}

    assert "see" in sorted_highest_usage(word_count_dict)
    assert expected_key_value == actual_key_value


pytest.main(["-v", "--tb=line", "-rN", __file__])
