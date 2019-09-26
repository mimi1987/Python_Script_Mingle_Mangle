def recursiveCall(n):
  # Exit condition
  if n == 1:
    return 1
   # Recursive call of recursiveCall
	return n * recursiveCall(n-1)
