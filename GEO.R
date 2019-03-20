
# Download bioconductor if you havent
# source("https://bioconductor.org/biocLite.R")

# Install GEOquery
# biocLite()
# biocLite("GEOquery")
library(GEOquery)



args <- commandArgs(trailingOnly = TRUE)


#rnorm(n=as.numeric(args[1]), mean=as.numeric(args[2]))

geonum = args[1]



### This will download a 20 Mb
eList <- getGEO(geonum, GSEMatrix = TRUE)
eData <- eList[[1]]

p = pData(eData)

write.csv(p, file = "MyData.csv")
