import unittest
from mock import patch, Mock
from . import tools
from .tools import (
    parse,
    prettify_time,
    full_example_dict,
    flatten_dict,
    parse_periods,
    prettify_periods,
    stringify_parsed_json
)

FIXTURE_FLAT_DICT = [
    {'type': 'open', 'value': 36000, 'day': 'tuesday'},
    {'type': 'close', 'value': 64800, 'day': 'tuesday'},
    {'type': 'open', 'value': 36000, 'day': 'wednesday'},
    {'type': 'close', 'value': 64800, 'day': 'wednesday'}
]
FIXTURE_JSON = {
    "tuesday": [
        {
            "type": "open",
            "value": 36000
        },
        {
            "type": "close",
            "value": 64800
        }
    ],
    "wednesday": [
        {
            "type": "open",
            "value": 36000
        },
        {
            "type": "close",
            "value": 64800
        }],
}

PARSED_PERIODS_FIXTURE = [
    (
        {'type': 'open', 'value': 36000, 'day': 'tuesday'},
        {'type': 'close', 'value': 64800, 'day': 'tuesday'},
    ), (
        {'type': 'open', 'value': 36000, 'day': 'wednesday'},
        {'type': 'close', 'value': 64800, 'day': 'wednesday'}
    )
]

PRETTIFIED_DICT = {
    'friday': 'Closed',
    'monday': 'Closed',
    'saturday': 'Closed',
    'sunday': 'Closed',
    'thursday': 'Closed',
    'tuesday': '10 AM - 6 PM',
    'wednesday': '10 AM - 6 PM'
}

STRINGIFIED_OUTPUT = """A resturant is open:
Friday: Closed
Monday: Closed
Saturday: Closed
Sunday: Closed
Thursday: Closed
Tuesday: 10 AM - 6 PM
Wednesday: 10 AM - 6 PM
"""


class TestParse(unittest.TestCase):
    def test_prettify_time(self):
        self.assertEqual(prettify_time(36000), '10 AM')

    def test_flatten_dict(self):
        self.assertEqual(flatten_dict(FIXTURE_JSON), FIXTURE_FLAT_DICT)

    def test_parse_periods(self):
        self.assertEqual(
            parse_periods(FIXTURE_FLAT_DICT),
            PARSED_PERIODS_FIXTURE
        )

    def test_prettify_periods(self):
        self.assertEqual(
            prettify_periods(PARSED_PERIODS_FIXTURE),
            PRETTIFIED_DICT
        )

    @patch.object(tools, 'flatten_dict')
    @patch.object(tools, 'parse_periods')
    @patch.object(tools, 'prettify_periods')
    def test_parse(self, mock_flatten, mock_parse_periods, mock_prettify):
        parse({})
        mock_flatten.assert_called_once()
        mock_parse_periods.assert_called_once()
        mock_prettify.assert_called_once()

    def test_stringify_parsed_json(self):
        string_output = stringify_parsed_json(PRETTIFIED_DICT)
        self.assertEqual(
            string_output, STRINGIFIED_OUTPUT
        )


if __name__ == '__main__':
    unittest.main()
