import unittest
from django.test import TestCase
from django.test.client import Client
from ..env_conversion import bool_env, int_env, filter_list_to_tuple

TEST_TRUE_LIST = [1, "1", "true", "True", "TRUE", "YES", "Yes", "yes", True]
TEST_FALSE_LIST = [0, "0", "False", "FALSE", "false", "NO", "No", "no", False]
BAD_VALUES = [2, 10, 100, ("tuple", "tuple_value"), [1, "bad", "list"], 99.999]


class ConversionTests(unittest.TestCase):
    def test_bool_true(self):
        """ Test for True Values """
        for t in TEST_TRUE_LIST:
            self.assertEqual(bool_env(t), True)


    def test_bool_false(self):
        """ test for False values """
        for f in TEST_FALSE_LIST:
            self.assertEqual(bool_env(f), False)

    def test_bool_bad(self):
        """ test for bad values returning same value and value is a bool """
        for b in BAD_VALUES:

            # Does bool_env return the value it received
            self.assertEqual(bool_env(b), False)

    def test_bool_null(self):
        """ Test for a null value passed to bool_env() """
        self.assertEqual(bool_env(), False)

    def test_integer_good(self):
        """ Test for good string numbers to integers """
        GOOD_INTEGERS = [(0, 0), (1, 1), (99, 99),
                         (9999, 9999), (1.5, 1), (2.345678, 2),
                         (3.7, 3), ("88", 88), ("9.999", 9),
                         ("1001", 1001)]
        for i in GOOD_INTEGERS:
            self.assertEqual(int_env(i[0]), i[1])

    def test_integer_bad(self):
        """ Test for bad strings that don't convert to integers """
        BAD_INTEGERS = ["bad", "one", "two", "1,000"]
        for b in BAD_INTEGERS:
            print("B is %s" % b)
            self.assertEqual(isinstance(int_env(b), type("int")), False)

    def test_tuple_good(self):
        """ Test for a good tuple selection """
        GOOD_TUPLES = [("PATIENT_ID_FHIR SSN MEDICARE_ID MEDICARE_HICN", [
    ('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
    ('MPI', 'Master Patient Index (Not FHIR Patient ID)'),
    ('SSN', 'Social Security Number'),
    ('MEDICAID_ID', 'Medicaid ID Number'),
    ('MEDICARE_HICN', 'Medicare HICN (Legacy)'),
    ('MEDICARE_ID', 'Medicare ID Number'),
    ('INSURANCE_ID', 'Insurance ID Number'),
    ('IHE_ID', 'Health Information Exchange ID'),
    ('NPI', 'National Provider Identifier'),
    ('UHI', 'Universal Health Identifier')],
                        (('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
                        ('SSN', 'Social Security Number'),
                        ('MEDICARE_ID', 'Medicare ID Number'),
                        ('MEDICARE_HICN', 'Medicare HICN (Legacy)')
                        )
                        )]

        for g in GOOD_TUPLES:
            print("Selecting: %s" % g[0])
            self.assertEqual(filter_list_to_tuple(g[0], g[1],), g[2])

    def test_tuple_with_added_blank(self):
        """ Test for a tuple with an added blank entry """
        selector = 'PATIENT_ID_FHIR SSN MEDICARE_ID MEDICARE_HICN'
        source = [('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
                  ('MPI', 'Master Patient Index (Not FHIR Patient ID)'),
                  ('SSN', 'Social Security Number'),
                  ('MEDICAID_ID', 'Medicaid ID Number'),
                  ('MEDICARE_HICN', 'Medicare HICN (Legacy)'),
                  ('MEDICARE_ID', 'Medicare ID Number'),
                  ('INSURANCE_ID', 'Insurance ID Number'),
                  ('IHE_ID', 'Health Information Exchange ID'),
                  ('NPI', 'National Provider Identifier'),
                  ('UHI', 'Universal Health Identifier')]

        result = [('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
                  ('SSN', 'Social Security Number'),
                  ('MEDICARE_ID', 'Medicare ID Number'),
                  ('MEDICARE_HICN', 'Medicare HICN (Legacy)'),
                  ('', 'nothing to see here')]
        add_blank = ('', 'nothing to see here')

        print("\nWe should be adding: %s" % (add_blank,))
        print(filter_list_to_tuple(selector, source, add_blank))
        print("\nresult:", tuple(result))
        self.assertEqual(filter_list_to_tuple(selector, source, add_blank), tuple(result))

    def test_tuple_is_empty(self):
        """ Empty tuple returns default list as tuple """
        selector = ""
        source = [('PATIENT_ID_FHIR', 'Patient ID in FHIR'),
                  ('MPI', 'Master Patient Index (Not FHIR Patient ID)'),
                  ('SSN', 'Social Security Number'),
                  ('MEDICAID_ID', 'Medicaid ID Number'),
                  ('MEDICARE_HICN', 'Medicare HICN (Legacy)'),
                  ('MEDICARE_ID', 'Medicare ID Number'),
                  ('INSURANCE_ID', 'Insurance ID Number'),
                  ('IHE_ID', 'Health Information Exchange ID'),
                  ('NPI', 'National Provider Identifier'),
                  ('UHI', 'Universal Health Identifier')]

        print("\nExpected Result is default tuple: %s" % (tuple(source),))
        self.assertEqual(filter_list_to_tuple(selector, source,), tuple(source))

if __name__ == '__main__':
    unittest.main()
