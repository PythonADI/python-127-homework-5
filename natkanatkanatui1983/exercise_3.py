def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

for score in  range (0,  101, 10):
    print(f"score: {score}, grade: {grade(score)}")