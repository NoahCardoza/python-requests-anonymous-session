import unittest
from python_requests_anonymous_session import AnonymosSession


class TestRandomUserAgent(unittest.TestCase):
    def setUp(self):
        self.session = AnonymosSession()

    def tearDown(self):
        self.session.close()

    def test_user_agent_is_not_default(self):
        self.assertNotIn(
            "python-requests",
            self.session.headers['User-Agent']
        )

    def test_user_agent_is_random(self):
        # TODO(dw): This could occasionally fail
        self.assertNotEqual(
            self.session.headers['User-Agent'],
            AnonymosSession().headers['User-Agent']
        )

    def test_request(self):
        resp = self.session.get('https://httpbin.org/user-agent')

        self.assertEqual(resp.status_code, 200)
        user_agent = resp.json()['user-agent']

        self.assertEqual(
            self.session.headers['User-Agent'],
            user_agent
        )

        self.assertNotIn(
            "python-requests",
            user_agent
        )

    def test_request_session(self):
        resp = self.session.get('https://httpbin.org/user-agent')

        self.assertEqual(resp.status_code, 200)
        user_agent = resp.json()['user-agent']

        self.assertNotIn(
            "python-requests",
            user_agent
        )

    def test_request_session_keeps_user_agent(self):
        # TODO(dw): This could occasionally fail
        resp = self.session.get('https://httpbin.org/user-agent')
        self.assertEqual(resp.status_code, 200)
        first_user_agent = resp.json()['user-agent']

        resp = self.session.get('https://httpbin.org/user-agent')
        self.assertEqual(resp.status_code, 200)
        second_user_agent = resp.json()['user-agent']

        self.assertEqual(
            first_user_agent,
            second_user_agent
        )
