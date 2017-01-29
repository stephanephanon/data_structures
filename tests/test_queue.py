from unittest import TestCase
from queue import CircularArrayQueue, QueueException, PythonListQueue, LinkedListQueue


class CircularArrayQueueTests(TestCase):
    def test_max_queue_size_zero(self):
        with self.assertRaises(QueueException):
            q = CircularArrayQueue(max_queue_size=0)

    def test_enqueue_and_first(self):
        """
        Test that we can see the first element in the queue
        """
        # nothing in the queue
        q = CircularArrayQueue(max_queue_size=5)
        with self.assertRaises(QueueException):
            q.first()

        # one item in the queue
        q.enqueue('a')
        ret = q.first()
        self.assertEqual(ret, 'a')

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.first()
        self.assertEqual(ret, 'a')

    def test_size(self):
        # nothing in the queue
        q = CircularArrayQueue(max_queue_size=5)
        self.assertEqual(q.size(), 0)

        # one item in the queue
        q.enqueue('a')
        self.assertEqual(q.size(), 1)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        q.size()
        self.assertEqual(q.size(), 3)

    def test_dequeue(self):
        # nothing in the queue
        q = CircularArrayQueue(max_queue_size=5)
        with self.assertRaises(QueueException):
            q.dequeue()

        # one item in the queue
        q.enqueue('a')
        ret = q.dequeue()
        self.assertEqual(ret, 'a')
        self.assertEqual(q.size(), 0)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.dequeue()
        self.assertEqual(ret, 'b')
        self.assertEqual(q.size(), 1)
        ret = q.dequeue()
        self.assertEqual(ret, 'c')
        self.assertEqual(q.size(), 0)

    def test_is_empty(self):
        # nothing in the queue
        q = CircularArrayQueue(max_queue_size=5)
        self.assertTrue(q.is_empty())

        # one item in the queue
        q.enqueue('x')
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        # nothing in the queue
        q = CircularArrayQueue(max_queue_size=2)
        self.assertFalse(q.is_full())

        # add one
        q.enqueue('a')
        self.assertFalse(q.is_full())

        # add another
        q.enqueue('b')
        self.assertTrue(q.is_full())

        # go beyond max (wraps around)
        q.enqueue('c')
        self.assertTrue(q.is_full())


class PythonListQueueTests(TestCase):
    def test_enqueue_and_first(self):
        """
        Test that we can see the first element in the queue
        """
        # nothing in the queue
        q = PythonListQueue()
        with self.assertRaises(QueueException):
            q.first()

        # one item in the queue
        q.enqueue('a')
        ret = q.first()
        self.assertEqual(ret, 'a')

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.first()
        self.assertEqual(ret, 'a')

    def test_size(self):
        # nothing in the queue
        q = PythonListQueue()
        self.assertEqual(q.size(), 0)

        # one item in the queue
        q.enqueue('a')
        self.assertEqual(q.size(), 1)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        q.size()
        self.assertEqual(q.size(), 3)

    def test_dequeue(self):
        # nothing in the queue
        q = PythonListQueue()
        with self.assertRaises(QueueException):
            q.dequeue()

        # one item in the queue
        q.enqueue('a')
        ret = q.dequeue()
        self.assertEqual(ret, 'a')
        self.assertEqual(q.size(), 0)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.dequeue()
        self.assertEqual(ret, 'b')
        self.assertEqual(q.size(), 1)
        ret = q.dequeue()
        self.assertEqual(ret, 'c')
        self.assertEqual(q.size(), 0)

    def test_is_empty(self):
        # nothing in the queue
        q = PythonListQueue()
        self.assertTrue(q.is_empty())

        # one item in the queue
        q.enqueue('x')
        self.assertFalse(q.is_empty())


class LinkedListQueueTests(TestCase):
    def test_enqueue_and_first(self):
        """
        Test that we can see the first element in the queue
        """
        # nothing in the queue
        q = LinkedListQueue()
        with self.assertRaises(QueueException):
            q.first()

        # one item in the queue
        q.enqueue('a')
        ret = q.first()
        self.assertEqual(ret, 'a')

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.first()
        self.assertEqual(ret, 'a')

    def test_size(self):
        # nothing in the queue
        q = LinkedListQueue()
        self.assertEqual(q.size(), 0)

        # one item in the queue
        q.enqueue('a')
        self.assertEqual(q.size(), 1)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        q.size()
        self.assertEqual(q.size(), 3)

    def test_dequeue(self):
        # nothing in the queue
        q = LinkedListQueue()
        with self.assertRaises(QueueException):
            q.dequeue()

        # one item in the queue
        q.enqueue('a')
        ret = q.dequeue()
        self.assertEqual(ret, 'a')
        self.assertEqual(q.size(), 0)

        # multiple items in the queue
        q.enqueue('b')
        q.enqueue('c')
        ret = q.dequeue()
        self.assertEqual(ret, 'b')
        self.assertEqual(q.size(), 1)
        ret = q.dequeue()
        self.assertEqual(ret, 'c')
        self.assertEqual(q.size(), 0)

    def test_is_empty(self):
        # nothing in the queue
        q = LinkedListQueue()
        self.assertTrue(q.is_empty())

        # one item in the queue
        q.enqueue('x')
        self.assertFalse(q.is_empty())