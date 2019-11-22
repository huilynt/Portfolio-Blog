from home.views import *
from blog.views import *
from django.test import TestCase, Client
from django.core import serializers

from blog.forms import CommentForm
from blog.models import Post, Category, Comment

from unittest.mock import MagicMock, patch
import unittest
import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestViews(TestCase):
        pytestmark = pytest.mark.django_db

        def setUp(self):
                print("SETTING UP")
                cat_hobby = Category.objects.create(name="Hobby777777777777")
                post_cca = Post.objects.create(title="CCA", body="Yoga")
                post_cca.categories.add(cat_hobby)
                post_cca.save()
                comment_1 = Comment.objects.create(author="Hui Lin", body="Comment!", post_id=1)
                comment_1.save()
                        
        def test_home_index(self):
                mock = MagicMock()
                response = home_index(mock)
                assert 200 == response.status_code

        def test_blog_index(self):
                mock = MagicMock()
                response = blog_index(mock)
                assert 200 == response.status_code

        def test_blog_category(self):
                mock = MagicMock()
                response = blog_category(mock, 1)
                assert 200 == response.status_code

        def test_blog_detail(self):
                mock = MagicMock()
                response = blog_detail(mock, 1)
                assert 200 == response.status_code

        def test_blog_detail_form(self):
                mock = MagicMock()
                mock.method = 'POST'
                mock.POST = {'author': ['TEST TITLE'], 'body': ['TEST BODY']}
                response = blog_detail(mock, 1)
                assert 200 == response.status_code
                
                
