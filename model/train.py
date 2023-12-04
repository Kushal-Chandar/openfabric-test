import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv("/mnt/data/science_questions_dataset.csv")

tokenizer = Tokenizer(num_words=1000, oov_token='<OOV>')
tokenizer.fit_on_texts(df['question'])
sequences = tokenizer.texts_to_sequences(df['question'])
padded = pad_sequences(sequences, maxlen=20, padding='post', truncating='post')

label_encoder = LabelEncoder()
numeric_labels = label_encoder.fit_transform(df['category'])
categorical_labels = to_categorical(numeric_labels)

model = Sequential([
    Embedding(1000, 16, input_length=20),
    GlobalAveragePooling1D(),
    Dense(24, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(padded, categorical_labels, epochs=30)

model.save("/mnt/data/science_chatbot_model")
