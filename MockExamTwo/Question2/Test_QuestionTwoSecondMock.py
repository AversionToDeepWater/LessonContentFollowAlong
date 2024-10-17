from unittest import TestCase
from MockExamTwo.Question2.QuestionTwoSecondMock import total_revenue
items_info = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7,
    "grape": 1.2
}

sales_info = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 12
}

empty1 = {}
empty2 = {}

missing_key1 = {
    "apple": 5,
    "orange": 3
}
missing_key2 = {
    "apple": 5
}

class TestCheckTotalRevenue(TestCase):
    def test_correct_revenue(self):
        result = total_revenue(items_info,sales_info)
        self.assertEqual(result, 26.5)

    def test_empty_dict(self):
        result = total_revenue(empty1, empty2)
        self.assertEqual(result, 0)

    def test_edge_case(self):
        result = total_revenue(missing_key1, missing_key2)
        self.assertEqual(result, 25)



