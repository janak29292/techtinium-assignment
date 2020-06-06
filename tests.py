import unittest, resource

class Test(unittest.TestCase):

    def test_one(self):
        input_val = 'Capacity of 50 units for 1 Hour'
        output = resource.main(input_val)
        ny = list(filter(lambda x: x['region'] == 'New York', output['Output']))[0]
        india = list(filter(lambda x: x['region'] == 'India', output['Output']))[0]
        china = list(filter(lambda x: x['region'] == 'China', output['Output']))[0]
        self.assertEqual(ny['total_cost'], 570)
        self.assertEqual(ny['machines'], [('2XLarge', 1), ('Large', 1)])
        self.assertEqual(india['total_cost'], 553)
        self.assertEqual(india['machines'], [('2XLarge', 1), ('Large', 1)])
        self.assertEqual(china['total_cost'], 510)
        self.assertEqual(china['machines'], [('XLarge', 2), ('Large', 1)])

    def test_two(self):
        input_val = 'Capacity of 1150 units for 1 Hour'
        output = resource.main(input_val)
        ny = list(filter(lambda x: x['region'] == 'New York', output['Output']))[0]
        india = list(filter(lambda x: x['region'] == 'India', output['Output']))[0]
        china = list(filter(lambda x: x['region'] == 'China', output['Output']))[0]
        self.assertEqual(ny['total_cost'], 10150)
        self.assertEqual(ny['machines'], [('8XLarge', 7), ('XLarge', 1), ('Large', 1)])
        self.assertEqual(india['total_cost'], 9520)
        self.assertEqual(india['machines'], [('8XLarge', 7), ('Large', 3)])
        self.assertEqual(china['total_cost'], 8570)
        self.assertEqual(china['machines'], [('8XLarge', 7), ('XLarge', 1), ('Large', 1)])

    def test_three(self):
        input_val = '230 units for 5 Hours'
        output = resource.main(input_val)
        ny = list(filter(lambda x: x['region'] == 'New York', output['Output']))[0]
        india = list(filter(lambda x: x['region'] == 'India', output['Output']))[0]
        china = list(filter(lambda x: x['region'] == 'China', output['Output']))[0]
        self.assertEqual(ny['total_cost'], 11000)
        self.assertEqual(ny['machines'], [('8XLarge', 1), ('2XLarge', 1), ('XLarge', 1), ('Large', 1)])
        self.assertEqual(india['total_cost'], 10665)
        self.assertEqual(india['machines'], [('8XLarge', 1), ('2XLarge', 1), ('Large', 3)])
        self.assertEqual(china['total_cost'], 9450)
        self.assertEqual(china['machines'], [('8XLarge', 1), ('XLarge', 3), ('Large', 1)])

    def test_four(self):
        input_val = '100 units for 24 Hours'
        output = resource.main(input_val)
        ny = list(filter(lambda x: x['region'] == 'New York', output['Output']))[0]
        india = list(filter(lambda x: x['region'] == 'India', output['Output']))[0]
        china = list(filter(lambda x: x['region'] == 'China', output['Output']))[0]
        self.assertEqual(ny['total_cost'], 24096)
        self.assertEqual(ny['machines'], [('4XLarge', 1), ('XLarge', 1)])
        self.assertEqual(india['total_cost'], 26544)
        self.assertEqual(india['machines'], [('2XLarge', 2), ('Large', 2)])
        self.assertEqual(china['total_cost'], 20880)
        self.assertEqual(china['machines'], [('4XLarge', 1), ('XLarge', 1)])

    def test_five(self):
        input_val = '1100 units for 12 Hours'
        output = resource.main(input_val)
        ny = list(filter(lambda x: x['region'] == 'New York', output['Output']))[0]
        india = list(filter(lambda x: x['region'] == 'India', output['Output']))[0]
        china = list(filter(lambda x: x['region'] == 'China', output['Output']))[0]
        self.assertEqual(ny['total_cost'], 118248)
        self.assertEqual(ny['machines'], [('8XLarge', 6), ('4XLarge',1), ('2XLarge', 1), ('XLarge', 1)])
        self.assertEqual(india['total_cost'], 111828)
        self.assertEqual(india['machines'], [('8XLarge', 6), ('2XLarge', 3), ('Large', 2)])
        self.assertEqual(china['total_cost'], 100200)
        self.assertEqual(china['machines'], [('8XLarge', 6), ('4XLarge', 1), ('XLarge', 3)])


if __name__ == '__main__':
    unittest.main()
