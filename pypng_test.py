import unittest2 as unittest

import png

class PyPngTest(unittest.TestCase):
  def test01(self):
    i = png.Reader(filename='testdata/test01.png').asDirect()
    self.assertEquals(32, i[0])
    self.assertEquals(20, i[1])

  def test02(self):
    i = png.Reader(filename='testdata/test02.png').asDirect()
    self.assertEquals(3, i[0])
    self.assertEquals(2, i[1])
    d = list(i[2])
    self.assertEquals([255, 255, 0], list(d[0]))
    self.assertEquals([0, 0, 0], list(d[1]))

