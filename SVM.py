import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import NuSVC

class SVM():
    def __init__(self,train_path,test_path):
        #initialize train and test datasets
        self.input_train, self.target_train, self.input_test, self.target_test = self.train_test_prep(train_path,test_path)
        self.SVM_classifier = None



    def train_test_prep(self,train_path,test_path):
        df_train = pd.read_csv(train_path)
        input_train = df_train.drop('LABELS', axis='columns')
        target_train = df_train['LABELS']

        df_test = pd.read_csv(test_path)
        input_test = df_test.drop('LABELS', axis='columns')
        target_test = df_test['LABELS']

        return input_train,target_train,input_test,target_test

    def SVM_trainer(self):
        self.SVM_classifier = svm.SVC()
        self.SVM_classifier.fit(self.input_train,self.target_train)

    def SVM_test(self):
        target_pred_test = self.SVM_classifier.predict(self.input_test)
        accuracy_score(self.target_test, target_pred_test)
        return target_pred_test

    def plot_result(self,target_pred_test):
        print("Accraucy of model ::", accuracy_score(self.target_test, target_pred_test))
        print(classification_report(self.target_test, target_pred_test))
        # Get and reshape confusion matrix data
        matrix = confusion_matrix(self.target_test, target_pred_test)
        matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]

        # Build the plot
        plt.figure(figsize=(16, 7))
        sns.set(font_scale=1.4)
        sns.heatmap(matrix, annot=True, annot_kws={'size': 15},
                    cmap=plt.cm.Blues, linewidths=0.2)

        # Add labels to the plot
        class_names = ['1', '2', '3',
                       '4', '5', '6']
        tick_marks = np.arange(len(class_names))
        tick_marks2 = tick_marks + 0.5
        plt.xticks(tick_marks, class_names, rotation=25)
        plt.yticks(tick_marks2, class_names, rotation=0)
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        plt.title('Confusion Matrix for Support Vector Machine (SVM)')
        plt.show()

class NuSVM():
    def __init__(self,train_path,test_path):
        #initialize train and test datasets
        self.input_train, self.target_train, self.input_test, self.target_test = self.train_test_prep(train_path,test_path)
        self.SVM_classifier = None



    def train_test_prep(self,train_path,test_path):
        df_train = pd.read_csv(train_path)
        input_train = df_train.drop('LABELS', axis='columns')
        target_train = df_train['LABELS']

        df_test = pd.read_csv(test_path)
        input_test = df_test.drop('LABELS', axis='columns')
        target_test = df_test['LABELS']

        return input_train,target_train,input_test,target_test

    def SVM_trainer(self):
        self.SVM_classifier = make_pipeline(StandardScaler(), NuSVC(degree=6))
        self.SVM_classifier.fit(self.input_train,self.target_train)

    def SVM_test(self):
        target_pred_test = self.SVM_classifier.predict(self.input_test)
        accuracy_score(self.target_test, target_pred_test)
        return target_pred_test

    def plot_result(self,target_pred_test):
        print(classification_report(self.target_test, target_pred_test))
        # Get and reshape confusion matrix data
        matrix = confusion_matrix(self.target_test, target_pred_test)
        matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]

        # Build the plot
        plt.figure(figsize=(16, 7))
        sns.set(font_scale=1.4)
        sns.heatmap(matrix, annot=True, annot_kws={'size': 15},
                    cmap=plt.cm.Blues, linewidths=0.2)

        # Add labels to the plot
        class_names = ['1', '2', '3',
                       '4', '5', '6']
        tick_marks = np.arange(len(class_names))
        tick_marks2 = tick_marks + 0.5
        plt.xticks(tick_marks, class_names, rotation=25)
        plt.yticks(tick_marks2, class_names, rotation=0)
        plt.xlabel('Predicted label')
        plt.ylabel('True label')
        plt.title('Confusion Matrix for Nu Support Vector Machine (NuSVM)')
        plt.show()