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
- Hình dạng của nó giống như chữ "S". Sigmoid chuyển đổi mọi giá trị đầu vào thành một giá trị đầu ra nằm trong khoảng 0 và 1.
```python
def sigmoid(x):
    return 1 / (1 + (math.e)**(-x))
```

**ReLu Function**
- Rectified Linear Unit:  nếu đầu vào là số âm, hàm sẽ trả về giá trị 0, còn nếu đầu vào là số dương, hàm sẽ trả về chính giá trị đó.
```python
def reLU(x):
    if (x >=0):
        return x
    return 0
```

**ELU Function**
- Exponential Linear Unit: giảm thiểu vấn đề vanishing
gradient ở các giá trị âm, đồng thời vẫn duy trì tính phi tuyến cần
thiết cho quá trình học sâu.
```python
def ELU(x):
    a = 0.01
    if x <= 0:
        return a*((math.e)**x - 1)
    return x
```
