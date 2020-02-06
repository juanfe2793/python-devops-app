#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'This is the app index')

    def test_add(self):
        rv = self.app.get('/add?name=testuser&money=100')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'"Client added with id={}".format(client.id)')

if __name__ == '__main__':
    unittest.main()