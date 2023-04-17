
def classificator(x, w):
    # zip(x, w) -> [(x_1, w_1), ..., (x_n, w_n)]
    dot_product = [x_i*w_i for x_i, w_i in zip(x, w)]
    print(dot_product)
    res = sum(dot_product)
    
    if res >= 0:
        return True
    else:
        return False

# bank, 1 000 000, best regards
weights = [2, -4, -1]
dataset = [([1, 0, 1], True), 
            ([1, 0, 2], True),
            ([1, 2, 0], False),
            ([0, 1, 1], False),
            ([0, 0, 1], False)]

all_predictions = list()
all_labels = list()
for features, label in dataset:
    print(f"Features: {features}")
    print(f"Label: {label}")
    prediction = classificator(features, weights)
    all_predictions.append(prediction)    
    all_labels.append(label)

num_correct = 0
num_instances = len(all_predictions)
for prediction, label in zip(all_predictions, all_labels):
    if prediction == label:
        num_correct += 1

accuracy = num_correct / num_instances
print(f"Accuracy: {accuracy}")
