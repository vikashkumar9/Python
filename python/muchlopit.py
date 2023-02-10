import numpy as np
import matplotlib.pyplot as plt

input_table = np.array([
    [0,0], [0,1], [1,0], [1,1]])

weights = np.array([1,1])
print(f'weights: {weights}')

dot_products = input_table @ weights
print(f'Dot products: {dot_products}')

def linear_threshold_gate(dot: int, T: float) -> int:
    '''Returns the binary threshold output'''
    if dot >= T:
        return 1
    else:
        return 0
T = 1
for i in range(0,4):
    activation = linear_threshold_gate(dot_products[i], T)
    print(f'Activation: {activation}')


plt.scatter(input_table,)
plt.show()
