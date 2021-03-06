# -*- coding: utf-8 -*-

import unittest

import wiki_link

class Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual("", wiki_link.wiki_links(""))

    def test_link(self):
        self.assertEqual('<a href="http://url.com">url.com</a>', wiki_link.wiki_links("[[url.com]]"))

    def test_deep_link(self):
        self.assertEqual('<a href="http://url.com/special/page">url.com/special/page</a>', wiki_link.wiki_links("[[url.com/special/page]]"))

    def test_link_with_description(self):
        self.assertEqual('<a href="http://url.com">interesting description</a>', wiki_link.wiki_links("[[url.com|interesting description]]"))

    def test_link_with_parenthesis_in_description(self):
        self.assertEqual('<a href="http://url.com">description (DESC)</a>', wiki_link.wiki_links("[[url.com|description (DESC)]]"))

    def test_link_with_ampersand_in_description(self):
        self.assertEqual('<a href="http://url.com">description & stuff</a>', wiki_link.wiki_links("[[url.com|description & stuff]]"))

    def test_link_with_coma_in_description(self):
        self.assertEqual('<a href="http://url.com">description, stuff</a>', wiki_link.wiki_links("[[url.com|description, stuff]]"))

    def test_link_with_accentuated_character_in_description(self):
        self.assertEqual(u'<a href="http://url.com">Umeå éèà</a>', wiki_link.wiki_links(u"[[url.com|Umeå éèà]]"))

    def test_link_start_with_star(self):
        self.assertEqual('<a href="http://url.com">url.com</a>', wiki_link.wiki_links("[[*url.com]]"))

    def test_link_with_minus(self):
        self.assertEqual('<a href="http://url.com">url.com</a>', wiki_link.wiki_links("[[-url.com]]"))

    def test_several_links(self):
        self.assertEqual('<a href="http://url.com">url.com</a> <a href="http://other.org">other.org</a>', wiki_link.wiki_links("[[url.com]] [[other.org]]"))

    def test_text_before_and_after_link(self):
        self.assertEqual(u'hello å <a href="http://url.com">url.com</a> bye bye å', wiki_link.wiki_links("hello å [[url.com]] bye bye å"))


if __name__ == '__main__':
    unittest.main()
