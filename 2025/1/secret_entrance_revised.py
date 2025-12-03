import sys
import math

position = 50 # The dial starts pointing at 50
result = 0

def parse_line(line):
  global position
  global result

  direction = line[0]
  steps = int(line[1:])

  if (direction == 'L'):
    steps = -steps
  elif (direction != 'R'):
    print(f"Invalid direction: {direction}")
    return

  start = position
  position += steps

  if (position % 100 == 0):
    # print(f"Zero counted for {position}")
    result += 1

  passes = math.floor(position / 100) - math.floor(start / 100)
  result += abs(passes)

  if (steps < 0):
    # Moved Left
    if (start % 100 == 0):
      # Moving Left from 0 will count as 1 pass
      # Example: start = 0 position = -1 => passes -1
      result -= 1

  if (steps > 0):
    # Moved Right
    if (position % 100 == 0):
      # Moving Right from >0 to 0 WILL count as a pass, so we compensate
      result -= 1

  return

def main():
  global result

  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

  filename = sys.argv[1]

  try:
    with open(filename, 'r') as f:
      for line in f:
        parse_line(line.rstrip())
  except FileNotFoundError:
    print(f"File not found: {filename}")
  
  print(f"Password is: {result}")

if __name__ == "__main__":
  main()
