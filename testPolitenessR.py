import politenessr as pr

# Predict a single text
print(pr.predict(["I am totally agree with you"]))

# Predict a list of texts
preds = pr.predict(['I am totally agree with you','I hate you'])
print(preds)
