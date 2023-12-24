"""Unit tests for Post model"""
import json
from http import HTTPStatus

from django.test import TestCase
from model_bakery import baker

HOMEPAGE_URL = "http://127.0.0.1:8000/bank/"


class TestBankHomePage(TestCase):
    """test bank home page"""

    def test_bank_homepage_returns_correct_response(self):
        """test if homepage has elements"""
        response = self.client.get(HOMEPAGE_URL)
        self.assertTemplateUsed(response, "bank/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)
