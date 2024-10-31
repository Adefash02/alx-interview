#!/usr/bin/python3

def validUTF8(data):
  """
  This function validates if a list of integers represents a valid UTF-8 encoding.

  Args:
      data: A list of integers representing bytes.

  Returns:
      True if the data is valid UTF-8 encoding, False otherwise.
  """
  consecutive_ones = 0  # Tracks the number of consecutive leading 1's in a byte

  for byte in data:
    # Get the 8 least significant bits (representing the actual byte data)
    current_byte = byte & 0xFF

    # Check for single-byte characters (start with 0)
    if consecutive_ones == 0:
      if current_byte < 0x80:
        continue  # Valid single-byte character, move to next byte
      else:
        # Check for number of leading 1's based on byte range (2, 3, or 4 bytes)
        num_leading_ones = 0
        while current_byte & 0x80:
          num_leading_ones += 1
          current_byte = current_byte << 1

        # Invalid character if number of leading 1's is not 2, 3, or 4
        if num_leading_ones not in (2, 3, 4):
          return False

        consecutive_ones = num_leading_ones - 1  # Track remaining continuation bytes
    else:
      # Check for continuation bytes (start with 10)
      if not (current_byte & 0xC0 == 0x80):
        return False
      consecutive_ones -= 1  # Decrement counter for continuation bytes

  # Check if all continuation bytes are processed
  return consecutive_ones == 0

# Example usage (same as provided)
if __name__ == "__main__":
  data = [65]
  print(validUTF8(data))

  data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
  print(validUTF8(data))

  data = [229, 65, 127, 256]
  print(validUTF8(data))

