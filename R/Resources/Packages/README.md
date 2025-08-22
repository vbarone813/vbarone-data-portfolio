# Packages and `library()` 

---

Think of a package like a game expansion: it gives you a bunch of extra features that don’t come with the base game. The difference? In programming, most packages are free! 😄

A package is a collection of **functions** that all serve a similar purpose. For example, one package might have functions for creating visualizations — one for boxplots, another for barplots, and so on. R doesn’t know how to do these things on its own, so you need the package to access those functions.

Different tasks require different packages. When you **install** a package, your computer stores it in your “library.” Later, whenever you start a new R project and want to use that package, you call it with the `library()` function. Just type the package name in the parentheses, and you’re ready to go!

```r
install.packages("ggplot2")  # download it once
library(ggplot2)             # make the functions available in your project
```

---

# Tidyverse 

The tidyverse is a collection or suite of R packages that work together and follow the same philosophy. Think of it like a starterpack for analysis. 

Tidyverse includes:
* readr -> importing data
* tidyr -> data tidying and reshaping
* dplyr -> data manipulation
* ggplot2 -> data visualization  
* forcats -> working with categorical variables 
* stringr -> string/text manipulation
* lubridate -> dates and times 

Using Tidyverse is really useful in this way because all of the functions in its included packages behave in a familiar and uniform way, so you don't have to learn new syntax styles. Most modern R tutorials and courses use tidyverse, too, so familiarizing yourself with it early sets you up for success. 

--- 

# Exploring the Tidyverse Packages 

## readr
The main role of this package is importing data into R quickly and cleanly. Basically, if you have a spreadsheet or table, readr helps R understand it. 

Key Functions:
* `read_csv()` - reads comma-separated files (.csv)
* `read_tsv()` - reads tab-separated files (.tsv)
* `read_delim()` - reads files with a custom delimiter
* `write_csv()` - saves a data frame as a CSV
* `write_tsv()` - saves a data frame as a TSV
* `problems()` - shows parsing problems from imported files

There are more functions, but these cover most beginner use cases.
  

## tidyr
The main role of this package is tidying and reshaping data. "Tidy data" means each row is one observation and each column is one variable. `tidyr` helps you get messy or wide data into a clean, tidy format so it's easier to analyse and visualize. Think of it as an organization tool: it takes messy spreadsheets and puts them in a neat, R friendly layout. 

Key Functions: 
* `pivot_longer()` - turns wide-format columns in long-format
  * ex: convert separate 'Day 1,' 'Day 2,' 'Day 3' columns into one 'Day column.'
  * Similar to 'pivot/unpivot' in excel
*   


## dplry

## ggplot2

## forcats

## stringr

## lubridate

--- 

# Help 

Everypackage in R comes with built-in documentation. There's package level help and function level help.

```r
?readr
help(package = "readr") #insert package name in quotations

?read_csv
help(read_csv) #insert function in parentheses
```

Additionally, there is a modern, beginner-friendly Tidyverse website with documentation and exammples: https://readr.tidyverse.org  




