import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

def md(text):
    cells.append(nbf.v4.new_markdown_cell(text))

def code(text):
    cells.append(nbf.v4.new_code_cell(text))

# ---------------------------------------------------------------
md("""# Data Science Fundamentals Assessment

**Submission:** Task 1 — Data Science Fundamentals Assessment
**Author:** _<your name here>_
**Date:** _<submission date>_

This notebook demonstrates the foundational Data Science concepts covered in this
task: the Data Science lifecycle, Python programming basics, statistical
foundations, data types & structures, and clean-coding best practices, closing
with a set of practical assignments.
""")

# ---------------------------------------------------------------
md("""## 1. The Data Science Lifecycle

A typical Data Science project moves through six broad stages:

1. **Problem Definition** — understand the business question and success criteria.
2. **Data Collection** — gather data from databases, APIs, files, or sensors.
3. **Data Cleaning & Preparation** — handle missing values, duplicates, and
   inconsistent types so the data is analysis-ready.
4. **Exploratory Data Analysis (EDA)** — summarize and visualize the data to
   find patterns, trends, and relationships.
5. **Modeling / Analysis** — apply statistical methods or machine learning to
   answer the question.
6. **Communication** — present findings through reports, dashboards, or
   visualizations for stakeholders.

**Common types of data analysis:**
- *Descriptive* — what happened (summary statistics, dashboards)
- *Diagnostic* — why it happened (correlation, root-cause analysis)
- *Predictive* — what is likely to happen (forecasting, regression)
- *Prescriptive* — what should be done (optimization, recommendations)

**Industry use cases:** fraud detection in banking, recommendation engines in
retail, patient-risk scoring in healthcare, demand forecasting in supply
chains, and churn prediction in telecom.
""")

# ---------------------------------------------------------------
md("## 2. Python Programming Basics")

md("### 2.1 Variables and Data Types")
code("""# Core Python data types used throughout Data Science
name = "Aarav"            # str
age = 20                  # int
gpa = 8.75                 # float
is_enrolled = True         # bool

print(name, type(name))
print(age, type(age))
print(gpa, type(gpa))
print(is_enrolled, type(is_enrolled))
""")

md("### 2.2 Operators")
code("""a, b = 17, 5

print("Arithmetic:", a + b, a - b, a * b, a / b, a // b, a % b, a ** 2)
print("Comparison:", a > b, a == b, a != b)
print("Logical:", (a > 10) and (b < 10), (a < 10) or (b < 10), not is_enrolled)
""")

md("### 2.3 Conditional Statements")
code("""def grade_band(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

for s in [95, 82, 67, 40]:
    print(s, "->", grade_band(s))
""")

md("### 2.4 Loops")
code("""# for loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print("Squares:", squares)

# while loop
count, total = 1, 0
while count <= 5:
    total += count
    count += 1
print("Sum 1..5 via while:", total)
""")

md("### 2.5 Functions")
code("""def descriptive_summary(numbers):
    \"\"\"Return count, sum, and average of a list of numbers.\"\"\"
    n = len(numbers)
    total = sum(numbers)
    avg = total / n if n else 0
    return {"count": n, "sum": total, "average": avg}

descriptive_summary([88.5, 76.0, 91.2, 58.4, 73.6])
""")

md("### 2.6 Lists, Tuples, Dictionaries, and Sets")
code("""# List - ordered, mutable
scores = [88.5, 76.0, 91.2, 58.4, 73.6]
scores.append(95.0)
print("List:", scores)

# Tuple - ordered, immutable
coordinates = (28.6139, 77.2090)  # New Delhi lat/long
print("Tuple:", coordinates)

# Dictionary - key/value pairs
student = {"name": "Aarav Sharma", "age": 20, "grade": "A"}
print("Dict:", student)

# Set - unordered, unique elements
cities = {"Delhi", "Mumbai", "Delhi", "Pune", "Bangalore"}
print("Set (duplicates removed):", cities)
""")

md("### 2.7 Basic File Handling")
code("""report_path = "sample_output.txt"

with open(report_path, "w") as f:
    f.write("Data Science Fundamentals Assessment\\n")
    f.write(f"Average score of sample: {descriptive_summary(scores)['average']:.2f}\\n")

with open(report_path, "r") as f:
    print(f.read())
""")

# ---------------------------------------------------------------
md("## 3. Statistical Foundations")
code("""import numpy as np
from scipy import stats as st

data = np.array([88.5, 76.0, 91.2, 58.4, 73.6, 95.0, 45.2, 79.8, 61.0, 89.9])

mean_val = np.mean(data)
median_val = np.median(data)
mode_val = st.mode(data, keepdims=True).mode[0]
variance_val = np.var(data, ddof=1)      # sample variance
std_val = np.std(data, ddof=1)           # sample standard deviation
p25, p50, p75 = np.percentile(data, [25, 50, 75])

print(f"Mean:      {mean_val:.2f}")
print(f"Median:    {median_val:.2f}")
print(f"Mode:      {mode_val:.2f}")
print(f"Variance:  {variance_val:.2f}")
print(f"Std Dev:   {std_val:.2f}")
print(f"25th pct:  {p25:.2f}")
print(f"50th pct:  {p50:.2f}")
print(f"75th pct:  {p75:.2f}")
""")

md("### 3.1 Probability Basics")
code("""# Simple probability: chance of drawing a score >= 80 at random
above_80 = (data >= 80).sum()
prob_above_80 = above_80 / len(data)
print(f"P(score >= 80) = {prob_above_80:.2f}")
""")

