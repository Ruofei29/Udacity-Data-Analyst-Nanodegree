# P6 Data Visualization with D3.js

## Summary

In this project, I chose 2008 flight data (http://stat-computing.org/dataexpo/2009/the-data.html) to do my analysis and data visualization. On the chart, you can see 10 airports with the arrival (red line) and departure (blue line) delay time group by months. I selected 10 busiest airports in US. (https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States)

In summary, departure delay is more common than arrival delay. Also, the busiest months for each airport are always June and December. I think the reason is that December is holiday season and June is a great summer time to take a break for people. Among the 10 airports, ORD and JFK have the highest delay time, which may indicate that they are usually considered as intermediary destination rather than final destination and those two airports are busy to coordinate airplanes.

Interesting findings:
1. For ATL, the highest delay months are July, March and December which is quite different than others. I'm wondering if there are major events in July and March there.
2. For JFK, the highest delay months are July and August. I guess there are more flights during the summer time since people are travelling at that time.


## Design

First, I used Python to clean the data and get arrival and departure delay time grouped by months and airports. Then I used those data to create a map that could show every airport in the US and its arrival/departure delay time by circles. However, after I collected the feedback, I decided to change my original design to a line chart which will more clear to show my focused points - delay time. So I chose the Top 10 busiest airports in the US to create a simple line chart accross 12 months. Now in this chart, we can clearly see which month has the highest delay time in a particular airport. We can also know that whether it's a good idea to choose a certain airport to be the arrival/departure destination. 

Elements on the chart:
* X axis - 12 months
* Y axis - Delay time by minutes
* Legend - Red line: Arrival Delay time; Blue line: Departure Delay time
* Buttons (changed) - It was initially airport codes; then I changed it to city names to make it more clear to audience
* Summary & Findings (changed) - Added after the review
* Color coding - Background: white; text: black; line & points: red or blue
* Tooltip (changed) - Delay Time: "100,000 mins"; Airport: "San Francisco International"; Month: "June"

## Feedback

I've shown my original design (map) to my friends and got these feedback:

First person:
* What do you notice in the visualization? -There are many circles in the map that represents the delay time.
* What questions do you have about the data? -Where you get the data? 
* What relationships do you notice? -There are big and small circles.
* What do you think is the main takeaway from this visualization? -There are too many airports in the US.
* Is there something you don’t understand in the graphic? -I kind of lost what you want to show in this map. There are too many circles there.

Second person:
* What do you notice in the visualization? -A map with many cities/airports
* What questions do you have about the data? -Is the delay time accurate? Those circles looks no difference. 
* What relationships do you notice? -Some big cities to have more delay time than others.
* What do you think is the main takeaway from this visualization? -Not much. Why don't you just let people choose the airport instead of finding the airport on a map?
* Is there something you don’t understand in the graphic? -I kind of lost what you want to show in this map. There are too many circles there.

After I changed to the line chart, Third person (reviewer):
* title and intro paragraph (REQUIRED) - please add these to tell your story and ensure your visualisation is EXPLANATORY
* y-axis consistency (REQUIRED) - to allow the reader to compare results between airports I'd strongly recommend sticking to one y-axis scale. It looks like Chicago has the most delays?
* animation (REQUIRED)- I'm wondering how helpful this is? If you are going to keep it in you need to make it clear to the reader what they are seeing by adding a changing textbox which tells them which airport the lines refer to. I'd also recommend making it a bit slower.
* buttons (text REQUIRED) - Could you go for city names instead of airport acronyms? I understand the full airport name is just too long but city names would be so much easier to handle accessibility-wise? You could add the airport codes into the tooltips instead?
* buttons (mouseover REQUIRED) - could you make the mouseover colour different to the clicked colour? This is great interaction but slightly confusing when there is one button clicked and you are hovering over another?
* buttons (spacing) - a small space between each button would make them look less crowded.
* legend (REQUIRED) - you need to add a legend for your red and blue lines

## Resources

Dataset - http://stat-computing.org/dataexpo/2009/the-data.html

Top 10 Airports - https://en.wikipedia.org/wiki/List_of_the_busiest_airports_in_the_United_States

US Map - Udacity forum




