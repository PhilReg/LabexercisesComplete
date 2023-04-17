import numpy as np

def classificator(x, w):
    dot_product = np.dot(x, w)    
    
    if dot_product >= 0:
        return True
    else:
        return False

# bank, 1 000 000, best regards
weights = np.array([2, 0, -1])
dataset = [([1, 0, 1], True), 
            ([1, 0, 2], True),
            ([1, 2, 0], False),
            ([0, 1, 1], False),
            ([0, 0, 1], False)]

all_predictions = list()
all_labels = list()

for features, label in dataset:
    prediction = classificator(np.array(features), weights)
    all_predictions.append(prediction)    
    all_labels.append(label)

is_equal = np.equal(all_predictions, all_labels)
# is_equal = np.array(all_predictions) == np.array(all_labels)
print(is_equal)
accuracy = np.mean(is_equal)

print(f"Accuracy: {accuracy}")
