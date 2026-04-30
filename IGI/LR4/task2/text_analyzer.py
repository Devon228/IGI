'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: text_analyzer
Provides mixin classes and functions for text analysis:
- sentence counting and classification
- smiley detection
- date (year) extraction
- word pattern matching
'''

import re
from typing import List, Tuple, Dict, Any

class TextAnalysisMixin:
    """
    Mixin class that adds text analysis capabilities.
    Requires self.text attribute (string) to be set.
    """

    @property
    def _text(self) -> str:
        """Override this property in the target class."""
        raise NotImplementedError("TextAnalysisMixin requires _text property")

    def count_sentences(self) -> int:
        """
        Count total number of sentences in text.
        Sentences end with ., !, ? (including multiple punctuation like ...?).
        """
        sentences = re.split(r'[.!?]+', self._text)
        sentences = [s.strip() for s in sentences if s.strip()]
        return len(sentences)

    def classify_sentences(self) -> Dict[str, int]:
        """
        Classify sentences into declarative (.), interrogative (?), imperative (!).
        Returns dict with keys: 'declarative', 'interrogative', 'imperative'.
        """
        endings = re.findall(r'[.!?]+(?=\s|$)', self._text)
        counts = {'declarative': 0, 'interrogative': 0, 'imperative': 0}
        for end in endings:
            if '?' in end:
                counts['interrogative'] += 1
            elif '!' in end:
                counts['imperative'] += 1
            else:
                counts['declarative'] += 1
        return counts

    def average_sentence_length_chars(self) -> float:
        """
        Average number of characters in a sentence (only letters/words, not spaces/punctuation).
        Returns total letters / number of sentences.
        """
        letters_only = re.sub(r'[^a-zA-Zа-яА-ЯёЁ]', '', self._text)
        num_sentences = self.count_sentences()
        if num_sentences == 0:
            return 0.0
        return len(letters_only) / num_sentences

    def average_word_length(self) -> float:
        """
        Average length of a word in characters.
        Words are sequences of letters (Unicode alphabetic).
        """
        words = re.findall(r'\b\w+\b', self._text, flags=re.UNICODE)
        if not words:
            return 0.0
        total_chars = sum(len(w) for w in words)
        return total_chars / len(words)

    def count_smileys(self) -> int:
        """
        Count smileys matching pattern:
        Starts with ; or : , then zero or more '-', then one or more identical brackets from ()[].
        """
        # Pattern: [;:] -* ( bracket ) \1*
        # Use backreference to ensure identical brackets
        pattern = r'[;:]-*([\(\)\[\]])\1*'
        matches = re.findall(pattern, self._text)
        return len(matches)

    def extract_dates_year(self) -> List[str]:
        """
        Extract all four-digit years (like 2007, 2020) from text.
        Returns list of strings.
        """
        pattern = r'\b\d{4}\b'
        dates = re.findall(pattern, self._text)
        return dates

    def get_words_with_conditions(self) -> List[str]:
        vowels = 'aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ'
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
        pattern = rf'\b\w*[{consonants}][{vowels}]\w\b'
        return re.findall(pattern, self._text, flags=re.UNICODE)

    def count_words_starting_with_vowel(self) -> int:
        vowels = 'aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ'
        pattern = rf'\b[{vowels}]\w*\b'
        matches = re.findall(pattern, self._text, flags=re.UNICODE)
        return len(matches)
    
    def find_words_with_double_letters(self) -> List[Tuple[int, str]]:
        """
        Find words containing two identical letters in a row.
        Returns list of tuples (word_index, word) where index starts from 1.
        """
        words = re.findall(r'\b\w+\b', self._text, flags=re.UNICODE)
        result = []
        for idx, w in enumerate(words, start=1):
            if re.search(r'(.)\1', w):
                result.append((idx, w))
        return result

    def get_sorted_words_alphabetically(self) -> List[str]:
        """
        Return all words in text sorted alphabetically (case-insensitive, but original case preserved).
        """
        words = re.findall(r'\b\w+\b', self._text, flags=re.UNICODE)
        words.sort(key=lambda x: x.lower())
        return words