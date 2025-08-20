# Bird Malaria Analysis

## Overview
The dataset consists of two columns:  
- **Treatment:** Control or Egg Removal  
- **Response:** Malaria or No Malaria  

Our goal was to explore the relationship between treatment type and malaria outcomes.

## Step 1: Importing Data
```R
Bird_Malaria_Data<-read.csv("Bird_Malaria_Data.csv")
View(Bird_Malaria_Data)
summary(Bird_Malaria_Data)
```

- I gave the dataset a short reference name (`Bird_Malaria_Data`) so I could reuse it throughout the code without repeatedly typing the file name.  
- `read.csv()` pulls the data from the CSV file into R.  
- `View()` allows inspection of the data in a spreadsheet-like format.  
- `summary()` gives a quick overview of each column, including counts and basic statistics.

## Step 2: Creating a Summary Table
```R
table(Bird_Malaria_Data$Treatment, Bird_Malaria_Data$Response)
counts<-table(Bird_Malaria_Data$Treatment, Bird_Malaria_Data$Response)
```

- `table()` counts the occurrences of each combination of treatment and response.  
- We only needed the two columns because this is the focus of our analysis — comparing treatment to outcome.  
- Assigning the table to `counts` with `<-` allows us to reference this table later in our code (plotting, percentages, etc.).

## Step 3: Normalizing Percentages
```R
percents=100*prop.table(counts,2)
```

- `prop.table(counts, 2)` normalizes the table by columns, converting raw counts into proportions.  
  - `margin = 2` → normalize by columns (each response category sums to 1)  
- Multiplying by 100 converts these decimals into percentages (e.g., 0.67 → 67%).  
- This step is important because our treatment groups are uneven in size, so percentages allow a fair comparison.

## Step 4: Plotting the Data
```R
plot(counts, main="Barone, Victoria: Bird Malaria Treatment vs. Response", 
        xlab="Treatment", col=c("pink", "lightyellow"),
        legend=rownames(counts), 
        args.legend = list(x="topleft", horiz=TRUE), beside=FALSE)
```

- `counts` is the table used to generate the bar plot. We could also use `percents` to show normalized proportions.  
- `main` sets the title of the plot.  
- `xlab` labels the x-axis (“Treatment”).  
- `col` assigns colors to each treatment group.  
  - (I took my time learning some unique colors here, as you can tell)  
- `legend` pulls row names from `counts` to label the bars.  
- `args.legend` is a list of instructions for legend placement and formatting.  
  - “What are the conditions or characteristics (arguments <- args) of this legend?”  
  - Everything that follows `=` is related to the legend.  
- `beside=FALSE` produces a stacked bar plot. Set `beside=TRUE` for side-by-side bars.  
  - It’s called `beside` because the question you’re answering is “should the bars be beside each other?”  
    - `beside = TRUE` → yes, put them beside each other  
    - `beside = FALSE` → no, don’t put them beside each other (so stack them instead)  

This plot gives a visual representation of the distribution of malaria outcomes across treatment groups.

## Reflections on Revisiting This Project
- Initially, I was just following example code without understanding it. Now, I can look at each line, ask why it’s written that way, and understand how it connects to the data.  
- The `<-` operator is used to assign values to variables, allowing easy reuse.  
- Functions like `table()` and `prop.table()` provide quick ways to summarize and normalize data.  
- Plot customization (colors, legends, stacking) makes the visualization clearer and more interpretable.  

Overall, this revisiting exercise reinforces how coding concepts learned in Python transfer to R, and how thoughtful normalization and visualization can make small datasets meaningful.


---
