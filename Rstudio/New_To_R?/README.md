# So You Have to Use RStudio (and You’re Afraid) 😅

## What Even IS R?

R is a programming language designed for **statistics, data analysis, and visualization**. It’s great at turning messy datasets into insights and charts — basically your data translator.

---

## So What’s RStudio?

RStudio is an **Integrated Development Environment (IDE)** for R.  
Think of it as the “workshop” where you write code, check your data, generate plots, and organize your analysis.  
It’s polite, organized, and tells you exactly what’s in your session at all times — which is a lifesaver.

---

## When Would I Ever Use This?

- You need to **analyze datasets** (big or small) quickly and efficiently.  
- You want to **visualize trends, distributions, or relationships** in your data.  
- You like knowing **exactly what each part of your code is doing** (no hidden hand-wavy magic).  

---

## A Rough Step-by-Step for Creating Visualizations

1. **Check out your data** – How many columns are there? What’s listed in each? What are the column names?  
2. **Define your objective** – What question are you trying to answer? What insight are you looking for?  
3. **Choose an analysis type** – e.g., counts, percentages, ANOVA, correlation (see below).  
4. **Pick the best graph** – bar chart, boxplot, scatterplot, etc. (see below).  
5. **Load the right libraries** – these give you access to plotting functions and analysis tools.  
6. **Understand the syntax** – what all the symbols mean, why you write it that way, and how to customize it.

---

## The Environment: It’s Actually So Polite

- **Global Environment** – keeps track of every object you create (datasets, tables, variables).  
- **Values Pane** – shows the content of each object.  
- **History** – shows the commands you’ve run.  
- **Console/Terminal** – executes code and gives feedback.  
- **Files, Plots, Packages, Help, Viewer** – like a ribbon in Excel; quick access to everything you need.

---

## Libraries

Libraries are like **toolkits** for R. They contain functions for plotting, math, and data manipulation. Examples you’ll see:  
- `readr` → reading CSV files  
- `ggplot2` → powerful visualizations  
- `dplyr` → data manipulation  

---

## Graph Types: When to Use Them and Why

- **Barplot** → categorical counts or percentages  
- **Boxplot** → distributions and outliers  
- **Scatterplot** → relationships between two continuous variables  
- **Line plot** → trends over time  

---

## Analysis Types: When to Use Them and Why

- **Counts/Table** → basic categorical summaries  
- **Percentages/Proportions** → normalize uneven groups  
- **ANOVA/MANOVA** → comparing means across groups  
- **Correlation/Regression** → relationships between continuous variables  

---

## Uploading Files

- Make sure your dataset is in the **current working directory** (`getwd()` to check).  
- Or use **RStudio’s import dataset button** to upload and view it immediately.  

---

## Additional Resources

- [RStudio Cheatsheet](https://www.rstudio.com/resources/cheatsheets/)  
- [R for Data Science](https://r4ds.had.co.nz/)  
- [ggplot2 Documentation](https://ggplot2.tidyverse.org/)  
