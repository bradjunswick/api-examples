#starting with Leon French's collapsed human microarray data
brain1=read.delim(file="Desktop/matrix.29192x346.txt", sep="\t", header=T, row.names=1)
brain2=read.delim(file="Desktop/matrix.29192x323.txt", sep="\t", header=T, row.names=1)
brain3=read.delim(file="Desktop/matrix.29192x158.txt", sep="\t", header=T, row.names=1)
#combine all into a single matrix
a=cbind(brain1, brain2, brain3)
write.table(a, "test.txt", quote=F, row.names=T, col.names=T, sep="\t")
#sampled 1500 values from the data
b=sample(a, 1500)
write.table(b, "rand1500.txt", quote=F, row.names=F, col.names=F, sep="\t")
#sorted and log transformed the data
b=sort(b)
c=log2(as.numeric(b))
c=as.list(c)
write.table(c, "randlog1500.txt", quote=F, row.names=F, col.names=F, sep="\t")
#found a gene of interest (PDYN)
intersect("PDYN", row.names(a))
which(row.names(a) == "PDYN")
head(a[21652, ])
write.table(as.list(a[21652,]), "PDYN.txt", quote=F, row.names=F, col.names=F, sep="\t")

#output files are formatted to be read by the python script
