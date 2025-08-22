# Tadpole Treatment Analysis

## Overview

The dataset consists of multiple measurements of tadpoles subjected to three experimental groups: **Low**, **High**, and **Control**. The columns include:

* **Days\_Treatment** – Number of days each tadpole received treatment
* **Gosner\_Change** – Change in Gosner developmental stage
* **SVL\_Change** – Change in snout-vent length
* **Tail\_Change** – Change in tail length
* **Mouth\_Change** – Change in mouth structure
* **RHL\_Change** – Change in relative hind limb length

Our goal is to explore the differences in these measurements across the treatment groups and visualize trends in multi-dimensional data.

---

## Quick Glance

1. **Set Working Directory & Upload Data** – Use `getwd()` to check where R is looking and place your CSV there.
2. **Load Libraries** – `library(readr)` to access `read_csv()`, `library(GGally)` and `library(ggplot2)` for visualization.
3. **Import & View Data** – `Tadpole_Data <- read_csv("Tadpole_Data.csv")` and `View(Tadpole_Data)` for spreadsheet-style inspection.
4. **Check Structure** – `str(Tadpole_Data)` provides an overview of each column.
5. **Statistical Analysis** – Run a MANOVA to test whether treatment affects multiple response variables simultaneously.
6. **Visualization** – Use a parallel coordinates plot to visualize trends across all measurements and treatment groups.

---

## Step 1: Set Working Directory and Upload Data

R requires files to be in the **working directory** to access them easily. Check your current working directory with:

```r
getwd()
```

Once you know where R is looking, place `Tadpole_Data.csv` in that folder so it can be read into R without errors.

---

## Step 2: Load Libraries

```r
library(readr)
library(GGally)
library(ggplot2)
```

* `readr` – provides `read_csv()` and other helpful functions for data import.
* `GGally` – contains `ggparcoord()` for parallel coordinates plots.
* `ggplot2` – enables customization of plots.

**Note:** More on libraries and packages in New\_To\_R?.

---

## Step 3: Import and View the Data

```r
Tadpole_Data <- read_csv("Tadpole_Data.csv")
View(Tadpole_Data)
str(Tadpole_Data)
```

* `read_csv()` imports the dataset and assigns it to `Tadpole_Data` for easy reference.
* `View()` opens a spreadsheet-style viewer to inspect data interactively.
* `str()` shows the structure, including column types and sample data.

---

## Step 4: Statistical Analysis

```r
model <- manova(
  cbind(Days_Treatment, Gosner_Change, SVL_Change, Tail_Change, Mouth_Change, RHL_Change) ~ Treatment, 
  data = Tadpole_Data
)
```

* `cbind()` combines multiple response variables for the MANOVA.
* `Treatment` is the independent grouping variable.
* This analysis tests whether treatment group affects tadpole growth and development across all measurements simultaneously.

---

## Step 5: Create a Parallel Coordinates Plot

```r
parallel_plot <- ggparcoord(
  Tadpole_Data, 
  columns = c("Days_Treatment", "Gosner_Change", "SVL_Change", "Tail_Change", "Mouth_Change", "RHL_Change"), 
  groupColumn = "Treatment", 
  alphaLines = 0.5
) + 
  theme_minimal() +
  ggtitle("Barone, Victoria: Parallel Coordinates Plot")

print(parallel_plot)
```

* Each line represents one tadpole, colored by **Treatment group**.
* `alphaLines = 0.5` makes overlapping lines semi-transparent.
* The plot visualizes multi-dimensional trends, making it easier to compare variables across groups.

---

## Reflections on Revisiting This Project

* I’ve developed an intuitive understanding of R syntax, like naming objects (`<-`) and referencing columns for analysis and plotting.
* The parallel coordinates plot provides a clear visual comparison of multiple measurements across treatment groups.
* Revisiting this project reinforced key concepts in data cleaning, statistical testing, and multi-dimensional visualization.

---
