import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_explosiveness(self):
        """Test explosiveness."""
        prod = Product('Test Product')
        self.assertTrue(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        prod = generate_products()
        print(len(prod))
        self.assertTrue(prod, 25)

if __name__ == '__main__':
    unittest.main()
