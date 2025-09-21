import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<html>", "",[],{})
        node2 = HTMLNode("<html>", "",[],{})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("<head>", "",[],{})
        node2 = HTMLNode("<html>", "",[],{})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode("<html>", "this is a value",[],{})
        node2 = HTMLNode("<html>", "",[],{})
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = HTMLNode("<html>", "this is a value")
        node2 = HTMLNode("<html>", "this is a value")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("<link>", "https://www.boot.dev")
        self.assertEqual(
                "HTMLNode(tag:<link>, value:https://www.boot.dev, children:None, props:None)", repr(node)
        )

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag:p, value:What a strange world, children:None, props:{'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()
