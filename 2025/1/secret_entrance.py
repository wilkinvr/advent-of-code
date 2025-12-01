import sys

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
    sys.exit(1)

  position += steps

  if (position % 100 == 0):
    # print(f"Zero counted for {position}")
    result += 1

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
