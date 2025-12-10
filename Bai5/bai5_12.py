# Nguyễn Duy Hiếu; Msv: 245752021610054
import numpy as np
# Dữ liệu đầu 
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])
# sắp xếp chiều cao, nếu chiều cao bằng nhau thì xét ID 
indices = np.lexsort((student_id, student_height)) 
print("chỉ số:")
print(indices)
print("\nDữ liệu sắp xếp:")
for i in indices:
    print(f"{student_id[i]:>5} {student_height[i]:>6}")
