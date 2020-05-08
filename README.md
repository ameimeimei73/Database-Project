# CS645-Project

Extracting Top-K Insights from Multi-dimensional Data

##To setup

We deployed our project on google cloud to improve our computation ability. please follow the following two toturials to set up google cloud and set up PostgreSQL on google cloud vm instance and transfer relative files from local to your instance.

https://compsci682-fa18.github.io/gce-tutorial/

https://cloud.google.com/community/tutorials/setting-up-postgres

You need to install Postgresql, then run the `setup.sql` to create the datasets for different questions.

We didn't upload the original dblp dataset because of size limitation, please make sure the dblp csv files are in the same folder with the `setup.sql`.

After the setup.sql finished, please copy the output csv files to the directory where main.py located. The csv files include "venueid_1.csv", "venueyear_1.csv", "authorid_2.csv", "venueyear_2.csv", "authorid_3.csv", "venueyear_3.sql", "venueyear_4.sql", and "venueyear_5.sql".

## Run the code

First you should open the `insight_helper` file,  at the top you will see several lines of code for import the domain of every dimension. Here we need to set different domain values according to different question numbers. We set the first question by default. If you want to test questions 2-5 , Please comment the relevant code of the first question, and then uncomment the relevant question code.

Moreover, you need to change the value of `total_tuples`, it should be the size of corresponding dataset (dataset1, dataset2,...,dataset5). For example, the size of dataset1 for the question1, we already generated dataset1-5 for our five questions in the previous step. Since we generate datasets by randomly choose some data, so the dataset size will be different when you everytime setup the dataset, we can't set `total_tuples` in advance for you.

Finally, in `Extractor.py`pass correct parameters to the connect function to connect postgresql database. Here is an example what is our parameters looks like. All of the parameters are set when you create your postgres database.

connection = psycopg2.connect(user="postgres", password="123456", host="localhost", port="5432", database="cs645")


Then you can run the following command: 

```
python main.py R tau k
```

Parameter 1: R is the question number of the question you want to test (5 for the extension question).

Parameter 2: tau is the depth parameter.

Parameter 3: k is the number of insights you want to obtain.

The result should looks like:

```
[ (0.851199658777641, [['*', '*'], 1, (-1,), 2])]
 (0.2274903126520635, [['networks', '*'], 1, (-1,), 2]),
(0.18023308362662654, [['systems', '*'], 1, (-1,), 2]),
 (0.13722921482954537, [['data', '*'], 1, (-1,), 2]),
 (0.1022779088632658, [['algorithm', '*'], 1, (-1,), 2]),
(0.09577032994097821, [['learning', '*'], 1, (-1,), 2])
 (0.05866120819098794, [['mobile', '*'], 1, (-1,), 2]),
 (0.05696472947194629, [['distributed', '*'], 1, (-1,), 2]),
(0.0381410071039586, [['web', '*'], 1, (-1,), 2]),
 (0.01559808550797058, [['neural', '*'], 1, (-1,), 2])]
```

Means:

![image-20200508021154207](/Users/lichenmei/Library/Application Support/typora-user-images/image-20200508021154207.png)



