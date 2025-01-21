import tensorflow as tf
from tensorflow.keras import layers, models
from utils import load_images_from_pdf

pdf_path = "D:/Handwritten_Text_OCR/data/Kaggle/new.pdf"
model_save_path = "D:/Handwritten_Text_OCR/models/ocr_model.h5"

print("Loading and preprocessing data...")
X = load_images_from_pdf(pdf_path)
y = []

vocab = sorted(set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "))
vocab_size = len(vocab) + 1
char_to_idx = {char: idx for idx, char in enumerate(vocab)}

def build_ocr_model(img_size=(128, 32), vocab_size=100):
    input_img = layers.Input(shape=(img_size[1], img_size[0], 1), name="image_input")
    x = layers.Conv2D(32, (3, 3), activation="relu", padding="same")(input_img)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Conv2D(64, (3, 3), activation="relu", padding="same")(x)
    x = layers.MaxPooling2D((2, 2))(x)
    x = layers.Reshape(target_shape=(-1, 64))(x)
    x = layers.Bidirectional(layers.LSTM(128, return_sequences=True))(x)
    x = layers.Dense(vocab_size, activation="softmax")(x)
    model = models.Model(inputs=input_img, outputs=x)
    return model

def ctc_loss_function(y_true, y_pred):
    batch_size = tf.shape(y_pred)[0]
    input_length = tf.fill([batch_size], tf.shape(y_pred)[1])
    label_length = tf.reduce_sum(tf.ones_like(y_true.indices[:, 1]), axis=0)
    return tf.reduce_mean(tf.nn.ctc_loss(
        labels=tf.cast(y_true, tf.int32),
        logits=y_pred,
        label_length=tf.cast(label_length, tf.int32),
        logit_length=tf.cast(input_length, tf.int32),
        logits_time_major=False,
        blank_index=-1
    ))

model = build_ocr_model(vocab_size=vocab_size)
model.compile(optimizer="adam", loss=ctc_loss_function)

print("Starting model training...")
model.fit(X, y, batch_size=3, epochs=10, validation_split=0.2)

print("Saving the trained model...")
model.save(model_save_path)
print("Model saved successfully!")
