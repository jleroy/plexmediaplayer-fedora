srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "49991b2b8992ee0dedce98bbb91038ec319aafd8c0f923dff6ac333206e37a95d2c9e4bee1d61e075e2f0b6eb5368063d4f0cf16b13260be4e01a8e35fc37e3c  SOURCES/plexmediaplayer-2.30.1.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
