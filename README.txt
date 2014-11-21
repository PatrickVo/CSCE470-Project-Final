For the Algorithm Datacheck point - We separated the yelp review data into 5 json files grouping reviews by star ratings. 
Reviews in the json files have also been removed of stop words and stemmed. You can check our makejson.py file on how we did this. 
These json files make it easier/faster for us to run our algorithm on the data to find similarities. 
Currently we are only reading the first thousand from each json file, To run our code here are 3 easy steps. 

1. Download the Github files.
2. The only files required are the star json files and the algorithm.py located in the APP folder.
3. Then run the algorithm.py located inside the APP folder. 
	
If time permits, we are planning to add more to the algorithm part later. 
So far our core algorithm mainly consists of cosine similarity.
We would like to add the language model method and classification method to the star rating calculation to make the star rating prediction more accurate.
