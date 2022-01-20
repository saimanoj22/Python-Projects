# Unit Tests and Test Cases
'''The module unittest from the Python standard library provides tools for testing your code. 
A unit test verifies that one specific aspect of a function's behavior is correct. A test case 
is a collection of unit tests that together prove that a function behaves as it's supposed to'''

# A Passing Test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()

# A Failing Test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')  # but here get_formatted_name() have three arguments, the other is middle name
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()


# Testing a Class
# A Variety of Assert Methods
'''
    Method                              Use
assertEqual(a, b)               Verify that a == b
assertNotEqual(a, b)            Verify that a != b
assertTrue(x)                   Verify that x is True
assertFalse(x)                  Verify that x is False
assertIn(item, list)            Verify that item is in list
assertNotIn(item, list)         Verify that item is not in list
'''

# A Class to Test
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    def show_question(self):
        """Show the survey question."""
        print(self.question)
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)
    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

    # another file to test above class
from survey import AnonymousSurvey
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()