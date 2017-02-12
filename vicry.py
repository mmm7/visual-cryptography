M = {
  (1, 1): {
    # Identity. Test pattern.
    'a': (
      [ (((0,),),), ],
      [ (((1,),),), ],
    ),
    # Scale 2x horizontally. Test pattern.
    't12': (
      [ (((0,0),),), ],
      [ (((1,1),),), ],
    ),
    # Scale 2x vertically. Test pattern.
    't21': (
      [ (((0,),(0,)),), ],
      [ (((1,),(1,)),), ],
    ),
    # Resize 2x. Test pattern
    't22': (
      [ (((0,0),(0,0)),), ],
      [ (((1,1),(1,1)),), ],
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
  (3,2): {
    'a': (
      [
        (((1,1,1),(0,0,0),(0,0,0)), ((1,1,1),(0,0,0),(0,0,0)), ((1,1,1),(0,0,0),(0,0,0))),
        (((0,0,0),(1,1,1),(0,0,0)), ((0,0,0),(1,1,1),(0,0,0)), ((0,0,0),(1,1,1),(0,0,0))),
        (((0,0,0),(0,0,0),(1,1,1)), ((0,0,0),(0,0,0),(1,1,1)), ((0,0,0),(0,0,0),(1,1,1))),
      ],
      [
        # 3 times the same is fine, it'll be transformed.
        (((1,1,1),(0,0,0),(0,0,0)), ((0,0,0),(1,1,1),(0,0,0)), ((0,0,0),(0,0,0),(1,1,1))),
        (((1,1,1),(0,0,0),(0,0,0)), ((0,0,0),(1,1,1),(0,0,0)), ((0,0,0),(0,0,0),(1,1,1))),
        (((1,1,1),(0,0,0),(0,0,0)), ((0,0,0),(1,1,1),(0,0,0)), ((0,0,0),(0,0,0),(1,1,1))),
      ]
    ),
    'b': (
      # X-             X-             X-
      # --             --             --
      [ (((1,0),(0,0)), ((1,0),(0,0)), ((1,0),(0,0))), ],
      # X-             -X             --
      # --             --             -X
      [ (((1,0),(0,0)), ((0,1),(0,0)), ((0,0),(0,1))), ],
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
  (4,2): {
    'a': (
      # X-             X-             X-               X-
      # --             --             --               --
      [ (((1,0),(0,0)), ((1,0),(0,0)), ((1,0),(0,0)), ((1,0),(0,0))),],
      # X-             -X             --               --
      # --             --             -X               X-
      [ (((1,0),(0,0)), ((0,1),(0,0)), ((0,0),(0,1)), ((0,0),(1,0))),],
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

# Flatten a list of lists.
_flatten = lambda l: [item for sublist in l for item in sublist]

def _transformations(p):
  return [
    tuple(map(lambda x: _flip_h(x), p)),
    tuple(map(lambda x: _flip_h(_flip_v(x)), p)),
    tuple(map(lambda x: _flip_v(x), p)),
  ]

def _square_transformations(p):
  return [
    tuple(map(lambda x: _transpose(x), p))
  ]

def _all_transformations(ps, f):
  return _flatten([f(p) for p in ps])

# Add (append) the flipped versions, rotations, transpositions of the patterns.
for _, v1 in M.iteritems():
  for _, v2 in v1.iteritems():
    b, w = v2
    b.extend(_all_transformations(b, _transformations))
    w.extend(_all_transformations(w, _transformations))
    sample = b[0][0]
    if len(sample) == len(sample[0]):
      b.extend(_all_transformations(b, _square_transformations))
      w.extend(_all_transformations(w, _square_transformations))
