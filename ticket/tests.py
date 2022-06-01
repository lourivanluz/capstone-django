from django.test import TestCase

class TicketTest(testCase):
    def test_str(self):
        test_name = Ticket(name='An Issue')
        self.assertEqual(str(test_name), 'An Issue')
