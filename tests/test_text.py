# -*- coding: utf-8 -*-
import unittest
from thaibraille.text import *


class TestTextPackage(unittest.TestCase):
    def test_thai_word_braille(self):
        self.assertEqual(thai_word_braille("ลิ้น"), '⠇⠃⠲⠝')
        self.assertEqual(thai_word_braille("ว่าง"), '⠺⠔⠡⠻')
        self.assertEqual(thai_word_braille("แก้ม"), '⠣⠛⠲⠍')
        self.assertEqual(thai_word_braille("เรียน"), '⠗⠷⠝')

    def test_thai_text_braille(self):
        self.assertEqual(thai_text_braille("แมวกิน   ปลา"), ['⠣⠍⠺', '⠛⠃⠝', '   ', '⠯⠇⠡'])
