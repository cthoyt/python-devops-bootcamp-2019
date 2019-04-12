import contextlib
import unittest
from io import StringIO

import booty.utils


class TestBooty(unittest.TestCase):
    """Test the booty!"""

    def test_head(self):
        """Test the ``head`` function of the booty."""

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            booty.utils.head()

        output = temp_stdout.getvalue().strip()
        self.assertIsInstance(output, str)
