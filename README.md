# 💵 Image Recognition Model
## Project Overview  
In this project, I trained a convolutional neural network (CNN) to classify various types of currency. The model was built using the `tensorflow` library with the built-in `tf.keras` API. This is a simplified version of a deep learning model and comes with limitations, including a relatively small dataset (~100 images per class), which leads to overfitting and reduced generalization performance.

### Data Source
The dataset used for model training was created by the author. It consists of 5 currency types(5 classes), each of one has ~100 images for model training, ~10 images for model testing and validation.   

### Tools
* Jupyter Notebook
   * tensorflow - used to train, test, and build the model
   * tf.keras -  define and compile the model
   * model.save - saving trained model in .keras format
* Visual Studio Code (VSC) – test the model on a local server
  
## Deep Learning Model
### Building Model
The model was built using the `tensorflow` library and its high-level `tf.keras` API. The dataset was loaded using `tf.keras.utils.image_dataset_from_directory`- it loads images from directories and assigns labels based on the folder names. In the next step, I used the `sequential` class, which was helpful for building my simple, linear model. It allowed me to add layers one by one and train the model on images from start to finish.

### Measure Model Accuracy


### Results  

