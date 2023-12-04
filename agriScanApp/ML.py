import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



class MLModel:
    def __init__(self, base_folder='D:/finalProject/agriScan/agriScanApp/plantvillage dataset/color'):
        self.base_folder = base_folder
        self.rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
        self.load_and_preprocess_data()
        self.train_model()

    def load_and_preprocess_data(self):
        images = []
        labels = []

        class_folders = os.listdir(self.base_folder)

        for class_folder in class_folders:
            class_path = os.path.join(self.base_folder, class_folder)

            for filename in os.listdir(class_path):
                img_path = os.path.join(class_path, filename)

                # Read the image and resize it (adjust the size as needed)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (150, 150))

                # Extract the label from the class folder
                label = class_folder

                if img is not None:
                    images.append(img.flatten())  # Flatten the image
                    labels.append(label)

        self.X = np.array(images)
        self.y = np.array(labels)

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        self.rf_classifier.fit(X_train, y_train)
        y_pred = self.rf_classifier.predict(X_test)
        self.accuracy = accuracy_score(y_test, y_pred)
    def evaluate_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        y_true = y_test
        y_pred = self.rf_classifier.predict(X_test)
        return y_true, y_pred
       
    def get_accuracy(self):
        return self.accuracy
    def get_accuracy_graph_data(self):
        return ["Random Forest"], [self.accuracy]
