from home.views import *
from blog.views import *
from django.test import TestCase, Client

from blog.models import Post, Category, Comment

from unittest.mock import MagicMock
import unittest
import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestModels(TestCase):
    pytestmark = pytest.mark.django_db

    def test_create_category(self):
        new_cat = Category.objects.create(name="0TbncqeZq3")
        all_cat = Category.objects.all()
        get_cat = Category.objects.get(name="0TbncqeZq3")
        assert True == all_cat.filter(pk=get_cat.pk).exists()

    def test_create_post(self):
        new_cat = Category.objects.create(name="0TbncqeZq3")
        get_cat = Category.objects.get(name="0TbncqeZq3")
        new_post = Post.objects.create(title="zWLixOPcpu", body="oZobioGss8")
        new_post.categories.add(get_cat)
        new_post.save()
        
        all_post = Post.objects.all()
        get_post = Post.objects.get(title="zWLixOPcpu")
        assert True == all_post.filter(pk=get_post.pk).exists()

    def test_create_comment(self):
        new_cat = Category.objects.create(name="0TbncqeZq3")
        get_cat = Category.objects.get(name="0TbncqeZq3")
        new_post = Post.objects.create(title="zWLixOPcpu", body="oZobioGss8")
        new_post.categories.add(get_cat)
        new_post.save()
        
        new_comment = Comment.objects.create(author="PhcSAds82v", body="PhcSAds82v", post_id=new_post.pk)
        all_comment = Comment.objects.all()
        get_comment = Comment.objects.get(author="PhcSAds82v")
        assert True == all_comment.filter(pk=get_comment.pk).exists()
    


                
