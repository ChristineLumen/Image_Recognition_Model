import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from tensorflow.keras.utils import img_to_array
import streamlit as st
from PIL import Image
import numpy as np
st.header("Image Classification Model")
data_cat = ['British Pound (GBP)',
 'Canadian Dollar (CAD)',
 'Dollar (USD)',
 'Euro(EUR)',
 'Japanese Yen (JPY)']
img_height =180
img_width=180
model = load_model("/Users/christinelumen/Python/Currency_classify.keras")
image_name = st.text_input("Enter Image name", "euro.jpeg")

img_path = f"/Users/christinelumen/Python/Image_Classification_Currency/{image_name}"
img = Image.open(img_path).resize((180, 180))

img_arr = img_to_array(img)
img_bat = np.expand_dims(img_arr, axis=0)

predict = model.predict(img_bat)

score =tf.nn.softmax(predict)
st.image(img, caption=f"Input: {image_name}")
st.write("Currency in image is {} with accuracy of {:0.2f}%".format(
        data_cat[np.argmax(score)], np.max(score) * 100))