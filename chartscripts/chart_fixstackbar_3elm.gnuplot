# outputpath, name0, name1, name2
set datafile separator ","

set yrange [0:100]
#set ytics 10
#set mytics 10
set xtics rotate by -90
#set grid yticks
set boxwidth 0.8 relative
set style fill solid border lc rgb "black"

set style histogram rowstacked

set terminal png size 1024,576

set output outputpath

# set xtics rotate by -90
#
plot inputpath using (100.0 * $2 / ($2 + $3 + $4)):xtic(1) with histogram lw 2 lc rgb "light-blue" title name2, \
inputpath using (100.0 * $3 / ($2 + $3 + $4)) with histogram lw 2 lc rgb "light-green" title name1, \
inputpath using (100.0 * $4 / ($2 + $3 + $4)) with histogram lw 2 lc rgb "light-pink" title name0
replot
