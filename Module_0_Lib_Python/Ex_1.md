## Bài toán
Cho một mảng số nguyên 1 chiều.  
Yêu cầu:
- In ra **giá trị trung bình** của mảng
- Tìm **phần tử lớn nhất**
- **Đếm số phần tử chẵn** trong mảng

## Code Python
```python
import numpy as np

a = np.array([1, 2, 3, 4, 5])
countEven = np.sum(a % 2 == 0)
print(np.mean(a), np.max(a), countEven)
```