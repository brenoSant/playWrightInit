import unittest


class MytestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(2, 2)

    def test_assert_true(self):
        try:
            self.assertTrue(False)
        except Exception as ex:
            print(ex)

    def test_something2(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
