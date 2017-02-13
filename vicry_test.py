import unittest2 as unittest
import vicry

import png
import tempfile

class VicryTest(unittest.TestCase):
  M = vicry.M

  def testKnownData(self):
    self.assertEqual(len(self.M[(1,1)]['a'][0]), 8)
    self.assertEqual(len(self.M[(2,2)]['a'][0]), 8)
    self.assertEqual(len(self.M[(3,3)]['a'][0]), 8)

    self.assertEqual(len(self.M[(1,1)]['t21'][0]), 4)
    self.assertEqual(len(self.M[(1,1)]['t12'][0]), 4)
    self.assertEqual(len(self.M[(1,1)]['t22'][0]), 8)

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

  @staticmethod
  def _count_blocks(color):
    color_map = {}
    for mask_set in color:
      for block in mask_set:
        b = tuple(map(tuple,block))
        num = color_map.setdefault(b, 0)
        color_map[b] = num + 1
    return color_map

  def testStrength(self):
    """ Test that the scheme is not weak.

    Test that there is no correlation between the pattern and the original
    pixel. Black and white pixels should result in exactly the same
    distribution of patterns.

    Note that passing this test doesn't mean that the scheme is safe.
    """
    for key, s in self.M.iteritems():
      if key == (1,1): continue    # Does not apply.
      n, k = key
      self.assertGreaterEqual(n,k)  # (n, k) scheme
      for name, data in s.iteritems():
        black, white = data
        first_block = black[0][0]
        ysize = len(first_block)
        xsize = len(first_block[0])

        white_map = self._count_blocks(white)
        black_map = self._count_blocks(black)
        print 'BLACK:', black_map
        print 'WHITE:', white_map

        for block, white_count in white_map.iteritems():
          debug = str(key) + "/" + name + "/" + str(block)
          print block
          self.assertEquals(white_count, black_map[block], debug)
