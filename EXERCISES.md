# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

## exercise_1.py — Introduce

Write a function `introduce(name, age)` that prints one line:
`<name> is <age> years old.` Then call it with these two lines:

```python
introduce("Nina", 25)
introduce("Luka", 30)
```

Expected output:
```
Nina is 25 years old.
Luka is 30 years old.
```

## exercise_2.py — Fix the bug

This code should print `Total: 5`, but it prints `5` and then
`Total: None`. Copy it into `exercise_2.py`, then fix the function so
that `total` is `5`. Change only the line with the `BUG` comment.

```python
def add(a, b):
    print(a + b)   # BUG: fix this line

total = add(2, 3)
print(f"Total: {total}")
```

Expected output:
```
Total: 5
```

## exercise_3.py — Grade function

Write a function `grade(score)` that returns the letter grade: `"A"`
for 90 and above, `"B"` for 80-89, `"C"` for 70-79, otherwise `"F"`.
The function must `return` the letter, not print it. Then call it from
this loop:

```python
for score in range(60, 101, 10):
    print(f"{score}: {grade(score)}")
```

Expected output:
```
60: F
70: C
80: B
90: A
100: A
```

## exercise_4.py — Countdown with a step

Write a function `countdown(start, step=1)` that prints the numbers
from `start` down to `1`, going down by `step` each time. `step` has a
default value of `1`. Use a `while` loop inside the function. Then call
it like this:

```python
countdown(3)
print("---")
countdown(10, 3)
```

Expected output:
```
3
2
1
---
10
7
4
1
```

## exercise_5.py — Bonus: count the primes

A prime number is a whole number greater than 1 that divides evenly
only by 1 and by itself (2, 3, 5, 7, 11, ...). So 1 is not prime.
Write two functions:

- `is_prime(number)` returns `True` if `number` is prime, otherwise
  `False`.
- `count_primes(limit)` loops over `range(1, limit + 1)`, uses
  `is_prime` to count how many of those numbers are prime, and returns
  the count.

Hint: `number % divisor == 0` means `number` divides evenly by
`divisor`. Check every divisor from 2 up to `number - 1`.

Then call it like this:

```python
print(count_primes(10))
print(count_primes(20))
```

Expected output:
```
4
8
```
