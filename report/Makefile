TARGET=project1
HTML=main_html
SRC={$TARGET}
SRC_DIR=../src
TEST_RUN=../bin/testrun.eps

default: pdf
	rm ${TARGET}.aux ${TARGET}.dvi ${TARGET}.log ${TARGET}.out ${TARGET}.ps

both: pdf html

graph:
	cd ${SRC_DIR} && python test.py && python graphs.py -s

dvi: ${TARGET}.tex 
#	pygmentize the input source file -- THIS NAME SHOULD BE SAFE
	pygmentize -f latex -o __${TARGET}.tex ${TARGET}.tex
#	run latex twice to get references correct
	latex ${TARGET}.tex
	latex $(TARGET).tex
#	remove the pygmentized output to avoid cluttering up the directory
	rm __${TARGET}.tex 

ps: dvi
	dvips -R -Poutline -t letter ${TARGET}.dvi -o ${TARGET}.ps

pdf: ps
	ps2pdf ${TARGET}.ps

clean: ${TARGET}.pdf
	rm ${TARGET}.pdf
