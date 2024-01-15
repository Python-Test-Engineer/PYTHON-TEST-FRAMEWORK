import unittest
from unittest.mock import patch

from real_python_patch import get_holidays
from requests.exceptions import Timeout


class TestCalendar(unittest.TestCase):
    @patch("real_python_patch.requests")
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()
            mock_requests.get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
