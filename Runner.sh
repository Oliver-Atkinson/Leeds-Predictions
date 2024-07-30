# for (( j=1; j<=45; j++ ))
# do  
#python Starter.py
#python SheetReader.py 0
#python SheetReader.py 1
#python Preds.py 0
#python Preds.py 1
#python TableReader.py
pdflatex Summary.tex
#cp Champ_pointspos_NoDeds.pdf Dads/Champ_pointspos_NoDeds.pdf
cd Dads
pdflatex DadSummary.tex
cd ..
python Finisher.py
# done