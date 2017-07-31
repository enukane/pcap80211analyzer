# outputpath, name
set datafile separator ","
set style fill solid border lc rgb "black"
set boxwidth 0.8 relative
set terminal png size 1024,576
set output outputpath
set xtics rotate by -90
plot inputpath using 0:($2):xtic(1) with boxes lw 2 lc rgb "light-pink" title name
replot

