# Anylysis of an Election Audit Using Python:  is it successful and can it be automated

## Project and Purpose Overview:
Determining the winner of any US election is a large task.  A great deal of information is collected and processed as quickly as possible.  A recent Colorade US Congressional Precinct, for example, had a turnout of almost 370,000 voters.  Historically this information is analyzed in Excel.  While this is functional, there may be other options that can better handle large amounts of data and that can be automated to save time and increase accuracy.  

The purpose of this project is to determine if Python can successfully generate the information needed to determine the winner of an election, generate other information that is useful to the Election Board, and can it be automated to be used by all types of elections in the future.  

## Election_Audit Results:

•	A total of 369,711 votes were cast in this election.  
_Procedure_:  To find the total votes of the election, a loop was written for each row in the CSV file and a line added to tally the count:


 
 ![image](https://user-images.githubusercontent.com/84471904/124843345-9b3b6d80-df46-11eb-96ba-d4d6cf1b90a7.png)

•	Number of Votes and the Percentage of Total Votes for Each County in the Precinct: 


Jefferson: 10.509560% (38,855)

Denver: 82.782227% (306,055)

Arapahoe: 6.708213% (24,801)

_Procedure_:  To find the precinct's county information, a loop and the following lines were added to the code:  


![image](https://user-images.githubusercontent.com/84471904/124847506-e017d200-df4f-11eb-93ef-6f964cf192c8.png)

•	Denver County had the largest number of votes

_Procedure_:  An "if" statement was written to dettermine the winning county

![image](https://user-images.githubusercontent.com/84471904/124847844-8f54a900-df50-11eb-9d99-ad9a16d124cf.png)





