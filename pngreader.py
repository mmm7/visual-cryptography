import png

def _rgb_to_bit(t):
  return int(bool(sum(t)))

def _do_line(l):
  li = list(l)
  al = zip(li[0::3], li[1::3], li[2::3])
  return map(_rgb_to_bit, al)

def file_to_list(fname):
  i = png.Reader(filename=fname).asRGB()
  l = list(i[2])
  return map(_do_line, l)
