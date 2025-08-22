# Tadpole Treatment Analysis

## Overview

The dataset consists of multiple measurements of tadpoles subjected to three experimental groups: **Low**, **High**, and **Control**. The columns include:

* **Days\_Treatment** – Number of days each tadpole received treatment
* **Gosner\_Change** – Change in Gosner developmental stage
* **SVL\_Change** – Change in snout-vent length
* **Tail\_Change** – Change in tail length
* **Mouth\_Change** – Change in mouth structure
* **RHL\_Change** – Change in relative hind limb length

Out goal was to analyze the affect of the Treatment on this group of variables as a collective using a MANOVA test to get an overall understanding of how the treatment affects tadpole growth and size. 

---

## Quick Glance

1. **Set Working Directory & Upload Data** – Use `getwd()` to check where R is looking and place your CSV there.
2. **Load Libraries** – `library(readr)` to access `read_csv()`, `library(GGally)` and `library(ggplot2)` for visualization.
3. **Import & View Data** – Tadpole_Data <- `read_csv("Tadpole_Data.csv")` and `View(Tadpole_Data)` for spreadsheet-style inspection.
4. **Check Structure** – `str(Tadpole_Data)` provides an overview of each column.
5. **Change Column Data Types** – Convert dependent variable columns to numeric using `lapply(..., as.numeric)` and the independent variable (Treatment) to a factor using `as.factor()`.
6. **Handle Missing Values** – Use `na.omit(Tadpole_Data)` to remove rows with missing entries.
7. **Statistical Analysis (MANOVA)** – Run a MANOVA to test whether treatment affects multiple response variables simultaneously.
8. **Prepare for Visualization** – Convert tibbles to plain data frames `(as.data.frame())` and create numeric column indices for plotting.
9. **Visualization** – Use a parallel coordinates plot `(ggparcoord())` to visualize trends across all measurements and treatment groups, adjusting alphaLines for clarity.

--- 

## Why We Chose This Test

We used a **MANOVA** because it can test multiple variables at the same time. If we ran separate ANOVA tests tests for each measurement, we might accidentally think there’s an effect when there isn’t because each ANOVA test has a 5% chance of producing a *false positive*. That compounds on itself when we have more than one ANOVA test (5% x 5% x 5%, etc). MANOVA avoids that by looking at all traits together.

---

## Preparing the Data

* **Make sure numbers are numbers:** We listed out all of the columns that are dependent variables and told R to make them a group. Then, they were converted to numeric so R could do the calculations correctly.
* **Make sure groups are recognized:** We defined the treatment column as categorical rather than numerical so that R could tell which tadpoles were in which group.
* **Handle missing data:** We removed any rows with missing data to avoid mistakes in our calculations.
* **Set up for plotting:** The data we got from the MANOVA test comes out in a format called a 'tibble' which is hard for some later code to understand without things getting messy. We converted that tibble to a simple table called a data frame, and we marked which columns were numeric so we could make the visualization easily.

---

## Interpreting Results

The MANOVA results that show up in your terminal are from four different multivariate tests that R ran for you: Pillai's Trace, Wilks' Lambda, Hotelling-Lawley Trace, and Roy's Largest Root. They are all valid, they're just different mathematical approaches. Each one has an approximate F-value and a p-value, so you can see if your independent variable has a significant overall effect on the combination of dependent variables. 

The number that we're most intersted in right now is the p-value. There will be one for each test, but usually, they all go in the same direction. Some people just report Pillai's Trace becasue it's considered the most reliable. 

We took these numbers that were initially spit out and put them into a tidier and more universally adaptable format: a data frame. It's easier to look at the results this way. 

---

## Visualization

We used a **parallel coordinates plot** to show all measurements at once. Each line represents a tadpole, and lines are grouped by treatment. We made the lines partially transparent so overlapping lines don’t become a mess. This plot helps you see trends that match the MANOVA results.

---

## Reflections on Revisiting This Project

* The first time I attempted this analysis, I defintely did not do it right. No way I should have passed this assingment. I'm sure I got enough error messages that I probably just gave up.
* Before I could even begin to code, I took the time to really understand what question we were trying to answer with the data and why we had chosen a particular plot or visualization to do so 
* This time, I also really took the time to understand the full cycle in the data analysis:
  * We had to upload the data, reformat it, and remove rows with missing values before we could even begind our analysis.
  * We had to convert the results from our analysis into something that R could plot
  * After an analysis, we receive a measure of signficance, and it's important to understand which number we need, where that number came from, and what it tells us about our data
