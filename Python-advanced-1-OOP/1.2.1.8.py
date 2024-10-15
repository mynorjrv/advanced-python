import random

class apples_process:
    n_apples_processed = 0
    weight_processed = 0
    
    def __init__(self, weight):
        self.weight = weight
        apples_process.n_apples_processed += 1
        apples_process.weight_processed += self.weight
        
class apple(apples_process):
    def __init__(self, weight):
        super().__init__(weight)
        
while True:
    if (apples_process.weight_processed>300
        or apples_process.n_apples_processed>1000):
        # Start the if
        break
    
    ap = apple(random.uniform(0.2, 0.5))
    
    
print(
    apples_process.n_apples_processed, 
    apples_process.weight_processed
)
    
    