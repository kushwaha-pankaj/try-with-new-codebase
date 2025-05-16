Title: Check if Number is Integer or Decimal

```python
def check_number_type(num):
    if isinstance(num, int):
        return "Integer"
    elif isinstance(num, float):
        return "Decimal"
    else:
        return "Not a valid number"

# Example usage:
number = 3.14
print(check_number_type(number))  # Output: Decimal

number = 5
print(check_number_type(number))  # Output: Integer
```