criticcritic
============

NETS213 Final Project - Fall 2014

**Overview**:
<br>
Basically we're collecting data on the way politicians from different backgrounds are described in the media. So our first step is to gather articles about politicians, then we use crowdworkers to find the adjectives in the articles that describe the politicians. To aggregate the data we input it into a word cloud generator for a good way to visualize the results.

**MASTER BRANCH**
<br>
**Quality Control Model**
<br>
Input - CSV file of URLs of articles about politicians
<br>
Processing - Multiple crowdworkers per article
<br> 
Output - CSV file of adjectives describing politicians

**Aggregation Model**
<br>
Input - CSV file of adjectives
<br>
Processing - Remove duplicates, check validity, and count the most common words
<br>
Output - Word cloud of most frequent adjectives used

**Miscellaneous**
<br>
Data flowchart - called flowchart.pdf
<br>
Raw URL collection - a sample of the raw data called rawdata.csv
<br>
HIT Screenshot - hit.png

**WORDCLOUDS FOLDER**
<br>
Individual politician word clouds
<br>
Gender grouped word clouds
<br>
Political party grouped word clouds

**RAW FOLDER**
<br> 
Collection of csv data files from Crowdflower

**GRAPH ANALYSIS FOLDER**
<br>
Collection of graphs analysing different aspects of the project.
<br>
The first graph displays a geo chart of the city locations accepted HITs were from (to get a good sense of where worker quality is the best)

**Group Members**
<br>
*Devesh Dayal*
<br>
*Kate Miller*
<br>
*Sean Sheffer*
<br>
*Sierra Yit*
