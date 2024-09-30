import unittest
import socket
import threading
import time
from _5solutions._1completion.exercise3_tcp_server import start_server

class TestTCPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server in a separate thread
        cls.server_thread = threading.Thread(target=start_server, args=(9999,))
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(5)  # Wait a moment for the server to start

    def test_echo(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9999))
        test_message = b'Hello, Server!'
        client_socket.sendall(test_message)
        response = client_socket.recv(1024)
        client_socket.close()
        self.assertEqual(response, test_message)

if __name__ == '__main__':
    unittest.main()
