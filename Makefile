problems = $(shell ls **/day*.py)

all:
	for problem in $(problems); do \
	    echo $$problem ; \
	    python3 $$problem ;\
	done
