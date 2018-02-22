import sys

from haveibeenpwnd import HIBP
from tests.resources import no_match_response
from tests.resources import match_response

if sys.version_info.major == 3:
    from unittest import mock
else:
    import mock


@mock.patch('haveibeenpwnd.main.requests')
def test_no_match(mock_requests):
    mock_requests.get.return_value.text = no_match_response

    count = HIBP.check_password('super_safe_password')

    assert count == 0


@mock.patch('haveibeenpwnd.main.requests')
def test_match(mock_requests):
    mock_requests.get.return_value.text = match_response

    count = HIBP.check_password('hunter2')

    assert count == 16092
