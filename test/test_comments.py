import unittest
from app.models import Pizza, User, Comments
from flask_login import current_user
from app import db

class TestPizza(unittest.TestCase):

    def setUp(self):
        self.user_jerry = User(username='jerry',password='password',email='abc@defg.com')
        self.new_pizza = Pizza(pizza_contents = "My pizza",pizza_category = 'Order',user=self.user_jerry)
        self.new_comment = Comment(comment_contents = "My comment", user=self.user_jerry)
    
    def tearDown(self):
        db.session.delete(self)
        User.query.commit()
        my_user = db.session.query(User).filter(self.user.id==1).first()
        db.session.delete(my_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_contents,"My comments")
        self.assertEquals(self.new_comment.pizza,self.new_pizza)
        self.assertEquals(self.new_comment.user,self.user_jerry)