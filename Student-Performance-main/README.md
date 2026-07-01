Interactive Power BI dashboard for analyzing student performance,
attendance, behavior, and subject scores.

## Features

-   KPI Cards (Total Students, Attendance %, Average Score)
-   Class slicer
-   Subject-wise stacked bar chart
-   Behavior doughnut chart
-   Term-wise line chart
-   Student performance table

## Files

-   Student Performance Dashboard.pbix
-   Students.csv
-   Scores.csv
-   Attendance.csv
-   Behavior.csv

## Tools

-   Power BI Desktop
-   Power Query
-   DAX

## DAX Measures

``` dax
Total Students = COUNT(Students[StudentID])
Attendance % = DIVIDE(SUM(Attendance[Present]),COUNTROWS(Attendance))
Avg_Score_Per_Sub = AVERAGE(Scores[Score])
Behavior Count = COUNT(Behavior[BehaviorType])
```

## Dashboard

Add a screenshot in `Images/Dashboard.png`.


