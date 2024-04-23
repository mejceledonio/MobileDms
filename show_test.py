import pytest
from unittest.mock import patch, MagicMock

# Import functions to be tested
from show import (
    get_current_ip, change_ip, get_ipv6_address, change_ipv6_address,
    get_connected_devices, get_ip_info_wrapper, update_details
)

# Mocking tkinter and requests modules
@patch('show.tk')
@patch('show.requests')
def test_get_current_ip(mock_requests, mock_tk):
    # Mock the response from socket.gethostname() and socket.gethostbyname()
    mock_tk.Label = MagicMock()
    socket_mock = MagicMock()
    socket_mock.gethostname.return_value = 'test_host'
    socket_mock.gethostbyname.return_value = '192.168.1.1'
    with patch('show.socket', socket_mock):
        # Call the function
        get_current_ip()
        # Assert that the label's text was set correctly
        mock_tk.Label.assert_called_with(text='Current IPv4 address: 192.168.1.1 (Hostname: test_host)')

@patch('show.tk')
@patch('show.simpledialog')
def test_change_ip(mock_simpledialog, mock_tk):
    # Mock the response from simpledialog.askstring()
    mock_simpledialog.askstring.return_value = 'new_ip_address'
    mock_tk.Label = MagicMock()
    # Call the function
    change_ip()
    # Assert that the label's text was set correctly
    mock_tk.Label.assert_called_with(text='New IPv4 address: new_ip_address')

@patch('show.tk')
def test_get_ipv6_address(mock_tk):
    # Mock the response from socket.gethostname() and socket.getaddrinfo()
    mock_tk.Label = MagicMock()
    socket_mock = MagicMock()
    socket_mock.gethostname.return_value = 'test_host'
    socket_mock.getaddrinfo.return_value = [(None, None, None, None, ('ipv6_address',))]
    with patch('show.socket', socket_mock):
        # Call the function
        get_ipv6_address()
        # Assert that the label's text was set correctly
        mock_tk.Label.assert_called_with(text='Current IPv6 address: ipv6_address (Hostname: test_host)')

# Write similar test functions for change_ipv6_address, get_connected_devices, get_ip_info_wrapper, and update_details
