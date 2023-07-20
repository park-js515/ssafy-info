y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

S = 0

for i in range(4):
    S += (y_true[i] - y_pred[i]) ** 2;

print(S/4)