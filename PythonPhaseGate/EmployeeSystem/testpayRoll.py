import unittest
import employeeList

class TestAddEmployee(unittest.TestCase):

    def test_addemployee_valid(self):
        expected = {
            'name': 'tega jeremy',
            'hours_worked': 40,
            'hourly_pay': 15,
            'gross_pay': 600,
            'federal_tax': 120,
            'state_tax': 60,
            'total_deductions': 180,
            'net_pay': 420
        }
        result = employeeList.addemployee('Tega jeremy', 40, 15, 0.2, 0.1)
        self.assertEqual(result, expected)


    def test_addemployee_zero_hours(self):
        expected = {
            'name': 'tobi ope',
            'hours_worked': 0,
            'hourly_pay': 20,
            'gross_pay': 0,
            'federal_tax': 0,
            'state_tax': 0,
            'total_deductions': 0,
            'net_pay': 0
        }
        result = employeeList.addemployee('Tobi ope', 0, 20, 0.15, 0.05)
        self.assertEqual(result, expected)


    def test_addemployee_high_tax_rate(self):
        expected = {
            'name': 'mr evans',
            'hours_worked': 50,
            'hourly_pay': 30,
            'gross_pay': 1500,
            'federal_tax': 750,
            'state_tax': 750,
            'total_deductions': 1500,
            'net_pay': 0
        }
        result = employeeList.addemployee('Mr evans', 50, 30, 0.5, 0.5)
        self.assertEqual(result, expected)

    # def test_view__employee(self):
    #     expected = [{'federal_tax': 16200.0,
    #                     'gross_pay': 600.0,
    #                     'hourly_pay': 30.0,
    #                     'hours_worked': 20,
    #                     'name': 'tega',
    #                     'net_pay': -37800.0,
    #                     'state_tax': 22200.0,
    #                     'total_deductions': 38400.0}]
    #     actual = employeeList.view_employee_list()
    #     self.assertEqual(expected, actual)






