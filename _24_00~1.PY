student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

print(student_dict)


for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
'''
{'student': ['Angela', 'James', 'Lily'], 'score': [56, 76, 98]}
['Angela', 'James', 'Lily']
[56, 76, 98]
  student  score
0  Angela     56
1   James     76
2    Lily     98
'''