from django.test import TestCase
from django.utils import timezone
from products.models import Product, Brand, Comment

from django_dynamic_fixture import G, F


class ProductModelTestCase(TestCase):

    def setUp(self):
        # Crea una instancia de Brand para asociarla al Producto
        self.brand = Brand.objects.create(name='Mi Marca')
        # Crea una instancia de Product para probar
        self.product = Product.objects.create(
            name='Mi Producto',
            price=10.50,
            sku='SKU123',
            category='Electrónicos',
            brand=self.brand,
            discount=5,
            created_date=timezone.now(),
            published_date=timezone.now()
        )

        self.product_g = G(Product, name='Test product', brand=F(name='Test brand'))

    def test_product_str_method(self):
        # Verifica si el método __str__ devuelve el formato esperado
        expected_str = f'{self.product.name} | {self.product.brand}'
        self.assertEqual(str(self.product), expected_str)

    def test_product_attributes(self):
        # Verifica si los atributos del producto son correctos
        self.assertEqual(self.product.name, 'Mi Producto')
        self.assertEqual(self.product.price, 10.50)
        self.assertEqual(self.product.sku, 'SKU123')
        self.assertEqual(self.product.category, 'Electrónicos')
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.discount, 5)
        self.assertIsNotNone(self.product.created_date)
        self.assertIsNotNone(self.product.published_date)


class CommentModelTestCase(TestCase):

    def setUp(self) -> None:
        self.product_g = G(Product, name='Test product', brand=F(name='Test brand'))
        self.comment = G(Comment, author='Mulan', product=self.product_g)

    def test_approve_change_approved_comment(self):
        self.assertEqual(self.comment.approved_comment, False)
        self.assertFalse(self.comment.approved_comment)
        self.comment.approve()
        self.assertEqual(self.comment.approved_comment, True)
        self.assertTrue(self.comment.approved_comment)
