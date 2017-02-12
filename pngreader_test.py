import unittest2 as unittest

import pngreader as p

class PngreadedTest(unittest.TestCase):
  def testRgbToBit(self):
    self.assertEqual(p._rgb_to_bit((0,0,0)), 0)
    self.assertEqual(p._rgb_to_bit((1,0,0)), 1)
    self.assertEqual(p._rgb_to_bit((0,1,0)), 1)
    self.assertEqual(p._rgb_to_bit((0,0,1)), 1)
    self.assertEqual(p._rgb_to_bit((0,0,255)), 1)
    self.assertEqual(p._rgb_to_bit((0,0,2955)), 1)

  def testDoLine(self):
    self.assertEqual(p._do_line([0,0,0, 1,0,0, 0,1,0, 0,0,0]), [0,1,1,0])

  def testFileToList(self):
    l = p.file_to_list('testdata/test02.png')
    self.assertEqual(l, [[1,1,0], [0,0,0]])

    l = p.file_to_list('testdata/test01.png')
    self.assertEqual(len(l[0]), 32)
    self.assertEqual(len(l), 20)

    l = p.file_to_list('testdata/hullam.png')
    self.assertEqual(len(l[0]), 200)
    self.assertEqual(len(l), 100)
