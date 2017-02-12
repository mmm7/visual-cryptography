import unittest2 as unittest
import encoder as e

import random

import vicry

class ApplyTest(unittest.TestCase):
  IMG0 = [[0]]
  IMG1 = [[1]]
  IMG2 = [[0,1]]
  IMG3 = [[0], [1]]
  IMG4 = [[1,1],[0,1]]

  def testGetParams(self):
    self.assertEqual((2,2,2), e.get_params(vicry.M[(2,2)]['a']))
    self.assertEqual((3,2,2), e.get_params(vicry.M[(3,3)]['a']))

  def testApplyMasks_1_1(self):
    o = e.apply_masks(self.IMG0, vicry.M[(1,1)]['a'], random.Random(3))
    self.assertEqual(list(o), [[[0]]])

    o = e.apply_masks(self.IMG4, vicry.M[(1,1)]['a'], random.Random(3))
    self.assertEqual(list(o), [[[1, 1], [0, 1]]])

    o = e.apply_masks(self.IMG0, vicry.M[(1,1)]['t12'], random.Random(3))
    self.assertEqual(list(o), [[[0,0]]])

    o = e.apply_masks(self.IMG4, vicry.M[(1,1)]['t12'], random.Random(3))
    self.assertEqual(list(o), [[[1,1,1,1], [0,0,1,1]]])

  def testApplyMasks_2_2(self):
    o = e.apply_masks(self.IMG0, vicry.M[(2,2)]['a'], random.Random(5))
    self.assertEqual(list(o),  [[[0, 1], [1, 0]], [[0, 1], [1, 0]]])

  def testApplyMasks_non_0_1(self):
    """Test values that are not 0 or 1. """
    IMG = [[100,999],[0,7]]

    o = e.apply_masks(IMG, vicry.M[(1,1)]['a'], random.Random(3))
    self.assertEqual(list(o), [[[1, 1], [0, 1]]])

    o = e.apply_masks(IMG, vicry.M[(1,1)]['t12'], random.Random(3))
    self.assertEqual(list(o), [[[1,1,1,1], [0,0,1,1]]])
