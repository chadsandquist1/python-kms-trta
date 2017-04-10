import unittest
import kms

class TestKMS(unittest.TestCase):

    def test__get_key_by_alias(self):
        kms.get_key_by_alias('testing-alias-for-e017398b-ba0b-4bfa-b4bc-14a89fd29214')

    def test__list_aliases(self):
        kms.list_aliases()

    def test__list_keys(self):
        kms.list_keys()

    def test_create_keys(self):
        print('ignore')

if __name__ == '__main__':
    unittest.main()