import unittest2 as unittest
import vicry

import png
import tempfile

class VicryTest(unittest.TestCase):
  M = vicry.M

  def testKnownData(self):
    self.assertEqual(len(self.M[(1,1)]['a'][0]), 4)
    self.assertEqual(len(self.M[(2,2)]['a'][0]), 4)
    self.assertEqual(len(self.M[(3,3)]['a'][0]), 4)

  def testRotate(self):
    self.assertEqual(vicry._rotate([(1,)]), [(1,)])
    self.assertEqual(vicry._rotate([(1,2), (3,4)]), [(3,1), (4,2)])

  def testTranspose(self):
    self.assertEqual(vicry._transpose([(1,)]), [(1,)])
    self.assertEqual(vicry._transpose([(1,2), (3,4)]), [(1,3), (2,4)])
    self.assertEqual(
        vicry._transpose([(1,2,3), (4,5,6)]), [(1,4), (2,5), (3,6)])

  def testFlipV(self):
    self.assertEqual(vicry._flip_v([(1,)]), [(1,)])
    self.assertEqual(vicry._flip_v([(1,2)]), [(1,2)])
    self.assertEqual(vicry._flip_v([(1,2), (3,4)]), [(3,4), (1,2)])

  def testFlipH(self):
    self.assertEqual(vicry._flip_h([(1,)]), [[1,]])
    self.assertEqual(vicry._flip_h([(1,2)]), [[2,1]])
    self.assertEqual(vicry._flip_h([(1,2), (3,4)]), [[2,1], [4,3]])

  def testSanity(self):
    for key, s in self.M.iteritems():
      n, k = key
      self.assertGreaterEqual(n,k)  # (n, k) scheme
      for name, data in s.iteritems():
        debug = str(key) + "/" + name + "/"
        self.assertEqual(len(data), 2, debug)  # pixel: black, white
        black, white = data
        self.assertEqual(len(black), len(white), debug)
        first_block = black[0][0]
        ysize = len(first_block)
        self.assertGreater(ysize, 0, debug)
        xsize = len(first_block[0])
        self.assertGreater(xsize, 0, debug)

        for mask_set in white + black:
          self.assertEqual(len(mask_set), n)
          # All the blocks should be...
          for block in mask_set:
            # ... the same size,
            self.assertEqual(len(block), ysize, debug + str(block))
            self.assertEqual(len(block[0]), xsize, debug + str(block))
            # ... only have 0s and 1s.
            for row in block:
              for cell in row:
                self.assertTrue(cell in (0,1))
