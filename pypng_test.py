import unittest2 as unittest

import png
import tempfile

class PyPngTest(unittest.TestCase):
  DIR = tempfile.mkdtemp()
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

  def testWrite(self):
    fname = self.DIR + '/ttt.png'
    s = [[0,1,0,1],[1,1,0,0]]
    with open(fname, 'wb') as f:
      w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
      w.write(f, s)

    i = png.Reader(filename=fname).asDirect()
    self.assertEquals(4, i[0])
    self.assertEquals(2, i[1])
    d = list(i[2])
    self.assertEquals([0, 1, 0, 1], list(d[0]))
    self.assertEquals([1, 1, 0, 0], list(d[1]))
