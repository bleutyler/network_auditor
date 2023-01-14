import unittest
import ipaddress
from network_discovery.navigator import navigator

class TestNavigator(unittest.TestCase):
    def test_calculate_endpoints_to_investigate(self):
        default_list_of_ips = navigator.calculate_endpoints_to_investigate()
        self.assertIsNotNone(default_list_of_ips, "Default List of IPs is not empty")
        self.assertIsInstance(default_list_of_ips, list, "Return Object is a List")
        self.assertGreater(len(default_list_of_ips), 0, "Return List is greater than zero")
        self.assertEqual(len(default_list_of_ips), 255, "Return List is 255 elements")
        first_element = str(default_list_of_ips[0])
        last_element = str(default_list_of_ips[254])
        try:
            test_first_is_valid_ip = ipaddress.ip_address(first_element)
            test_last_is_valid_ip = ipaddress.ip_address(last_element)
        except ValueError:
            self.assertTrue(False, "Elements in array are valid IPv4 addresses")
        self.assertEqual(first_element[first_element.rfind('.'):], ".0",
                         "First element in List is .0")
        self.assertEqual(last_element[last_element.rfind('.'):], ".254",
                         "Last element in List is .254")


if __name__ == '__main__':
    unittest.main()
