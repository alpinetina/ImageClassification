import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam

MODEL_PATH = "model.h5"

def build_model(num_classes):
    base_model = ResNet50(weights='imagenet', include_top=False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    for layer in base_model.layers:
        layer.trainable = False
    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(data_dir, epochs=3):
    datagen = ImageDataGenerator(preprocessing_function=preprocess_input, validation_split=0.2)
    train_gen = datagen.flow_from_directory(data_dir, target_size=(224, 224),
                                            batch_size=16, class_mode='categorical',
                                            subset='training')
    val_gen = datagen.flow_from_directory(data_dir, target_size=(224, 224),
                                          batch_size=16, class_mode='categorical',
                                          subset='validation')
    model = build_model(num_classes=len(train_gen.class_indices))
    model.fit(train_gen, validation_data=val_gen, epochs=epochs)
    model.save(MODEL_PATH)
    return list(train_gen.class_indices.keys())

def predict_image(img_path, labels):
    model = tf.keras.models.load_model(MODEL_PATH)
    img = load_img(img_path, target_size=(224, 224))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return labels[np.argmax(preds)]