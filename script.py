png(filename="/Users/kaou/Documents/TMD_analysis/01.png", height=900, width=1600, bg="white")

ARG48= c(199, 200, 200, 200, 205)
LYS151= c(200, 183, 14, 17, 0)
ASP352= c(10, 0, 0,0,0 )
LYS155= c(199, 200, 200,119, 190 )
LEU159= c(30, 0, 0, 0, 0)
ARG158= c(200, 0, 200, 200, 205)
ASP220= c(60, 0, 27, 14, 0)
PHE224= c(37, 117, 0, 205, 0)
GLY351= c(11, 0, 0, 0,0)
SER282= c(18, 10, 8, 6, 19)
GLU143= c(55, 0, 0, 0,0)
PHE145= c(24, 0, 0,0,0 )
ASP318= c(40, 194, 200, 200, 205)
HIS223= c(192, 192, 200, 200, 205)
ASP225= c(149, 200, 200, 200, 205)
THR287= c(136, 0, 183, 200, 205 )
ARG168= c(0, 198, 0, 0,0)
THR221= c(0, 66, 115, 178,140 )
ASN291= c(0, 60, 80, 133, 140)
SER226= c(0, 0, 27, 0, 0)
PHE224= c(0, 0, 200, 200,0 )
ARG222= c(0, 0, 66, 200, 205)
LYS50= c(0, 0, 0, 28, 74)


matrice3 = matrix(c(ARG48,LYS151,ASP352,LYS155,LEU159,ARG158,ASP220,PHE224,GLY351,SER282,GLU143,PHE145,ASP318,HIS223,ASP225,THR287,ARG168,THR221,ASN291,SER226,PHE224,ARG222,LYS50), nrow=23, ncol=5, byrow=T)
rownames(matrice3) = c("ARG48","LYS151","ASP352","LYS155","LEU159","ARG158","ASP220","PHE224","GLY351","SER282","GLU143","PHE145","ASP318","HIS223","ASP225","THR287","ARG168","THR221","ASN291","SER226","PHE224","ARG222","LYS50")



par(bg=NA)

#par(mfrow=c(2,1))

par(xpd=T, mar=par()$mar+c(0,0,0,4))

barplot(matrice3, ylab= "Contacts frequency", beside= TRUE, col=rainbow(23), names.arg=c("1200","1400","1600","1800","2000","2200","2400          FRAMES"),sub="UTP interactions: Base side",ylim=range(matrice3))
#barplot(matrice3, col=rainbow(23), beside= TRUE,names.arg=c("1200","1400","1600","1800","2000","2200","2400          FRAMES") )

legend(205, 130, legend=c(rownames(matrice3)), fill=rainbow(12), cex=0.85)

dev.off()
