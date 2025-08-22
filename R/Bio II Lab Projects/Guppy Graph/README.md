# Guppy Data Analysis

## Overview

The dataset consists of two columns:
- **Ornaments:** The number of ornaments each guppy has
- **Attractiveness:** A measured attractiveness score

Our goal was to explore the relationship between ornament count and attractiveness.

## Quick Glance 
1. Set Working Directory & Upload Data – Make sure R can find your CSV file with `getwd()` and upload it to that folder.  
2. Load Libraries – Use `library(readr)` to access `read_csv()` and other helpful functions. 
3. Import & View Data – `Guppy_Data <- read_csv("Guppy Data.csv")` and `View(Guppy_Data)` for spreadsheet-style inspection.  
4. Check Summary Stats – `summary(Guppy_Data)` shows min, median, mean, max for numeric columns, and length/class/mode for categorical columns.  
5. Create Table of Counts & Percentages – Use `table()` and `prop.table()` to count combinations and normalize percentages for fair comparison.  
6. Create a Scatter Plot – `plot(Attractiveness ~ Ornaments, data = Guppy_Data, ylab="Attractiveness", xlab="Ornaments", main="Your Title", pch=2, lwd=2, col="lightblue")` visualizes the relationship between ornament number and attractiveness.

---

## Step 1: Set Working Directory and Upload Data
- I checked my working directory using `getwd()` to make sure R could find the CSV file.
- Once I knew where R was “looking,” I dragged the CSV file into that folder so it could be accessed easily.
- Note: I explain what a working directory is and how to set one up in [New_To_R?](Rstudio/New_To_R?).

---

## Step 2: Load Libraries (*)

```r
library(readr)
````

* This loads the `readr` package, which contains functions like `read_csv()` for reading CSV files.
* Note: More on libraries in [New_To_R?](Rstudio/New_To_R?).

---

## Step 3: Import and View the Data

```r
Guppy_Data <- read_csv("Guppy Data.csv")
View(Guppy_Data)
summary(Guppy_Data)
```

* `read_csv()` pulls the CSV file into R and assigns it the object name `Guppy_Data` for easy reference.
* `View()` opens a spreadsheet-style viewer for interactive inspection.
* `summary()` gives a quick overview of each column: min, median, mean, max for numeric columns, and length/class/mode for categorical columns.

---

## Step 4: Create a Table of Counts and Percentages

```r
table(Guppy_Data$Ornaments, Guppy_Data$Attractiveness)
counts <- table(Guppy_Data$Ornaments, Guppy_Data$Attractiveness)
percents <- 100 * prop.table(counts, 2)
```

* `table()` counts occurrences of each combination of Ornaments and Attractiveness.
* Assigning to `counts` lets us reference this table later.
* `prop.table(counts, 2)` normalizes the counts by column, converting raw counts into percentages.
* Multiplying by 100 gives actual percentages.
* This step ensures fair comparison between ornament groups even if sample sizes are uneven.

---

## Step 5: Create a Scatter Plot

```r
plot(Attractiveness ~ Ornaments, data = Guppy_Data, 
     ylab = "Attractiveness", xlab = "Ornaments", 
     main = "Barone, Victoria: Guppy Ornament Count vs. Attractiveness", 
     pch = 2, lwd = 2, col = "lightblue")
```

* `Attractiveness ~ Ornaments` → Y-axis is Attractiveness, X-axis is grouped by Ornaments.
* `data = Guppy_Data` → tells R which dataset to pull the columns from.
* `ylab` and `xlab` → label the axes for clarity.
* `main` → sets the title of the plot.
* `pch = 2` → changes the plotting symbol (triangle).
* `lwd = 2` → sets the line width (for points and axes).
* `col = "lightblue"` → sets the color of the points.

This scatter plot visualizes how ornament count relates to attractiveness across the guppies in the dataset.

---

## Reflections on Revisiting This Project

* Initially, I followed example code without understanding it. Now, I can read each line, ask why it’s written that way, and see how it connects to the dataset.
* Creating summary tables and normalizing counts shows how to make fair comparisons across uneven groups.
* The scatter plot gives a clear visual representation of the relationship between ornament number and attractiveness.
* Revisiting this project reinforced plotting and data grouping concepts I learned in Python and R.

--- 

