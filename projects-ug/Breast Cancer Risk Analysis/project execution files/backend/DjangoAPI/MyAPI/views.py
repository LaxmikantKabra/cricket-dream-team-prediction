from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from joblib import dump, load


from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pandas as pd
import numpy as np
import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import Sequential
from keras.layers import Dense
import warnings
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.sequence import pad_sequences
from rest_framework.response import Response
from rest_framework import status

# from .serializers import riskresultSerializers

# class riskresultView(viewsets.ModelViewSet):
#     queryset = riskresult.objects.all()
#     serializer_class = approvalsSerializers


def clean_dataset(df):
        assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
        df.dropna(inplace=True)
        indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
        return df[indices_to_keep].astype(np.float64)


class Risk_Amount(APIView):
    def post(self, request, format=None):
        data=request.data
        data = data['data']
        # data = data['abortion']
        # for i in data :
        #     print(i, data[i])
        # print(data)
        # return Response(data, status=status.HTTP_201_CREATED)


        df = pd.read_csv('D:\Education\Courses\Angular\\finalYear-project-backend\merged_with_missing_values_2removed.csv', na_values='-')
        clean_dataset(df)

        df = df.dropna()
        total = df.isnull().sum().sort_values(ascending=False)
        percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
        missing_data.head(25)
        train = df.drop((missing_data[missing_data['Total'] > 81]).index, 1)

        X = df.drop('\nBenign_malignant_cancer', axis=1)
        y = df['\nBenign_malignant_cancer']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        model = keras.Sequential()
        model.add(layers.Dense(16, activation="relu", kernel_regularizer='l2')),
        tf.keras.layers.Dropout(0.3),

        model.add(layers.Dense(32, activation="relu", kernel_regularizer='l2')),
        tf.keras.layers.Dropout(0.3),

        model.add(layers.Dense(64, activation='relu', kernel_regularizer='l2')),
        tf.keras.layers.Dropout(0.3),

        model.add(layers.Dense(1, activation='sigmoid'))
        # Compiling the ANN
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        model.fit(X_train, y_train,validation_data=(X_test,y_test), batch_size = 32, epochs = 90)

        if (data['gender']) == 'male':
                val1 = 1
        elif(data['gender']) == 'female':
                val1 = 0
        if (data['familyHistory']) == 'yes':
                val2 = 1
        else:
                val2 = 0
        val3 = (int(data['age']))
        val4 = (int(data['weight']))
        if (data['maritalStatus']) == 'yes':
                val5 = 1
        else:
                val5 = 0

        if (int(data['maritalLength'])) <= 10:
                val6 = 0
        else:
                val6 = 1
        if (data['pregnancyExperience']) == 'yes':
                val7 = 1
        else:
                val7 = 0

        val8 = (int(data['numberOfChild']))
        if (int(data['ageFirstChild'])) <= 30 :
                val9 = 0
        else:
                val9 = 1
        if (data['abortion']) == 'yes':
                val10 = 1
        else:
                val10 = 0
        bg=data['bloodGroup']
        if (bg) == 'A+':
                val11 = 0
        elif (bg) == 'A-':
                val11 = 1
        elif (bg) == 'AB+':
                val11 = 2
        elif (bg) == 'AB-':
                val11 = 3
        elif (bg) == 'B+':
                val11 = 4
        elif (bg) == 'B-':
                val11 = 5
        elif (bg) == 'O+':
                val11 = 6
        else:
                val11 = 7
        if (data['bp']) == 'yes':
                val12 = 1
        else:
                val12 = 0
        if (data['smoke']) == 'yes':
                val13 = 1
        else:
                val13 = 0
        if (data['alcohol']) == 'yes':
                val14 = 1
        else:
                val14 = 0
        if (data['breastPain']) == 'yes':
                val15 = 1
        else:
                val15 = 0
        if (data['contraception']) == 'yes':
                val16 = 1
        else:
                val16 = 0
        if (int(data['menstrualAge']) )<= 12:
                val17 = 1
        else:
                val17 = 2
        if (int(data['menopausalAge'])) <= 50:
                val18 = 1
        else :
                val18 = 2

        # dump(model, 'BreastCancerRiskNeuralNet.joblib')

        pred = model.predict([[val1 ,val2 ,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18]])
        # pred = [int(lab) for lab in pred]
        # print(pred)
        pred = [1 if y >= 0.6 else 0 for y in pred]
        result1 = ""
        if pred== 0:
                result1= "You are Not at a Risk"
        else:
                result1="You are at a Risk"

        return Response(result1, status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def sum(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        print("Hello there")
        pass
    elif request.method == 'POST':
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
        print(response_dict)
    return Response(response_dict, status=status.HTTP_201_CREATED)

class Add_Values(APIView):
    def post(self, request, format=None):
        sum = 0
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
        return Response(response_dict, status=status.HTTP_201_CREATED)


# loaded_model = load('BreastCancerRiskNeuralNet.joblib')
