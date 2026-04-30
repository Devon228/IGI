'''
Laboratory work number: 4. 
Version: 1.0.
Developer: Lukanski Dzmitry Mikalaevich.
Date: 25.04.2026.

Module: task2
Implements Task2 for text analysis.
Reads text from a file, analyzes using regular expressions,
displays results, saves to a file, archives with zipfile.
'''

import os
import zipfile
from datetime import datetime
from common.task import Task
from common.action import Action
from common.ui import read_str
from .text_analyzer import TextAnalysisMixin

class Task2(Task, TextAnalysisMixin):
    """Text analysis task implementing all required features."""
    name = "Task 2: Text Analysis"

    def __init__(self):
        self.input_filename = None
        self.text = ""
        self._analysis_results = {}

    @property
    def _text(self) -> str:
        """Required property for TextAnalysisMixin."""
        return self.text

    def menu_text(self) -> str:
        """Display menu header with current loaded file status."""
        if self.input_filename:
            return f"Text Analysis\nLoaded: {self.input_filename}"
        return "Text Analysis\nNo file loaded. Please load a text file first."

    def actions(self):
        """Define available actions."""
        return super().actions() + [
            Action("Load text file", self.load_file),
            Action("Analyze text and show results", self.analyze_and_show),
            Action("Save results to file", self.save_results_to_file),
            Action("Archive results (zip)", self.archive_results),
            Action("Show archive info", self.show_archive_info)
        ]

    def load_file(self):
        """Load text from a user-specified file."""
        filename = read_str("Enter text file path: ")
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.text = f.read()
            self.input_filename = filename
            print(f"File '{filename}' loaded successfully. {len(self.text)} characters.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def analyze_and_show(self):
        """Perform all analyses and display results on screen."""
        if not self.text:
            print("No text loaded. Please load a file first.")
            return

        self._analysis_results = self._perform_analysis()
        self._print_results()

    def _perform_analysis(self) -> dict:
        """Run all analysis methods and return a dictionary of results."""
        results = {}

        results['total_sentences'] = self.count_sentences()
        results['sentence_types'] = self.classify_sentences()
        results['avg_sentence_len_chars'] = self.average_sentence_length_chars()
        results['avg_word_len'] = self.average_word_length()
        results['smiley_count'] = self.count_smileys()
        results['dates'] = self.extract_dates_year()

        results['words_third_consonant_second_vowel'] = self.get_words_with_conditions()
        results['words_starting_with_vowel_count'] = self.count_words_starting_with_vowel()
        results['words_with_double_letters'] = self.find_words_with_double_letters()
        results['sorted_words'] = self.get_sorted_words_alphabetically()

        return results

    def _print_results(self):
        """Print formatted results to console."""
        r = self._analysis_results
        print("\n" + "="*60)
        print("TEXT ANALYSIS RESULTS")
        print("="*60)

        print(f"\n1. Total sentences: {r['total_sentences']}")
        print("2. Sentence types:")
        print(f"   - Declarative (.) : {r['sentence_types']['declarative']}")
        print(f"   - Interrogative (?) : {r['sentence_types']['interrogative']}")
        print(f"   - Imperative (!) : {r['sentence_types']['imperative']}")
        print(f"3. Average sentence length (characters in words): {r['avg_sentence_len_chars']:.2f}")
        print(f"4. Average word length: {r['avg_word_len']:.2f}")
        print(f"5. Smiley count: {r['smiley_count']}")
        print(f"6. Dates (years): {r['dates'] if r['dates'] else 'None found'}")

        print("\n7. Words where third from end is consonant and second last is vowel:")
        if r['words_third_consonant_second_vowel']:
            print("   " + ", ".join(r['words_third_consonant_second_vowel']))
        else:
            print("   None found")

        print(f"\n8. Number of words starting with a vowel: {r['words_starting_with_vowel_count']}")

        print("\n9. Words containing two identical letters in a row (with indices):")
        if r['words_with_double_letters']:
            for idx, w in r['words_with_double_letters']:
                print(f"   {idx}: {w}")
        else:
            print("   None found")

        print("\n10. Words in alphabetical order:")
        if r['sorted_words']:
            words_to_show = r['sorted_words'][:50]
            print("   " + ", ".join(words_to_show))
            if len(r['sorted_words']) > 50:
                print(f"   ... and {len(r['sorted_words'])-50} more")
        else:
            print("   None")
        print("="*60)

    def save_results_to_file(self):
        """Save analysis results to a text file."""
        if not self._analysis_results:
            print("No analysis results. Run analysis first.")
            return

        filename = f"results_{datetime.now().strftime('%Y%m%d')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("TEXT ANALYSIS REPORT\n")
            f.write(f"Source file: {self.input_filename}\n")
            f.write(f"Date: {datetime.now()}\n\n")
            f.write(f"Total sentences: {self._analysis_results['total_sentences']}\n")
            f.write("Sentence types: "
                    f"declarative={self._analysis_results['sentence_types']['declarative']}, "
                    f"interrogative={self._analysis_results['sentence_types']['interrogative']}, "
                    f"imperative={self._analysis_results['sentence_types']['imperative']}\n")
            f.write(f"Average sentence length (chars): {self._analysis_results['avg_sentence_len_chars']:.2f}\n")
            f.write(f"Average word length: {self._analysis_results['avg_word_len']:.2f}\n")
            f.write(f"Smiley count: {self._analysis_results['smiley_count']}\n")
            f.write(f"Dates (years): {self._analysis_results['dates']}\n")
            f.write(f"Words (third-consonant, second-vowel): {self._analysis_results['words_third_consonant_second_vowel']}\n")
            f.write(f"Words starting with vowel count: {self._analysis_results['words_starting_with_vowel_count']}\n")
            f.write(f"Words with double letters: {self._analysis_results['words_with_double_letters']}\n")
            f.write(f"Alphabetically sorted words: {self._analysis_results['sorted_words']}\n")
        print(f"Results saved to {filename}")

        self.last_results_file = filename
        return filename

    def archive_results(self):
        """Create a zip archive containing the last results file."""
        if not hasattr(self, 'last_results_file') or not os.path.exists(self.last_results_file):
            print("No results file found. Save results first.")
            return

        zip_name = f"results_{datetime.now().strftime('%Y%m%d')}.zip"
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.write(self.last_results_file, arcname=os.path.basename(self.last_results_file))
        print(f"Archive created: {zip_name}")
        self.last_archive = zip_name

    def show_archive_info(self):
        """Display information about the last created archive."""
        if not hasattr(self, 'last_archive') or not os.path.exists(self.last_archive):
            print("No archive found. Create archive first.")
            return

        with zipfile.ZipFile(self.last_archive, 'r') as zf:
            info = zf.infolist()[0]
            print(f"Archive: {self.last_archive}")
            print(f"File in archive: {info.filename}")
            print(f"Original size: {info.file_size} bytes")
            print(f"Compressed size: {info.compress_size} bytes")
            print(f"Compression ratio: {(1 - info.compress_size/info.file_size)*100:.1f}%")