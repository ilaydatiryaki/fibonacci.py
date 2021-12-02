def calculateFibonacci(n):
  if n < 2:
    return n

  return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
