M = {
  (1, 1): {
    'a': (
      [ (((1,),),), ],
      [ (((0,),),), ],
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

# Rotate a list of lists.
_rotate = lambda m: zip(*m[::-1])

# Add (append) the 3 other (90-degree) "rotations" of the patterns.
for _, v1 in M.iteritems():
  for _, v2 in v1.iteritems():
    w, b = v2
    for i in xrange(3):
      w.append(tuple(map(_rotate, w[-1])))
      b.append(tuple(map(_rotate, b[-1])))
