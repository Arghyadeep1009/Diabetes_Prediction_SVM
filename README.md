# Diabetes_Prediction_SVM
## Diabetes Prediction using SVM

This project implements a Support Vector Machine (SVM) model to predict diabetes using the Pima Indians Diabetes Dataset.

### Getting Started

This project requires the following Python libraries:

* pandas
* numpy
* scikit-learn

You can install them using pip:

pip install pandas numpy scikit-learn

### Running the Script

1. Clone this repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using Python:

python diabetes_prediction.py

This will print the training and test accuracy of the model, along with a sample prediction for a new data point.

### Project Breakdown

The script is divided into the following sections:

1. **Importing Dependencies:** Necessary libraries are imported for data manipulation, model building, and evaluation.
2. **Data Collection and Analysis:**
    * Loads the diabetes dataset into a pandas DataFrame.
    * Explores the data through various methods.
    * Separates features and target variable.
    * Applies standard scaling to normalize the features.
3. **Train Test Split:** Splits data into training and testing sets for model evaluation.
4. **Training the Model:** Trains an SVM classifier with a linear kernel on the training data.
5. **Model Evaluation:** Evaluates the model's accuracy on both training and testing data.
6. **Making a Predictive System:** Demonstrates how to use the trained model to predict diabetes for a new data point.

### Additional Notes

* This is a basic implementation, and exploring different SVM kernels or feature engineering techniques might improve performance.
* For more complex classification tasks, consider using additional evaluation metrics beyond accuracy.
