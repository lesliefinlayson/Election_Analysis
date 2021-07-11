# Anylysis of an Election Audit Using Python:  
Is It Successful and Can It Be Automated

## Project and Purpose Overview:
Determining the winner of any US election is a large task.  A great deal of information is collected and processed as quickly as possible.  A recent Colorade US Congressional Precinct, for example, had a turnout of almost 370,000 voters.  Excel has been customarily used to analyze this information.  While this is functional, there may be other options that can better handle large amounts of data and that can be automated to save time and increase accuracy.  

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

•	Denver County received the largest number of votes

_Procedure_:  An "if" statement was written to dettermine the winning county

![image](https://user-images.githubusercontent.com/84471904/124847844-8f54a900-df50-11eb-9d99-ad9a16d124cf.png)


•	Number of Votes and the Percentage of Total Votes for Each Candidate: 

Charles Casper Stockham: 23.0% (85,213)

Diana DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

_Procedure_:  To find the candidate information, a loop and the following lines were added to the code:


![image](https://user-images.githubusercontent.com/84471904/124848515-dc854a80-df51-11eb-9820-33f8ab70e636.png)


•	Diana DeGette won the election:

Winning Vote Count: 272,892

Winning Percentage: 73.8%

_Procedure_:  An "if" statement was written to dettermine the winning candidate:

![image](https://user-images.githubusercontent.com/84471904/124848880-9381c600-df52-11eb-8a0d-5b11e7573804.png)


## Election_Audit Summary
This Python script quickly and correctly analyzes the information needed to determine the winner of the election by calculating total election votes, the total votes received by each candidate, the percentage of the total vote each candidate received, and finally, the election winner based on this information.  This script was then modified to include analyzing the data by county, including number of votes and the percentage of total votes for each county.  

Business proposal:  
This Python script can be easiy modified for future elections, whether local, county, congressional, etc. Because the lists and dictionaries in the script are not hard-coded, they will run analysis on whatever data files are entered.  County information in the current script may or may not be of intereste in some elections and can be removed.  Other parameters that might be of interest which could be added and analyzed to give more information are:
 
•	political party affiliation

•	collecting and analyzing data by voting districts

•	voters' age, ethnicity, gender if this infomratin is available 



