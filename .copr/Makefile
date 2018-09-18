srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "a8fa4387e4f0aab144277b54efb52b3da3b4f07ea361404416df64b2591c10f53ad79c3bf2de50a5ac3e7c2a41260a0b25f3ef54bf916bb59c2f5f210627aff9  plexmediaplayer-2.18.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" -bs SPECS/plexmediaplayer.spec
