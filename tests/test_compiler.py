import unittest
from anomalo_compile.compiler import main


class TestCompiler(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()