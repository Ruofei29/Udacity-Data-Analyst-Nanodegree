# P6 Data Visualization with D3.js

## Summary

In this project, I chose 2008 flight data (http://stat-computing.org/dataexpo/2009/the-data.html) to do my analysis and data visualization. On the chart, you can see 10 airports with the arrival (red line) and departure (blue line) delay time group by months. I selected 10 busiest airports in US. (https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States)

## Design

First, I used Python to clean the data and get arrival and departure delay time grouped by months and airports. Then I used those data to create a map that could show every airport in the US and its arrival/departure delay time by circles. However, after I collected the feedback, I decided to change my original design to a line chart which will more clear to show my focused points - delay time. So I chose the Top 10 busiest airports in the US to create a simple line chart accross 12 months. Now in this chart, we can clearly see which month has the highest delay time in a particular airport. We can also know that whether it's a good idea to choose a certain airport to be the arrival/departure destination. 

## Feedback

I've shown my original design (map) to 3 of my friends and got these feedback:

1. "The map looks cool but I kind of lost what you want to show in this map. There are too many circles there."

2. "I don't know the point of this map. I know that you want to show the delay time, but there is no difference for each airports in my opinion."

3. "Why don't you just let people choose the airport instead of finding the airport on a map?"

## Resources

Dataset - http://stat-computing.org/dataexpo/2009/the-data.html

Top 10 Airports - https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States

US Map - Udacity forum




