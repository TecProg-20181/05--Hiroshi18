import os
import unittest
from diskspace import bytes_to_readable, print_tree, subprocess_check_output, show_space_list


class TestDiskSpace(unittest.TestCase):

    def test_subprocess_check_output(self):
        func = subprocess_check_output('pwd')
        cwd = os.getcwd()+'\n'
        self.assertEquals(cwd, func)

    def test_subprocess_check_output_error(self):
        with self.assertRaises(OSError): subprocess_check_output('not')

    def test_bytes_to_readable_B(self):
        func = bytes_to_readable(1)
        self.assertEquals('512.00B', func)

    def test_bytes_to_readable_Kb(self):
        func = bytes_to_readable(1024)
        self.assertEquals('512.00Kb', func)

    def test_bytes_to_readable_Mb(self):
        func = bytes_to_readable(1048576)
        self.assertEquals('512.00Mb', func)

    def test_bytes_to_readable_Gb(self):
        func = bytes_to_readable(1073750000)
        self.assertEquals('512.00Gb', func)

    def test_bytes_to_readable_Tb(self):
        func = bytes_to_readable(1099504999000)
        self.assertEquals('512.00Tb', func)

    def test_bytes_to_readable_error(self):
        with self.assertRaises(TypeError): bytes_to_readable('test')

if __name__ == '__main__':
    unittest.main()