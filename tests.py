import src.BlockOL.__init__ as BlockOL, unittest

class TestEverything(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(BlockOL.is_prime(2))
        self.assertTrue(BlockOL.is_prime(3))
        self.assertFalse(BlockOL.is_prime(4))
        self.assertTrue(BlockOL.is_prime(5))
        self.assertFalse(BlockOL.is_prime(6))
        self.assertTrue(BlockOL.is_prime(7))
        self.assertFalse(BlockOL.is_prime(8))
        self.assertFalse(BlockOL.is_prime(9))
        self.assertFalse(BlockOL.is_prime(10))
    
    def test_prev_prime(self):
        self.assertEqual(BlockOL.prev_prime(2), None)
        self.assertEqual(BlockOL.prev_prime(5), 3)
        self.assertEqual(BlockOL.prev_prime(10), 7)
        self.assertEqual(BlockOL.prev_prime(50), 47)
        self.assertEqual(BlockOL.prev_prime(100), 97)
        self.assertEqual(BlockOL.prev_prime(500), 499)
        self.assertEqual(BlockOL.prev_prime(1000), 997)
    
    def test_next_prime(self):
        self.assertEqual(BlockOL.next_prime(2), 3)
        self.assertEqual(BlockOL.next_prime(5), 7)
        self.assertEqual(BlockOL.next_prime(10), 11)
        self.assertEqual(BlockOL.next_prime(50), 53)
        self.assertEqual(BlockOL.next_prime(100), 101)
        self.assertEqual(BlockOL.next_prime(500), 503)
        self.assertEqual(BlockOL.next_prime(1000), 1009)
    
    def test_fibn(self):
        self.assertEqual(BlockOL.fibn(102334156), [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155])
    
    def test_fibi(self):
        self.assertEqual(BlockOL.fibi(40), [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155])
    
    def test_fib(self):
        a = [1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946,17711,28657,46368,75025,121393,196418,317811,514229,832040,1346269,2178309,3524578,5702887,9227465,14930352,24157817,39088169,63245986,102334155]
        b = BlockOL.fib()
        for i in a:
            self.assertEqual(next(b), i)
    
    def test_zeros_after(self):
        self.assertEqual(BlockOL.zeros_after(12894670000), 4)
        self.assertEqual(BlockOL.zeros_after(8725100000), 5)
        self.assertEqual(BlockOL.zeros_after(20989810948109000), 3)
        self.assertEqual(BlockOL.zeros_after(0), 1)
    
    def test_counter(self):
        self.assertEqual(BlockOL.counter({}, [1, 5, 2, 6, 1, 5]), {1: 2, 5: 2, 2: 1, 6: 1})
        self.assertEqual(BlockOL.counter({5: 1, 2: 100}, [1, 5, 2, 6, 1, 5]), {1: 2, 5: 3, 2: 101, 6: 1})
    
    def test_diviz(self):
        self.assertEqual(BlockOL.diviz(0), [])
        self.assertEqual(BlockOL.diviz(1), [1])
        self.assertEqual(BlockOL.diviz(2), [1, 2])
        self.assertEqual(BlockOL.diviz(3), [1, 3])
        self.assertEqual(BlockOL.diviz(4), [1, 2, 4])
        self.assertEqual(BlockOL.diviz(123), [1, 3, 41, 123])
    
    def test_diviz_fl(self):
        self.assertEqual(BlockOL.diviz_fl(0), [1, 0])
        self.assertEqual(BlockOL.diviz_fl(1), [1, 1])
        self.assertEqual(BlockOL.diviz_fl(2), [1, 2])
        self.assertEqual(BlockOL.diviz_fl(3), [1, 3])
        self.assertEqual(BlockOL.diviz_fl(4), [2, 2])
        self.assertEqual(BlockOL.diviz_fl(123), [3, 41])
    
    def test_largest_prime_div(self):
        self.assertEqual(BlockOL.largest_prime_div(1), 1)
        self.assertEqual(BlockOL.largest_prime_div(2), 2)
        self.assertEqual(BlockOL.largest_prime_div(3), 3)
        self.assertEqual(BlockOL.largest_prime_div(4), 2)
        self.assertEqual(BlockOL.largest_prime_div(5), 5)
        self.assertEqual(BlockOL.largest_prime_div(6), 3)
        self.assertEqual(BlockOL.largest_prime_div(7), 7)
        self.assertEqual(BlockOL.largest_prime_div(8), 2)
        self.assertEqual(BlockOL.largest_prime_div(9), 3)
        self.assertEqual(BlockOL.largest_prime_div(10), 5)
    
    def test_prime_div(self):
        self.assertEqual(BlockOL.prime_div(1), [])
        self.assertEqual(BlockOL.prime_div(2), [2])
        self.assertEqual(BlockOL.prime_div(3), [3])
        self.assertEqual(BlockOL.prime_div(4), [2, 2])
        self.assertEqual(BlockOL.prime_div(5), [5])
        self.assertEqual(BlockOL.prime_div(6), [2, 3])
        self.assertEqual(BlockOL.prime_div(7), [7])
        self.assertEqual(BlockOL.prime_div(8), [2, 2, 2])
        self.assertEqual(BlockOL.prime_div(9), [3, 3])
        self.assertEqual(BlockOL.prime_div(10), [2, 5])

if __name__ == "__main__":
    unittest.main()