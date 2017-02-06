M = {
  (1, 1): {
    'a': (
      [ (((0,),),), ],
      [ (((1,),),), ],
    ),
  },
  (2, 2): {
    'a': (
      #  -X            -X
      #  X-            X-
      [ (((0,1),(1,0)), ((0,1),(1,0))), ],
      #  -X            X-
      #  X-            -X
      [ (((0,1),(1,0)), ((1,0),(0,1))), ],
    ),
  },
  (3,3): {
    'a': (
      # XX             X-             X-
      # --             X-             -X
      [ (((1,1),(0,0)), ((1,0),(1,0)), ((1,0),(0,1))), ],
      # XX             X-             -X
      # --             X-             X-
      [ (((1,1),(0,0)), ((1,0),(1,0)), ((0,1),(1,0))), ],
    ),
  },
}

# Rotate a list of lists by 90 degrees.
_rotate = lambda m: zip(*m[::-1])

# Transpose a list of lists.
_transpose = lambda m: zip(*m)

# Flip a list of lists vertically.
_flip_v = lambda m: list(reversed(m))

# Flip a list of lists horizontally.
_flip_h = lambda m: map(_flip_v, m)

# Add (append) the other (90-degree or 180 degree) "rotations" of the patterns.
for _, v1 in M.iteritems():
  for _, v2 in v1.iteritems():
    b, w = v2
    for i in xrange(3):
      b.append(tuple(map(_rotate, b[-1])))
      w.append(tuple(map(_rotate, w[-1])))
