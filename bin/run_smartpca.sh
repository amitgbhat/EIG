# ./smartpca.perl -i HumanOriginsPublic2068_out_valid.eigenstratgeno -a HumanOriginsPublic2068_out_valid.snp -b HumanOriginsPublic2068_out.ind -k 2 -o example.pca -p example.plot -e example.eval -l example.log
file="example.pca.evec"
if [ -f "$file" ]
then
	echo "$file found."
else
    export PATH=$PATH:$(pwd);
    smartpca -p example.pca.par
fi

python my_plot.py