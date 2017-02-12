def get_params(masks):
  """ Return the important parameters of a mask: (n, pixel_x, pixel_y).

  n: Number of output images (different masks for a pixel).
  pixel_x: width of a single masK
  pixel_y: height of a single mask
  """
  black_masks, white_masks = masks
  sample_mask = white_masks[0][0]
  n = len(white_masks[0])
  pixel_y = len(sample_mask)
  pixel_x = len(sample_mask[0])
  return n, pixel_x, pixel_y

def apply_masks(image, masks, random):
  """Apply the visual cryptography masks from 'masks' to 'image'.

  A list of output images is returned.
  The number and size of the output images is determined by 'masks'.
  'random' is the random number source. random.Random() can be passed.
  """
  n, pixel_x, pixel_y = get_params(masks)
  black_masks, white_masks = masks
  # outputs is a list of output images.
  outputs = [[] for _ in xrange(n)]
  assert n == len(outputs)
  for row in image:
    assert n == len(outputs)
    # Add pixel_y new rows to each of the outputs.
    map(lambda x: x.extend([[] for _ in xrange(pixel_y)]), outputs)
    for orig_pixel in row:
      # Processing a pixel of the original image.
      # Which set of mask sets to use?
      masks_to_use = (black_masks, white_masks)[bool(orig_pixel)]
      # Pick one mask set (one for each output image).
      masks = random.choice(masks_to_use)
      assert n == len(masks)
      assert n == len(outputs)
      random.shuffle(outputs)  # This is important for some masks.
      for output, mask in zip(outputs, masks):
        assert pixel_y == len(mask)
        for y, mask_row in enumerate(mask):
          assert pixel_x == len(mask_row)
          # Fill the last rows.
          output[-pixel_y+y].extend(mask_row)
  return outputs
