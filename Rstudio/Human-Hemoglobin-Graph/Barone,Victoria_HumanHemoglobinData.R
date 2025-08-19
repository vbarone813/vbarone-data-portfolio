###Human Hemoglobin Data 

library(readr)
Human_Hemoglobin <- read_csv("Human Hemoglobin.csv")
View(Human_Hemoglobin)

summary(Human_Hemoglobin)

table(Human_Hemoglobin$Country, Human_Hemoglobin$Hemoglobin_level)

counts<-table(Human_Hemoglobin$Country, Human_Hemoglobin$Hemoglobin_level)
percents=100*prop.table(counts, 2)

boxplot(Hemoglobin_level~Country, data=Human_Hemoglobin, ylab="Hemoglobin Level", 
        xlab="Country", main = "Barone, Victoria: Human Hemoglobin Levels by Country", 
        col=c("lightgreen", "pink", "lightblue", "lightyellow"))

