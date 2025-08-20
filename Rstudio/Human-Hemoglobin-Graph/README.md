# Human Hemoglobin Analysis 

## Overview 
The dataset consists of two columns:
- **Country:** The country each participant is from
- **Hemoglobin_level:** The Measured hemoglobin level

Our goal was to explore the distribution of hemoglobin levels across countries. 

--- 
## Quick Glance
1. **Set Working Directory & Upload Data** – Make sure R can find your CSV file with `getwd()` and upload it to that folder.
2. **Load Libraries** – Use `library(readr)` to access `read_csv()` and other helpful functions. (*More on libraries in a separate file*)
3. **Import & View Data** – `Human_Hemoglobin <- read_csv("Human Hemoglobin.csv")` and `View(Human_Hemoglobin)` for spreadsheet-style inspection.
4. **Check Summary Stats** – `summary(Human_Hemoglobin)` shows min, median, mean, max for numeric columns, and length/class/mode for categorical columns.
5. **Create Table of Counts & Percentages** – Use `table()` and `prop.table()` to count combinations and normalize percentages for fair comparison.
6. **Create Boxplot** – `boxplot(Hemoglobin_level ~ Country, data = Human_Hemoglobin, ylab="Hemoglobin Level", xlab="Country", main="Your Title", col=c(...))` visualizes distributions grouped by country.

---
## Step 1: Set Working Directory and Upload Data 
- I was having a hard time uploading my dataset and kept getting errors. This is because R is really picky about where it uploads its files from. I had to check where R was currently pulling files from by using `getwd()` to look at my *Working Directory*
- Note: More about the working directory in [file here]).
- Once I knew where R was "looking," I opened up my computer's file application and dragged the CSV file into that folder.

---
## Step 2: Load Libraries 
```R
library(readr)
```

- This loads the readr package, which contains functions like read_csv() for reading CSV files
- Note: More on libraries and packages in [file here].

--- 
## Step 3: Import and View the Data 
```R
Human_Hemoglobin <- read_csv("Human_Hemoglobin.csv")
View(Human_Hemoglobin)
summary(Human_Hemoglobin)
```

- `read_csv()` pulls the CSV file into R and assigns it the object name Human_Hemoglobin for easy reference. That way, you don't have to write out Human_Hemoglobin.csv every single time. Technically, you could name this anything so long as you know what you're referencing.
- `View()` opens a spreadsheet-style viewer so we can inspect the data interactively.
- `summary()` gives a quick overview of each column in the console (bottom left part of the screen where you might also get error messages): min, median, mean, max for numeric columns, and length/class/mode for categorical columns.
- Note: R is case sensitive, so there is a difference between "Summary()" and "summary()," so watch out for that if you start getting error messages!
- Note: More on R's layout (like what I mean when I say "in the console" in [file here].

--- 
## Step 4: Create a Table of Counts and Percentages 
```R
table(Human_Hemoglobin$Country, Human_Hemoglobin$Hemoglobin_level)
counts <- table(Human_Hemoglobin$Country, Human_Hemoglobin$Hemoglobin_level)
percents <- 100 * prop.table(counts, 2)
```

- `table()` counts occurrences of each combination of Country and Hemoglobin_level.
- When we write `counts <-` we are assigning whatever follows (our table, in this case) to that object name so we can easily reference it later. Think of this step as naming our table so we can call on it by name later on.
- `prop.table(counts, 2)` normalizes the counts by column, converting raw counts into percentages.
- Multiplying by 100 gives actual percentages (67%) instead of decimal numbers (0.67).
- This step ensures fair comparison between countries even if sample sizes are uneven. 

---
## Step 5: Create a Boxplot 
```R
boxplot(Hemoglobin_level ~ Country, data = Human_Hemoglobin, 
        ylab="Hemoglobin Level", xlab="Country", 
        main="Barone, Victoria: Human Hemoglobin Levels by Country", 
        col=c("lightgreen", "pink", "lightblue", "lightyellow"))
```
- Hemoglobin_level ~ Country → Y-axis is Hemoglobin_level, X-axis is grouped by Country. Each box represents the distribution for one country.
- data = Human_Hemoglobin → tells R which dataset to pull the columns from.
- ylab and xlab → label the axes for clarity.
- main → sets the title of the plot.
- col = c(...) → assigns colors to each box for easy visual distinction.

--- 
## Reflections on Revisiting This Project 
- Initially, I was just following example code without understanding it. Now, I can read each line, ask why it’s written that way, and see how it connects to the dataset.
- I've developed an understanding of the syntax that feels somewhat intuitive now (ex: "xlab as in x label" and "counts <-" meaning naming an object like naming a variable in Python)
- The boxplot gives a clear visual representation of distribution, variability, and differences between countries.
- Revisiting this project reinforced concepts I learned in Python and helped me understand grouping, labeling, and plotting in R.



