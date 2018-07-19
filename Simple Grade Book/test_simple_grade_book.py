import unittest
from simple_grade_book import gradebook
from simple_grade_book import add_student, add_grade
from simple_grade_book import get_grade, letter_grade
from simple_grade_book import grade_average, class_average


class TestGrades(unittest.TestCase):
    def setUp(self):
        add_student("Jean Roy")
        add_student("Liverpool")
        add_student("JoJo")
        add_grade("Jean Roy", 86)
        add_grade("Jean Roy", 55)
        add_grade("Liverpool", 100)
        add_grade("Liverpool", 84)


    def test_not_enrolled(self):
        x = add_grade("Lise Dion", 55)
        self.assertEqual(x, "'Lise Dion' not enrolled")

    def test_grades(self):
        self.assertEqual(gradebook, {"Jean Roy": [86, 55],
                         "JoJo": [], "Liverpool": [100, 84]})

    def test_average(self):
        self.assertEqual(letter_grade(grade_average(gradebook.get("Jean Roy"))), "C")

    def test_get_grade(self):
        self.assertEqual(get_grade("Jean Roy"), [86, 55])

    def test_class_average(self):
        add_grade("JoJo", 0)
        self.assertEqual(letter_grade(class_average(gradebook.values())), "F")

    def test_class_average_exception(self):
        with self.assertRaises(ZeroDivisionError):
            letter_grade(class_average(gradebook.values()))



if __name__ == '__main__':
    unittest.main()