from unorderedlist import UnorderedList
import unittest


class TestUnorderedList(unittest.TestCase):

    def setUp(self):
        self.mylist = UnorderedList()

    def test_add_and_search_items(self):

        for i in [1, 2, 3, 4]:
            self.mylist.add(i)
            self.assertTrue(self.mylist.search(i))

    def test_list_size(self):

        for i in [1, 2, 3, 4]:
            self.mylist.add(i)
            self.assertEqual(self.mylist.size(), i)

    def test_append_items(self):

        for i in [1, 2, 3, 4]:
            self.mylist.append(i)
            self.assertEqual(self.mylist.index(i), self.mylist.size()-1)

    def test_removing_items(self):

        for i in range(10):
            self.mylist.append(i)

        for i in [9, 0, 4, 7]:
            size = self.mylist.size()
            self.mylist.remove(i)
            self.assertEqual(self.mylist.size(), size-1)

    def test_is_empty_method(self):
        self.assertTrue(self.mylist.isEmpty())
        self.mylist.add(2)
        self.assertFalse(self.mylist.isEmpty())

    def test_pop_item(self):

        for i in range(1, 5):
            self.mylist.add(i)

        for i in range(4, 0, -1):
            size = self.mylist.size()
            self.assertEqual(self.mylist.pop(), i)
            self.assertEqual(self.mylist.size(), size-1)

    def test_insert_items(self):

        for i in range(10):
            self.mylist.add(i)

        for pos, val in [(2, 33), (4, 55), (0, 11)]:
            self.mylist.insert(pos, val)
            self.assertEqual(self.mylist.index(val), pos)
