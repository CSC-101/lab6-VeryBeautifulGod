from data import Book
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books_case_1(self):
        books = [
            Book(["Author A"], "Zebra"),
            Book(["Author B"], "Apple"),
            Book(["Author C"], "Mango"),
            Book(["Author D"], "Banana")
        ]
        expected = [
            Book(["Author B"], "Apple"),
            Book(["Author D"], "Banana"),
            Book(["Author C"], "Mango"),
            Book(["Author A"], "Zebra")
        ]
        lab6.selection_sort_books(books)
        self.assertEqual(books, expected)

    def test_selection_sort_books_case_2(self):
        books = [
            Book(["Author A"], "C"),
            Book(["Author B"], "B"),
            Book(["Author C"], "A")
        ]
        expected = [
            Book(["Author C"], "A"),
            Book(["Author B"], "B"),
            Book(["Author A"], "C")
        ]
        lab6.selection_sort_books(books)
        self.assertEqual(books, expected)

    # Part 2
    def test_swap_case_1(self):
        input_str = "Hello World!"
        expected = "hELLO wORLD!"
        actual = lab6.swap_case(input_str)
        self.assertEqual(expected, actual)

    def test_swap_case_2(self):
        input_str = "Python 3.8 is Fun!"
        expected = "pYTHON 3.8 IS fUN!"
        actual = lab6.swap_case(input_str)
        self.assertEqual(expected, actual)

    # Part 3
    def test_str_translate_1(self):
        input_str = 'abcdcba'
        old_char = 'a'
        new_char = 'x'
        expected = 'xbcdcbx'
        actual = lab6.str_translate(input_str, old_char, new_char)
        self.assertEqual(expected, actual)

    def test_str_translate_2(self):
        input_str = 'hello world'
        old_char = 'o'
        new_char = '0'
        expected = 'hell0 w0rld'
        actual = lab6.str_translate(input_str, old_char, new_char)
        self.assertEqual(expected, actual)

    # Part 4
    def test_histogram_1(self):
        input_str = "hello world hello"
        expected = {'hello': 2, 'world': 1}
        actual = lab6.histogram(input_str)
        self.assertEqual(expected, actual)

    def test_histogram_2(self):
        input_str = "this is a test this is only a test"
        expected = {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
        actual = lab6.histogram(input_str)
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
