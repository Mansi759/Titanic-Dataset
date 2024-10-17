# importing the libraries

import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

data= pd.read_csv("titanic.csv") # storing the data set in data variable ....

data["Age"]=data["Age"].fillna(method="ffill")## filling the null values in age column
data["Age"]=data["Age"].astype(int) # changing the data type of age column

data.drop(["PassengerId","Name","SibSp","Parch","Ticket","Fare","Cabin"],axis=1,inplace =True )# Dropping the invalid columns 

# drooping the duplicate values
data.drop_duplicates(inplace=True)

##sidebar

st.sidebar.header("Explore Insights :")
choice = st.sidebar.selectbox("Select a insight to explore :", options=
                              ["Survival Rate by Class","Survival rate by Age",
                               "Survival rate by Sex","Survival Rate by Embraked","Age distribution by class",
                                "Class distribution by embarked","Class distribution by Gender"])

## survial rate by class

if choice == "Survival Rate by Class":
    ax=sns.barplot(data=data,y="Survived",x="Pclass",errorbar=None)
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.2f}",(p.get_x()+p.get_width()/2.,p.get_height()),
                ha="center",va="baseline",fontsize=10,color="black",xytext=(0,5),textcoords='offset points')
    plt.title("Survival Rate by Passenger Class..",size=22,color="orange")
    plt.ylabel("Survival Rate",size=14,color="g")
    plt.xlabel("Passenger Class",size=14,color="g")
    plt.show()   
    st.pyplot(plt)
    st.header("Conclusion :....")
    st.write("Passenger class 1 has a the highest survival rate of 0.49")
    st.write("Passenger Class 3 has the second highest survival rate of 0.41")
    st.write("Passenger class 2 has the lowest survival rate of 0.35")
    
## survival rate by age....
    
    
if choice == "Survival rate by Age":
    sns.boxplot(data=data,x="Survived",y="Age",palette="Paired")
    plt.title("Survival rate by Age",size=18,color="orange")
    plt.xlabel("Survived",size=15,color="g")
    plt.ylabel("Age",size=15,color="g")
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :....")
    st.subheader("Not survived :")
    st.write("1.Maximum age of not survived people is: 68")
    st.write("2.The minimum age for individuals who do not survive is considered to be 0, which refers to infants or newborns.")
    st.write("3.The 50% of not-survived rate is observed in individuals aged between 22 and 43 years.")
    
    st.subheader("Survived :")
    st.write("1.Maximum age of survived people is: 74")
    st.write("2.The minimum age for individuals who survive is considered to be 0, which refers to infants or newborns.")
    st.write("3.The 50% survived rate is observed in individuals aged between 19 and 40 years.")
    
## survival rate by sex....
    
    
if choice == "Survival rate by Sex":
    sns.countplot(data=data,x="Survived",hue="Sex",palette="Paired")
    plt.title("Survival rate by Sex",size=18,color="orange")
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion :....")
    st.write("The number of males who did not survive the Titanic disaster is: 145.")
    st.write("The number of females who survived the Titanic disaster is: 109.")
    st.write("Thus, the survival rate of females is higher than that of males.")
    
## survival rate by embarked....
    
if choice =="Survival Rate by Embraked":
    sns.countplot(data=data,x="Survived",hue="Embarked",palette="Paired")
    plt.title("Survival rate by Embarked ",size=18,color="orange")
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion:...")
    st.subheader("Not survived...")
    st.write("The total number of individuals who departed from Queenstown was 19.")
    st.write("The total number of individuals who departed from Southampton was 82.")
    st.write("The total number of individuals who departed from Cherbourg was 48.")
   
    st.subheader("Survived...")
    st.write("The total number of individuals who departed from Queenstown was 14.")
    st.write("The total number of individuals who departed from Southampton was 60.")
    st.write("The total number of individuals who departed from Cherbourg was 30.")
    
## age distribution by class
   
    
if choice == "Age distribution by class":
    sns.barplot(data=data,y="Age",hue="Pclass",palette="Paired")
    plt.title("Age Distribution by Passenger class",size=18,color="orange")
    plt.ylabel("Age",size=16,color="g")
    plt.xlabel("Passenger Class",size=16,color="g")
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion...")
    st.subheader("Class 1")
    st.write("Class 1 consists of individuals whose ages range from 0 to 40 years.")
    st.subheader("Class 2")
    st.write("Class 2 consists of individuals whose ages range from 0 to 30 years.")
    st.subheader("Class 3")
    st.write("Class 3 consists of individuals whose ages range from 0 to 28 years.")
    st.subheader("The highest age recorded among individuals was observed in Class 1.")
    
    
## class distribution by embarked
    
if choice == "Class distribution by embarked":
    sns.countplot(data=data,x="Pclass",hue="Embarked",palette="Paired")
    plt.title("Class distribution by Embaked",size=18,color="orange")
    plt.ylabel("Count",size=16,color="g")
    plt.xlabel("Passenger Class",size=16,color="g")
    plt.show() 
    st.pyplot(plt)
    st.header("Conclusion....")
    st.subheader("Class 1")
    st.write("The total number of individuals who embarked from Southampton is 38.")
    st.write("The total number of individuals who embarked from Cherbourg is 43.")
    st.write("The total number of individuals who embarked from Queenstown is 2.")
    
    st.subheader("Class 2")
    st.write("The total number of individuals who embarked from Southampton is 49.")
    st.write("The total number of individuals who embarked from Cherbourg is 10.")
    st.write("The total number of individuals who embarked from Queenstown is 5.")
    
    st.subheader("Class 3")
    st.write("The total number of individuals who embarked from Southampton is 60.")
    st.write("The total number of individuals who embarked from Cherbourg is 25.")
    st.write("The total number of individuals who embarked from Queenstown is 28.")
    
    st.subheader("The highest number of individuals who embarked from Southampton belongs to class 3")
    
    
## Class distribution by Gender
    
if choice=="Class distribution by Gender":
    sns.countplot(data=data,x="Pclass",hue="Sex",palette="Paired")
    plt.title("Class Distribution by Gender ",size=16,color="orange")
    plt.xlabel("Passenger Class",size=14,color="g")
    plt.ylabel("Count",size=14,color="g")
    plt.show()
    st.pyplot(plt)
    st.header("Conclusion...")
    st.subheader("Class 1")
    st.write("The class 1 consists of 42 male students.")
    st.write("The class 1 consists of 40 female students.")
    
    st.subheader("Class 2")
    st.write("The class 1 consists of 40 male students.")
    st.write("The class 1 consists of 20 female students.")
    
    st.subheader("Class 3")
    st.write("The class 1 consists of 68 male students.")
    st.write("The class 1 consists of 50 female students.")
    
    st.subheader("Thus, class 3 had the maximum male and female passengers..")
        
        

    

    
    

