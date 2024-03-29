import tensorflow as tf


def multi_layer_perception(dataset_name, input_shape=(28,28), activation='relu'):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=input_shape),
        tf.keras.layers.Dense(256, activation=activation),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(class_number, activation='softmax')
    ])
    return model

def resNet50(dataset_name, input_shape=(32,32,3)):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.applications.ResNet50(
            include_top=False,
            weights=None,
            input_tensor=None,
            input_shape=input_shape,
            pooling="avg",
            classes=class_number,
        )
    return model


def alexnet(dataset_name, shape):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    input_layer = tf.keras.layers.Input(shape)

    x = tf.keras.layers.Conv2D(filters=96, kernel_size=[3,3], strides=[1,1], padding='same')(
        input_layer)
    x = tf.keras.layers.LayerNormalization()(x)
    x = tf.keras.layers.Conv2D(filters=256, kernel_size=[3,3], padding='same')(x)
    x = tf.keras.layers.LayerNormalization()(x)
    x = tf.keras.layers.MaxPool2D(pool_size=(3, 3), strides=[2, 2], padding='same')(x)

    x = tf.keras.layers.Conv2D(filters=384, kernel_size=[3, 3], padding='same')(x)
    x = tf.keras.layers.Conv2D(filters=384, kernel_size=[3, 3], padding='same')(x)
    x = tf.keras.layers.Conv2D(filters=256, kernel_size=[3, 3], padding='same')(x)

    x = tf.keras.layers.MaxPool2D(pool_size=(3, 3), strides=[2, 2], padding='same')(x)

    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(units=class_number, activation='softmax')(x)

    model = tf.keras.models.Model(inputs=input_layer, outputs=x)
    return model

def resNet50V2(dataset_name, input_shape=(32,32,3)):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.applications.ResNet50V2(
            include_top=False,
            weights=None,
            input_tensor=None,
            input_shape=input_shape,
            pooling="avg",
            classes=class_number,
            classifier_activation="softmax",
        )
    return model

def MobileNet(dataset_name, input_shape=(32,32,3)):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.applications.MobileNet(
            input_shape=input_shape,
            alpha=1.0,
            depth_multiplier=1,
            dropout=0.001,
            include_top=False,
            weights=None,
            input_tensor=None,
            pooling="avg",
            classes=class_number,
            classifier_activation="softmax",
        )
    return model


def MobileNetV2(dataset_name, input_shape=(32,32,3)):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.applications.MobileNetV2(
            input_shape=input_shape,
            alpha=1.0,
            include_top=False,
            weights=None,
            input_tensor=None,
            pooling="avg",
            classes=class_number,
            classifier_activation="softmax",
        )
    return model


def DenseNet121(dataset_name, input_shape=(32,32,3)):
    from Data import get_class_num
    class_number = get_class_num(dataset_name)
    model = tf.keras.applications.DenseNet121(
            include_top=False,
            weights=None,
            input_tensor=None,
            input_shape=input_shape,
            pooling="avg",
            classes=class_number,
        )
    return model