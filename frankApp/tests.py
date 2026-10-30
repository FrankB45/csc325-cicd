from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse

from .quotes import random_quote

from .numbers import generate_random_number

class QuoteFunctionTests(SimpleTestCase):
    def test_returns_nonempty_string(self):
        # Act: call the real function.
        quote = random_quote()

        # Assert: check the result's type and content.
        self.assertIsInstance(quote, str)
        self.assertTrue(quote.strip())

    def test_returns_selected_quote(self):
        # Arrange: control what random.choice returns.
        expected = "When in doubt, use brute force. - Ken Thompson"

        with patch(
            "frankApp.quotes.random.choice",
            return_value=expected,
        ) as mock_choice:
            # Act
            actual = random_quote()

        # Assert
        self.assertEqual(actual, expected)
        mock_choice.assert_called_once()


class QuoteAPITests(SimpleTestCase):
    def setUp(self):
        # Runs before each test in this class.
        self.url = reverse("get-random-quote")

    def test_get_returns_quote_json(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        data = response.json()

        self.assertEqual(set(data.keys()), {"quote"})
        self.assertIsInstance(data["quote"], str)
        self.assertTrue(data["quote"].strip())

    def test_response_contains_selected_quote(self):
        expected = "A predictable test quote."

        with patch(
            "frankApp.views.random_quote",
            return_value=expected,
        ):
            response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"quote": expected})

    def test_post_is_not_allowed(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 405)

class NumberFunctionTests(SimpleTestCase):
    def test_returns_integer_in_range(self):
        number = generate_random_number()

        self.assertIs(type(number), int)
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual(number, 99)

    def test_range_boundaries(self):
        # Force selection of each bound passed to randint().
        cases = [
            ("lower bound", lambda low, high: low, 0),
            ("upper bound", lambda low, high: high, 99),
        ]

        for label, select_bound, expected in cases:
            with self.subTest(boundary=label):
                with patch(
                    "frankApp.numbers.random.randint",
                    side_effect=select_bound,
                ):
                    number = generate_random_number()

                self.assertEqual(number, expected)


class NumberAPITests(SimpleTestCase):
    def setUp(self):
        self.url = reverse("get-random-number")

    def test_get_returns_number_json(self):
        # Exercise the real endpoint and number generator.
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        data = response.json()

        self.assertEqual(set(data.keys()), {"number"})
        self.assertIs(type(data["number"]), int)
        self.assertGreaterEqual(data["number"], 0)
        self.assertLessEqual(data["number"], 99)

    def test_response_preserves_generated_number(self):
        # Check zero, a middle value, and the highest allowed value.
        for expected in [0, 42, 99]:
            with self.subTest(number=expected):
                with patch(
                    "frankApp.views.generate_random_number",
                    return_value=expected,
                ):
                    response = self.client.get(self.url)

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json(), {"number": expected})

    def test_write_methods_are_not_allowed(self):
        for method in ["POST", "PUT", "PATCH", "DELETE"]:
            with self.subTest(method=method):
                response = self.client.generic(
                    method,
                    self.url,
                    data="{}",
                    content_type="application/json",
                )

                self.assertEqual(response.status_code, 405)