import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

test = False

if test:
    input_file = "test_input.evec"
else:
    input_file = "example.pca.evec"

x = [];
y = [];
with open(input_file, 'r') as file:
    for line in file:
        words = line.split();
        if words[0] == "#eigvals:":
            continue;
        else:
            print("X1: {0}, X2: {1}, Y: {2}".format(words[1], words[2], words[3]))
            values = [float(words[1]), float(words[2])]
            x.append(values);
            y.append(words[3]);

x = np.array(x)
y = np.array(y)
y = y.reshape(y.shape[0], 1)

unique_labels = np.unique(y)
fig = plt.figure(figsize=(8, 6))
for count,i in enumerate(unique_labels):
    rows = y == i;
    rows = rows[:,0]
    plt_t = plt.scatter(
        x[rows,0],
        x[rows,1],
        label=i,
        s = 5.5)
# plt.legend()
plt.grid()
plt.show()
fig.savefig('pca_output.png', dpi=fig.dpi)

print(x.shape, x.dtype)
print(y.shape, y.dtype)
        