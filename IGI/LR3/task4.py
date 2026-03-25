import ui

def calc_words_with_len_less_then_7(words):
    """
    Counts how many words have a length less than 7.

    Parameters:
        words (list of str): A list of words (strings).

    Returns:
        int: The number of words whose length is less than 7.
    """
    lens = [len(word) for word in words]
    return sum(1 for len in lens if len < 7)

def find_min_len_word_ends_with_a(words):
    """
    Finds the shortest word that ends with the letter 'a'.

    If multiple words have the same minimal length, the first encountered is returned.
    If no word ends with 'a', returns an empty string.

    Parameters:
        words (list of str): A list of words (strings).

    Returns:
        str: The shortest word ending with 'a', or an empty string if none found.
    """
    lens = [len(word) for word in words]
    min_len = max(lens) + 1
    min_len_word = ""
    for word in words:
        if word.endswith('a') and len(word) < min_len:
            min_len = len(word)
            min_len_word = word
    return min_len_word

def main():
    """
    Main function that reads a string from the user, splits it into words,
    removes commas from each word, and then:
    1. Prints the number of words shorter than 7 characters.
    2. Prints the shortest word ending with 'a'.
    3. Prints the list of words sorted by length in descending order.
    """
    str = ui.read_str("Enter a string to analyse:\n")
    words = str.split(" ")
    for i in range(len(words)):
        words[i] = "".join(character for character in words[i] if character != ',')
 
    print(f"Number of words with length < 7: {calc_words_with_len_less_then_7(words)}")
    
    print(f"Word with minimum length from ending with 'a' is {find_min_len_word_ends_with_a(words)}")

    print(sorted(words, key = lambda word: len(word), reverse=True))