import pytest
from unittest.mock import patch
from io import StringIO
from tkinter import Tk
from show import get_ip_info, update_details, get_ip_info_wrapper

@pytest.fixture
def root():
    root = Tk()
    yield root
    root.destroy()


def test_get_ip_info_valid_ip():
    ip_address = "8.8.8.8"  # A sample valid IP address
    details_data = {
        "ip": "8.8.8.8",
        "city": "Mountain View",
        "region": "California",
        "country": "US"
    }
    with patch("sys.stdout", new=StringIO()) as fake_out:
        get_ip_info(ip_address)
        output = fake_out.getvalue().strip()
        assert output == "IPv4: 8.8.8.8\nip: 8.8.8.8\ncity: Mountain View\nregion: California\ncountry: US"


def test_get_ip_info_invalid_ip():
    ip_address = "invalid_ip_address"
    with patch("sys.stdout", new=StringIO()) as fake_out:
        get_ip_info(ip_address)
        output = fake_out.getvalue().strip()
        assert output == "IPv4: invalid_ip_address\nerror: Error fetching details"


def test_update_details():
    details_data = {
        "ip": "8.8.8.8",
        "city": "Mountain View",
        "region": "California",
        "country": "US"
    }
    expected_output = "ip: 8.8.8.8\ncity: Mountain View\nregion: California\ncountry: US"
    with patch("tkinter.Text") as mock_text:
        update_details(details_data)
        mock_text.delete.assert_called_once_with('1.0', 'end')
        mock_text.insert.assert_called_once_with('end', expected_output)


@patch("your_module_name.ip_entry.get")
@patch("your_module_name.ip_v4_label.config")
def test_get_ip_info_wrapper(mock_config, mock_get):
    mock_get.return_value = "8.8.8.8"
    get_ip_info_wrapper()
    mock_config.assert_called_once_with(text="IPv4: 8.8.8.8")

    # Test with empty input
    mock_get.return_value = ""
    get_ip_info_wrapper()
    mock_config.assert_called_with(text="IPv4: ")

    # Test with None input
    mock_get.return_value = None
    get_ip_info_wrapper()
    mock_config.assert_called_with(text="IPv4: ")

    # Additional test cases for other scenarios can be added


if __name__ == "__main__":
    pytest.main()
