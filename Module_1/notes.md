# Module 1: Python
## Activation Function

**Viết hàm tính độ đo F1-Score thường được sử dụng để đánh
giá mô hình phân loại.**


```python
def evaluate_f1_components(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int') 
        return
    if not isinstance(fp, int):
        print('fp must be int') 
        return
    if not isinstance(fn, int):
        print('fn must be int') 
        return    
    
    if tp < 0 or fp < 0 or fn < 0:
        print("tp and fp and fn must be greater or equal zero")
        return
    if (tp + fp) == 0 or (tp+fn) == 0:
        print("div for zero")
        return
          
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    if (precision + recall == 0):
        print('div for zero')
        return
    f1_score = 2 * ((precision * recall) / (precision + recall)) 
    
    print('precision is', precision)
    print('recall is', recall)
    print('f1_score is', f1_score)
    
    return precision, recall, f1_score 

       
evaluate_f1_components(3,3,3)
# evaluate_f1_components(2,3,4)
```

## Note
- Positive( P - Dương tính) 
- Negative( N - Âm tính)
- True/False Positive/Negative

## 2. Viết hàm tính giá trị cho các hàm số kích hoạt.
**Sigmoid Function**
- Là một trong những hàm kích hoạt cơ bản nhất trong machine learning và neural networks.
- Ưu Điểm:
    + Dễ hiểu và triển khai: trong mạng neuron.
    + Đầu ra nằm trong khoảng [0,1].
- Nhược điểm 
    + Vanishing gradient problem:  Khi đầu vào có giá trị lớn hoặc nhỏ, đạo hàm của Sigmoid tiệm cận đến 0, dẫn đến vấn đề vanishing gradient, làm chậm quá trình học của mạng.