# CS645-Project

Extracting Top-K Insights from Multi-dimensional Data

##To setup

You need to install Postgresql, then run the `setup.sql` to create the datasets for different questions.

We didn't upload the original dblp dataset because of size limitation, please make sure the dblp csv files are in the same folder with the `setup.sql`.

## Run the code

First you should open the `insight_helper` file,  at the top you will see several lines of code for import the domain of every dimension. Here we need to set different domain values according to different question numbers. We set the first question by default. If you want to test questions 2-5 , Please comment the relevant code of the first question, and then uncomment the relevant question code.

Moreover, you need to change the value of `total_tuples`, it should be the size of corresponding dataset. For example, the size of dataset1 for the question1, we already generated dataset1-5 for our five questions in the previous step. Since we generate datasets by randomly choose some data, so the dataset size will be different when you everytime setup the dataset, we can't set `total_tuples` in advance for you.

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



