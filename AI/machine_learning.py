import tensorflow as tf
from tensorflow.keras import layers, Model

class MachineLearning:
    def __init__(self):
        pass

    def build_mastermind_model(self, colors=6, pins=4, turns=8, hidden_dim=256):
        input_dim = turns * (pins + 2)

        inputs = layers.Input(shape=(input_dim,))

        x = layers.Dense(hidden_dim, activation="relu")(inputs)
        x = layers.Dense(hidden_dim, activation="relu")(x)

        outputs = []
        for i in range(pins):
            outputs.append(layers.Dense(colors, activation="softmax", name=f"pin_{i}")(x))

        model = Model(inputs=inputs, outputs=outputs)
        model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"] * pins
        )
        return model