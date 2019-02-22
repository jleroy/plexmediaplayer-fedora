srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "ec6ed6994194d8f8915b3fcf3849b0ea2cd1c26a0d2d1ff5115445a3517a8ca54003c85b4fc76d1b3476106e374a69c5af90aa01fb7839c90810ed1ed74b56f6  SOURCES/plexmediaplayer-2.28.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