md("### 3.2 Correlation")
code("""import pandas as pd

study_hours = [5, 3, 6, 2, 4, 7, 1, 4, 3, 6]
exam_scores = [88.5, 76.0, 91.2, 58.4, 73.6, 95.0, 45.2, 79.8, 61.0, 89.9]

corr = pd.Series(study_hours).corr(pd.Series(exam_scores))
print(f"Correlation between study hours and exam scores: {corr:.2f}")
""")

# ---------------------------------------------------------------
md("""## 4. Data Types & Structures

Real-world datasets mix several kinds of data, each needing different
handling during analysis:

| Type | Example | Handling notes |
|---|---|---|
| **Numerical (continuous/discrete)** | `score`, `age` | Summary stats, scaling |
| **Categorical (nominal)** | `city` | One-hot encoding, mode |
| **Ordinal** | `grade` (A > B > C > D) | Preserve rank order when encoding |
| **Datetime** | `enrollment_date` | Parse to `datetime`, extract features |
| **Text** | `remarks` | Cleaning, tokenization, length/word counts |

The next cells load a small sample dataset and classify each column.
""")
code("""df = pd.read_csv("data/students_sample.csv", parse_dates=["enrollment_date"])
df.head()
""")

code("""df.dtypes
""")

code("""column_type_notes = {
    "student_id": "Numerical (identifier, discrete)",
    "name": "Text",
    "age": "Numerical (discrete)",
    "grade": "Ordinal (A > B > C > D)",
    "city": "Categorical (nominal)",
    "enrollment_date": "Datetime",
    "score": "Numerical (continuous)",
    "remarks": "Text (free-form)",
}
for col, note in column_type_notes.items():
    print(f"{col:16s} -> {note}")
""")

# ---------------------------------------------------------------
md("""## 5. Data Science Best Practices Applied Here

- **Meaningful naming:** variables and functions describe their purpose
  (`descriptive_summary`, `column_type_notes`) instead of generic names.
- **Documentation:** functions include docstrings; markdown cells explain the
  *why* before the *how*.
- **Reproducibility:** the sample dataset ships with this notebook
  (`data/students_sample.csv`) so results are identical on any machine.
- **Responsible interpretation:** correlation is reported without implying
  causation, and the dataset is explicitly a small illustrative sample, not a
  basis for real decisions.
""")

# ---------------------------------------------------------------
md("## 6. Practical Assignments")

md("**Assignment 1 — Sum, Average, and Product of Four Integers**")
code("""def sum_avg_product(a, b, c, d):
    numbers = [a, b, c, d]
    total = sum(numbers)
    average = total / len(numbers)
    product = 1
    for n in numbers:
        product *= n
    return total, average, product

s, avg, prod = sum_avg_product(4, 8, 15, 16)
print(f"Sum={s}, Average={avg}, Product={prod}")
""")

md("**Assignment 2 — Average of Numbers Given as a List**")
code("""def average_of_list(numbers):
    return sum(numbers) / len(numbers)

print("Average:", average_of_list([12, 45, 7, 23, 56, 9]))
""")

md("**Assignment 3 — Exchange Values of Two Variables**")
code("""x, y = 10, 25
print("Before swap:", x, y)
x, y = y, x
print("After swap:", x, y)
""")

md("**Assignment 4 — Print Numbers 1 to 10 (while and for loop)**")
code("""# while loop
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print()

# for loop
for n in range(1, 11):
    print(n, end=" ")
print()
""")

md("**Assignment 5 — Odd-Position Digits of a 5-Digit Number**")
code("""def odd_position_digits(number):
    digits = str(number)
    if len(digits) != 5:
        raise ValueError("Number must have exactly 5 digits")
    # position 1,3,5 (1-indexed) are the "odd positions"
    return [digits[i] for i in range(len(digits)) if (i + 1) % 2 != 0]

print("Odd-position digits of 48291:", odd_position_digits(48291))
""")

md("**Assignment 6 — Binary Search**")
code("""def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [3, 8, 12, 19, 25, 31, 45, 52, 67, 80]
print("Index of 45:", binary_search(numbers, 45))
print("Index of 100:", binary_search(numbers, 100))
""")

md("**Assignment 7 — Concatenate Two Strings and Find Length**")
code("""def concat_and_length(s1, s2):
    combined = s1 + s2
    return combined, len(combined)

combined, length = concat_and_length("DataScience", "Fundamentals")
print(f"Combined: {combined}, Length: {length}")
""")

md("**Assignment 8 — Smallest of Three Numbers**")
code("""def smallest_of_three(a, b, c):
    return min(a, b, c)

print("Smallest:", smallest_of_three(42, 17, 29))
""")

md("**Assignment 9 — Word, Character, Whitespace, and Special-Symbol Count**")
code("""import string

def text_stats(text):
    words = len(text.split())
    chars = len(text)
    whitespace = sum(1 for c in text if c.isspace())
    specials = sum(1 for c in text if not c.isalnum() and not c.isspace())
    return {"words": words, "characters": chars,
            "whitespace": whitespace, "special_symbols": specials}

sample_text = "Data Science is fun, powerful & full of insights!"
text_stats(sample_text)
""")

# ---------------------------------------------------------------
md("""## 7. Conclusion

This notebook covered the six objectives of the Fundamentals Assessment: the
Data Science lifecycle and use cases, core Python programming constructs,
descriptive/probability/correlation statistics, classification of data
types and structures, clean-coding best practices, and a full set of
practical assignments. The accompanying `report.docx` summarizes these
findings for submission.
""")

nb["cells"] = cells

with open("Data_Science_Fundamentals_Assessment.ipynb", "w") as f:
    nbf.write(nb, f)

print("Notebook written.")
