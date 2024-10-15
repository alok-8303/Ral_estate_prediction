# Real Estate Price Prediction
It is difficult to have a precise idea of the  price of house before buying ,so to save your time from visiting a lot of houses and then getting to know their prices use this model to predict the price of the house based on its features.

# What is the Project about?
It is a web-app that makes use of Machine learning inorder to determine the price of he house based on its features.

# What did we use to build it? 
The primary language for modeling and data analysis was Python. We made use of Sci-Kit learn library in order to make our model which is a linear regression model. For deployment we used Gradio Framework.


# About the Data-set
I used a data set off of Kaggle. It contained data of real houses and their features like distance to nearest market , latitude ,longitude etc.

# How was the project built?
1. I started off by getting the data from Kaggle and used the Kaggle notebooks to  create the model. After importing the data i looked at the different columns in our data. <br>
2. Once i had my columns, i split the data into training and testing set using the train-test split and made my Linear Regression model using the Sci-Kit learn Library. <br>
3. Once the model was ready, i put it in a pickle file. <br>
4. I then shifted to Colab Notebook where i deployed the model on web  using Gradio. The front end of the Web app was all made using Gradiot . <br>
5. In the end i tested the web app with the inputs from the test set that we created and the model gave results very close to the results we had in our original data. <br>

# Conclusion
The model was able to make some very good predictions. The model accuracy was somewhere around 94-95% which is quite decent and even on the data which the model had never seen before, it was able to make some good predictions.

# How to run 
To run this web app just open a collab note book and run these command-

!pip install gradio 
and copy rest of the code from app.py file also upload the model.sav file to notebook and replace its path in the code.
