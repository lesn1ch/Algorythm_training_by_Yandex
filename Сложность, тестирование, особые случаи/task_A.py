p, v = (int(i) for i in input().split())
q, m = (int(i) for i in input().split())

if p + v < q - m or p - v > q + m:
    print(2*m + 1 + 2*v + 1)    
else:
    min_val = q - m if p - v >= q - m else p - v
    max_val = p + v if p + v >= q + m else q + m
        
    print(max_val - min_val + 1)