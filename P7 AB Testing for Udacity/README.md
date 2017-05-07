# P7: A/B Testing for Udacity

## Project Overview
In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead.


The hypothesis was that this might set clearer expectations for students upfront, thus reducing the number of frustrated students who left the free trial because they didn't have enough time—without significantly reducing the number of students to continue past the free trial and eventually complete the course. If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.


The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

## Report
In this project, I chose the Invariant Metrics and Evaluation Metrics, identified hypothesis, calculated experiment size, duration and exposure. Finally, I did the result analysis to identify whether Gross Conversion and Net Conversion has significant difference.

To see the complete report, please go to [Udacity AB Testing for Start free trial.ipynb](https://github.com/Ruofei29/Udacity-Data-Analyst-Nanodegree/blob/master/P7%20AB%20Testing%20for%20Udacity/Udacity%20AB%20Testing%20for%20Start%20free%20trial.ipynb)

## Result and Recommendation
My final recommendation to Udacity team is not to launch this feature.

For Gross Conversion, we do see the statistical and practical significant change during the experiment. It matches our expectation before experiment, which is decrease of gross conversion. We also confirm it with sign test. We can conclude that this new feature really impact our enrollments and in the experiment, we have less enrollments(because people who cannot contribute their time will not enroll.) In that case, we can focuse on more high-quality customers.

From Net Conversion perspective, there is no statistical and practical change, even in the sign test. That is to say, this new feature has little impact on the number of paid users. This is exactly what we want - "without significantly reducing the number of students to continue past the free trial and eventually complete the course".

However, the confidence interval of net conversion does include the negative of the practical significance boundary, which means the net conversion might be decreased to a level that impact the business. So I will not recommend to launch this new feature.

## Follow-up Experiment

If you wanted to reduce the number of frustrated students who cancel early in the course, what experiment would you try? Give a brief description of the change you would make, what your hypothesis would be about the effect of the change, what metrics you would want to measure, and what unit of diversion you would use. Include an explanation of each of your choices.
* My suggested change: Give a free coach session (put it as one of the required assignment) to those students because I assume that students are frustrated about how to start learning new stuff and how to engage with the class.
* Hypothesis: If we provide this free coach session, students will find the direction to continue the course.
* Invariant metric: number of user-ids who enroll the course, because we only focus on the students has already enrolled and get a user-id.
* Evaluation metrics: Retension rate, since we want to know whether this free coach session during the free trial really help students and those students are willing to study further.
* Unit of diversion: User-id, because this free coach session is for each user not click or pageview.
