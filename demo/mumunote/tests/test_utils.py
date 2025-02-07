import os
import unittest
from common.utils import ImageCode, compress_image

class UtilsTestCase(unittest.TestCase):
    def test_image_code(self):
        image_code = ImageCode()
        code, image_b_string = image_code.get_code()
        self.assertIsNotNone(code)
        self.assertIsNotNone(image_b_string)

    def test_compress_image(self):
        # 假设有一个图片文件
        source = 'tests/test_image.jpg'
        dest = 'tests/test_image_compressed.jpg'
        compress_image(source, dest, 1200)
        self.assertTrue(os.path.exists(dest))

if __name__ == '__main__':
    unittest.main()
