from unittest.mock import patch

from django.test import SimpleTestCase
from django.urls import reverse

from .quotes import random_quote


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