###Guppy Data Begins Here 

Guppy_Data <- read_csv("Guppy Data.csv")

View(Guppy_Data)

summary(Guppy_Data)

table(Guppy_Data$Ornaments, Guppy_Data$Attractiveness)

counts<-table(Guppy_Data$Ornaments, Guppy_Data$Attractiveness)
percents=100*prop.table(counts,2)

plot(Attractiveness~Ornaments, data=Guppy_Data, ylab="Attractiveness",
     xlab= "Ornaments", main = "Barone, Victoria: Guppy Ornament Count vs. Attractiveness", 
     pch = 2, lwd = 2, col = "lightblue")



