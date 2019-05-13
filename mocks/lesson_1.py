from io import StringIO
import unittest
from unittest import TestCase, mock

from work import work_on, Helper, Worker, size_of, Pricer


class TestWorkMockingModule(TestCase):
    def test_using_context_manager(self):
        with mock.patch('work.os.getcwd', return_value='testing') as mocked_os:
            assert work_on() == 'testing'


class TestWorkerModule(TestCase):

    def test_patching_class(self):
        with mock.patch('work.Helper', autospec=True) as MockHelper:
            MockHelper.return_value.get_path.return_value = 'testing'
            worker = Worker()
            MockHelper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')
            
    def test_pathching_context_managers(self):
        with mock.patch('work.open') as mock_open:
            mock_open.return_value.__enter__.return_value = StringIO('testing')
            self.assertEqual(size_of(), 7)

    # Technology for mocking class attributes
    def test_patch_incorrect_class_attribute(self):
        with mock.patch.object(Pricer, 'PERCENTAGE', 1):
            pricer = Pricer()
            self.assertEqual(pricer.get_discounted_price(100), 100)

    def test_patch_class_attribute(self):
        with mock.patch.object(Pricer, 'DISCOUNT', 1):
            pricer = Pricer()
            self.assertEqual(pricer.get_discounted_price(100), 100)
        self.assertAlmostEqual(pricer.get_discounted_price(100), 80)

    # Mocking class Helpers
    def test_delayed_import(self):
        with mock.patch('work.COUNTRIES', ['GB']):
            from work import CountryPricer
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discount_price(100, 'GB'), 80)

        pricer = CountryPricer()
        self.assertAlmostEqual(pricer.get_discount_price(100, "GB"), 100)


unittest.main()
