# DataScienceAssignmentReligion
Assignment from Coursera course https://www.coursera.org/learn/python-plotting/home/week/4

## Subject
This script analyses **Germany** and **Religious events or traditions** as stated in the assignment. I was interested in the connection between religion and education. While finetuning my hypothesis I was looking at the available data. I found lots of statistics about the whole german population. Since I am german myself, I knew that each of the german countries is somewhat different in how many people are protestand or catholic. Just recently german high school students finished their 12 years of school and got their final degree. Therefore I had the hypothesis, that countries with a higher amount of religious population are doing worse than countries with a lower of amount of religious population. I was thinking that religion might have a direct or indirect effect on the education system and the success.

# Data Sources
## Number of catholics and protestants in german countries
https://www.kirchenaustritt.de/statistik/religionszugehoerigkeit

## Average degrees of german high school graduates in german countries
https://de.statista.com/statistik/daten/studie/36277/umfrage/durchschnittliche-abiturnoten-im-vergleich-der-bundeslaender/

# Analysis
As shown in the picture, I made two bar charts showing how many percent of the population of each of the 16 german countries is either protestant or catholic. To get a feeling of the connection to the average degrees achieved by high school students, I drew a line showing it. With this, you can see at a glance if there is a strong connection between the two or not. Additionally, I did two t-tests with p < 0.01 to check, if there is a significant correlation. 
It turned out, that between the percentage of protestant population and the degree there is a significant correlation (p < 0.01), but not between catholics and degrees (p > 0.01).
