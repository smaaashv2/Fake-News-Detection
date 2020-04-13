# -*- coding: utf-8 -*-
"""Text_Explicit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UKf7odoO3f_zCibg-06oCx2gUr2o-vGA
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.14

#importing libraries

from numpy import array
from numpy import asarray
from numpy import zeros
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten, BatchNormalization
from keras.layers import Embedding, Dropout, Conv1D, MaxPooling1D
import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv('drive/My Drive/The_Research/all_data_refined.csv')
a = df[df.columns[8: 14]]
# b,c,d,e,f,g = df['word_count',	'average_word_count',	'exclamation_count',	'capital_count', 'question_count', 'negation_count'] #Change this accordingly
print(a)
#load the labels


type = df['type'] #Change this accordingly
labels = []

for types in type:
  if types == 'real':
    labels.append(1)
  elif types == 'fake':
    labels.append(0)



# define model
model = Sequential()
model.add(Dense(31, input_shape=(6, )))
model.add(Dense(128))
model.add(BatchNormalization())
model.add(Dropout(0.8))
model.add(Dense(128, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(128))
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))


# compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# summarize the model
print("____________________")
print(model.summary())
print("____________________")

X_train, X_test, y_train, y_test = train_test_split(a, labels, test_size=0.33)

# fit the model
model.fit(X_train, y_train, epochs=5, verbose=1)


# evaluate the model
print("____________________")
loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
print('Accuracy: %f' % (accuracy*100))

count_true = 0
print("____________________")
output = model.predict(a[:100])
for i in range(len(output)):
  if(output[i] > 0.5 and labels[i] == 1): count_true += 1


print(count_true)

# save the model
model.save('textexplicit.h5')

