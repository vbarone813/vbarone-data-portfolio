# ----------------------------
# Tadpole Treatment Analysis
# Author: Victoria Barone
# ----------------------------

# Load Libraries
library(readr) #library used for data import and cleaning 
library(GGally) #extended visualizations for exploratory analysis (parallel coordinates plots or 'ggparcoord()' )
library(ggplot2) #general data visualization 

# Import Dataset
Tadpole_Data <- read_csv("Tadpole_Data.csv")
View(Tadpole_Data)

# Check data types 
str(Tadpole_Data) #gives you a summary of your data frame showing things like column names and data types

# Group dependent variable columns, convert to numeric
numeric_cols <- c("Days_Treatment", "Gosner_Change", "SVL_Change", "Tail_Change", "Mouth_Change", "RHL_Change")
Tadpole_Data[numeric_cols] <- lapply(Tadpole_Data[numeric_cols], as.numeric)

# convert independent variable column to categorical 
Tadpole_Data$Treatment <- as.factor(Tadpole_Data$Treatment)

# Handle Missing Values
Tadpole_Data <- na.omit(Tadpole_Data)

# Statistical Analysis (MANOVA)
model <- manova(cbind(Days_Treatment, Gosner_Change, SVL_Change, Tail_Change, 
                      Mouth_Change, RHL_Change) ~ Treatment, data = Tadpole_Data)
summary(model)

# Visualization: Parallel Coordinates Plot 

# Convert tibble to plain data frame
Tadpole_Data_df <- as.data.frame(Tadpole_Data)

# Get numeric column indices
numeric_cols_idx <- which(names(Tadpole_Data_df) %in% numeric_cols)

# Create the plot
parallel_plot <- ggparcoord(
  data = Tadpole_Data_df,
  columns = numeric_cols_idx,  # numeric columns by index
  groupColumn = "Treatment",   # grouping variable
  alphaLines = 0.5
) +
  theme_minimal() +
  ggtitle("Barone, Victoria: Parallel Coordinates Plot")

print(parallel_plot)
