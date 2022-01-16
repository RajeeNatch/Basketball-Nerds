# Basketball-Nerds

Welcome to Basketball Nerds, a dashboard for fans who and to compare the numbers. Thanks to the Balldontlie API, we were able to generate statistics for players, games and seasons over the course of 30 years. 
![lebron_scoring](https://user-images.githubusercontent.com/77027814/149636289-c95090f4-00eb-4ee3-9c4c-606c13622ba2.gif)

## ETL
![etl-process-diagram](https://user-images.githubusercontent.com/77027814/149636493-c7b4ef8c-ef6d-40ff-9421-c94ced823ef1.png)

The team extracted the data from the api, cleaned it by changing column names, ridding collumns and creating dataframes. 
We then created a connnection to Postgresql and loaded dataframes. 
Scripted queries to match out tables and boom the data was loaded directly to the data base. 
No need for you to go through all of the trouble. In out data file, we've included CSVs and our SQL queries.  

## The DASHboard

We used plotly and dash with in our flask file to configure the charts and tables. We also used HTML, CSS, and Javascript to style the elements on each page. 

### Home Tab:

<img width="633" alt="Screen Shot 2022-01-15 at 6 32 52 PM" src="https://user-images.githubusercontent.com/77027814/149641092-39549396-8221-49c8-b100-9666eee79407.png">


### Players Tab:
<img width="577" alt="Screen Shot 2022-01-15 at 6 34 05 PM" src="https://user-images.githubusercontent.com/77027814/149641111-fc1cff3d-f32e-402a-9ed9-5587aa1f2448.png">

<img width="589" alt="Screen Shot 2022-01-15 at 6 34 19 PM" src="https://user-images.githubusercontent.com/77027814/149641120-47566cd6-e7f4-4718-8128-424ddaa2bda4.png">




### Schedule Tab: 



## Running the script

Once you've loaded the data and created a virtual enviorment, make sure to install all the requirements.txt file 
Run python app.py in your terminal and open the browser address that it instructs. 

## Authors
Rajeswari Natchiappan,
Alexander Lorin,
Ra Ish Andrews
