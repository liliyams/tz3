import unittest
import tz3
import math
import time
import sys


class TestMax(unittest.TestCase):
    data_for_test = list(range(0, 10 ** 7))

    def test_min(self):
        try:
            self.assertEqual(min(self.data_for_test), tz3.min_number(self.data_for_test))
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_min')
            f.close()

    def test_max(self):
        try:
            self.assertEqual(max(self.data_for_test), tz3.max_number(self.data_for_test))
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_max')
            f.close()

    def test_sum_of_numbers(self):
        try:
            self.assertEqual(sum(self.data_for_test), tz3.sum_of_numbers(self.data_for_test))
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_sum_of_numbers')
            f.close()

    def test_product_of_numbers(self):
        try:
            self.assertEqual(math.prod(self.data_for_test), tz3.product_of_numbers(self.data_for_test))
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_product_of_numbers')
            f.close()

    def test_time(self):
        try:
            test_data = self.data_for_test[:100000]
            start_time = time.time()
            tz3.min_number(test_data)
            tz3.max_number(test_data)
            tz3.sum_of_numbers(test_data)
            tz3.product_of_numbers(test_data)
            end_time = time.time()
            first_time = end_time - start_time
            new_data_for_test = test_data * 100
            start_time = time.time()
            tz3.min_number(new_data_for_test)
            tz3.max_number(new_data_for_test)
            tz3.sum_of_numbers(new_data_for_test)
            tz3.product_of_numbers(new_data_for_test)
            end_time = time.time()
            second_time = end_time - start_time
            if first_time == 0:
                first_time = 0.00001
            result = second_time / first_time <= 150
            self.assertTrue(result)
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_time')
            f.close()

    # тест на выбор
    def test_split(self):
        try:
            s = ' '.join(map(str, self.data_for_test))
            self.assertEqual(tz3.convert(s), self.data_for_test)
        except AssertionError as error:
            f = open("bot.txt", 'a')
            f.write(str(error) + ' ' + 'test_split')
            f.close()


