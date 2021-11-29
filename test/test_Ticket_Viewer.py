
import requests
import unittest
from unittest.mock import patch
from assertpy.assertpy import assert_that

from src.Ticket_Viewer import get_tickets

'''
    Testing the same techniques used in Ticket_Viewer on a 'fake' api
'''

class test_TicketViewer(unittest.TestCase):

    requests = requests.get('https://jsonplaceholder.typicode.com/posts')

    @patch('TicketViewer.requests.get')
    # send a request to a fake api and make sure that the call is successful, and that the data retrieved is accurate
    def test_request_response(self, mock_get):
        data = requests.json()
        user_id = [id['userid'] for id in data]

        mock_get.return_value.status_code = 200
        response = get_tickets()

        self.assertEqual(response.status_code, 200) # making sure that the api request is successful 

        assert_that(user_id).contains('1') # making sure that we can access the first element within placeholder.json

    if __name__ == '__main__':
        unittest.main()
