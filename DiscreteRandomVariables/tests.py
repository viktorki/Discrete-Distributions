from django.test import TestCase

class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get("/add_problem/")
        self.assertEqual(resp.status_code, 200)
