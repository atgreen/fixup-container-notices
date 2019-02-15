all:
	rm -rf dist
	mkdir dist
	PWD=`pwd`; (cd ..; tar cvfz $(PWD)/dist/fixup-container-notices.tar.gz fixup-container-notices)
	rpmbuild --define "_srcrpmdir dist" --define "_sourcedir dist" -bs fixup-container-notices.spec

clean:
	rm -f *~
