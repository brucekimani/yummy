import unittest
from app.models import Pizza, User
from flask_login import current_user
from app import db

class TestPizza(unittest.TestCase):

    def setUp(self):
        self.user_jerry = User(username='jerry',password='password',email='abc@defg.com')
        self.new_pizza = Pizza(pizza_contents = "My pizza",pizza_category = 'Order',user=self.user_jerry)
    
    def tearDown(self):
        Pizza.query.delete()
        User.query.delete()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pizza,Pizza))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pizza.pizza_contents,"My pizza")
        self.assertEquals(self.new_pizza.pizza_category,'Order')
        self.assertEquals(self.new_pizza.user,self.user_jerry)