def weighted_accuracy(y_true, y_pred):
    total = 0
    correct = 0
    for t, p in zip(y_true, y_pred):
        weight = 2 if t == 1 else 1
        total += weight
        if t == p:
            correct += weight
    return correct / total
