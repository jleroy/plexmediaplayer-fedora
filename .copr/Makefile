srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "241332bb3e7dd4c63ee0f4d3b7aedeeccd59d59f35ea43a61389ea186754d18d5272452a22294cf9ee7f79c024b9bf3cf61af8eaff2b2bb3f631696a538f4dd6  SOURCES/plexmediaplayer-2.21.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
