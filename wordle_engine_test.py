
#######################################################
# wordle_engine_tests 
#
# Name: zzNAMEzz (replace with your name)
# Section: XX
#
# Fall 2023
#########################################################

import unittest
import wordle_engine

class wc:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class WordleEngineTest(unittest.TestCase):

#
# create_letter_status
#

    # This is the only test you need for this function
    def test_create_letter_status_01(self):
        observed = wordle_engine.create_letter_status()
        for l in "abcdefghijklmnopqrstuvwxyz":
            self.assertEqual(wc.BLUE, observed[l])

#
# load_words
# 
    def test_load_words_01(self):
        observed = wordle_engine.load_words("sample_word_list.txt")
        expected = {"dog", "cat", "turkey", "sheep", "goat"}
        self.assertEqual(expected, observed)

    # Create one more test case that loads a different, short file.

#
# format_guess
#
    def test_format_guess_00(self):
        # make sure string ends with ENDC
        observed = wordle_engine.format_guess('abcde', 'fghij')
        self.assertTrue(observed.endswith(wc.ENDC), "formatted guess should end with the ENDC special character.")

    def test_format_guess_01(self):
        # no matching letters
        observed = wordle_engine.format_guess('abcde', 'fghij')
        expected = f"{wc.RED}f{wc.RED}g{wc.RED}h{wc.RED}i{wc.RED}j{wc.ENDC}"
        self.assertEqual(expected, observed)

    # Write several more test cases to make sure different color combinations are handled correctly.
    # Don't forget about double letters.

    #     

#
# update_letter_status
#

    def test_update_letter_status_01(self):
        observed_letter_status = wordle_engine.create_letter_status()
        wordle_engine.update_letter_status(observed_letter_status, 'abcde', 'abdcf')
        self.assertEqual(wc.GREEN, observed_letter_status["a"]) 
        self.assertEqual(wc.GREEN, observed_letter_status["b"]) 
        self.assertEqual(wc.YELLOW, observed_letter_status["c"]) 
        self.assertEqual(wc.YELLOW, observed_letter_status["d"]) 
        self.assertEqual(wc.BLUE, observed_letter_status["e"]) 
        self.assertEqual(wc.RED, observed_letter_status["f"]) 

        for l in "ghijklmnopqrstuvwxyz":
            self.assertEqual(wc.BLUE, observed_letter_status[l]) 

    # Write several more test cases to make sure different color combinations are handled correctly.
    # Don't forget about double letters.

    #    

#
# format_letters
#

    # These are the only tests you need for this function

    def test_format_letters_00(self):
        # Make sure string ends with ENDC
        letter_status = wordle_engine.create_letter_status()
        observed = wordle_engine.format_letters(letter_status)
        self.assertTrue(observed.endswith(wc.ENDC), 
                        "formatted letters should end with the ENDC special character.")

    def test_format_letters_01(self):
        letter_status = wordle_engine.create_letter_status()
        letter_status["b"] = wc.GREEN
        letter_status["f"] = wc.RED
        letter_status["q"] = wc.YELLOW

        expected = [] 
        for l in "abcdefghijklmnopqrstuvwxyz":    
            if l == "b":
                expected.append(f"{wc.GREEN}b")
            elif l == "f":
                expected.append(f"{wc.RED}f")
            elif l == "q":
                expected.append(f"{wc.YELLOW}q")
            else:
                expected.append(f"{wc.BLUE}{l}")

        expected.append(wc.ENDC)
        self.assertEqual("".join(expected), wordle_engine.format_letters(letter_status) )

# This bit of "magic" lets you run the tests from the command line by 
# running "python wordle_engine_test.py"
if __name__ == '__main__':
    unittest.main()