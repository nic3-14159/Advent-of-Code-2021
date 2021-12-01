default:
	mkdir day$(day)
	cp Makefile.day day$(day)/Makefile
	cp template.cpp day$(day)/part1.cpp
	cp template.py day$(day)/part1.py
	wget --load-cookies=cookies.txt https://adventofcode.com/2021/day/$(day)/input --output-document=day$(day)/input
