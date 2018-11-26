srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "7cffb259e2bdf541b7acb5983155f034c9ac83d0e6be859f66e5631d5042336e80d069ee370c5a60c4906de9652216b25253551a8aa736c8bc278a43e6eec531  SOURCES/plexmediaplayer-2.21.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
