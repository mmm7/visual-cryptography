import os.path
import png
import sys

import encoder
import pngreader
import random
import vicry

def main():
  if len(sys.argv) == 4:
    n, k, input_fname = sys.argv[1:]
    scheme = 'a'
  elif len(sys.argv) == 5:
    n, k, input_fname, scheme = sys.argv[1:]
  else:
    print '%s <n> <k> <imagefile> [scheme]' % sys.argv[0]
    sys.exit(1)

  
  i = pngreader.file_to_list(input_fname)
  print len(i[0]), 'x', len(i)
  masks = vicry.M[(int(n),int(k))][scheme]
  outputs = encoder.apply_masks(i, masks, random.Random())
  fname, ext = os.path.splitext(input_fname)
  output_fnames = ['%s_%d%s' % (fname, i, ext) for i in xrange(len(outputs)) ]
  for fname, output in zip(output_fnames, outputs):
    with open(fname, 'wb') as f:
      w = png.Writer(len(output[0]), len(output), greyscale=True, bitdepth=1)
      w.write(f, output)

main()
