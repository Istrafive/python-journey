def merge_sort(arr):
  """Sorts a list using the merge sort algorithm.

  Args:
    arr: The list to be sorted.

  Returns:
    The sorted list.
  """

  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

def merge(left, right):
  """Merges two sorted lists into a single sorted list.

  Args:
    left: The left sorted list.
    right: The right sorted list.

  Returns:
    The merged sorted list.
  """

  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result += left[i:]

  result += right[j:]

  return result

def selection_sort(arr):
  """Sorts a list using the selection sort algorithm.

  Args:
    arr: The list to be sorted.

  Returns:
    The sorted list.
  """

  for i in range(len(arr)):
    min_index = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr