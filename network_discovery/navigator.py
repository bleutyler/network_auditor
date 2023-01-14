from socket import gethostname, gethostbyname


class navigator:
    '''The simple scanner that just tries to find out what is listening out there'''

    def find_alive_ips(self):
        pass

    @staticmethod
    def calculate_endpoints_to_investigate():
        '''Default behaviour: return a list of the /24 of whatever IP we are on'''
        return_list = []
        base_ip_address = str(gethostbyname(gethostname()))
        three_bytes = base_ip_address[:base_ip_address.rindex('.')]
        return [three_bytes + '.' + str(octet) for octet in range(0, 255)]
