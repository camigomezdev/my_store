from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from django_dynamic_fixture import G, F

from products.models import Product, Comment


class GetProductViewTest(TestCase):
    def setUp(self):
        self.product_g = G(Product, name='Test product', brand=F(name='Test brand'), price=10.5)
        self.comment = G(Comment, product=self.product_g, text='Msg for test', created_date='2013-04-09')

    def test_view_url_accessible_by_name(self):
        print(Comment.objects.all())
        response = self.client.get(reverse('get_product', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('get_product', args=[1]))
        self.assertTemplateUsed(response, 'products/show_product.html')

    def test_view_displays_product_details(self):
        response = self.client.get(reverse('get_product', args=[1]))
        self.assertContains(response, 'Test product')
        self.assertContains(response, '10.5')

    @freeze_time('2013-04-09')
    def test_view_displays_comments(self):
        response = self.client.get(reverse('get_product', args=[1]))
        self.assertEqual(self.comment.created_date, '2013-04-09')
        self.assertContains(response, 'Msg for test')
