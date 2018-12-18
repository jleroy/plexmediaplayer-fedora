srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "82a54bdacdcc299d18cae46de81350c99710c1fe37904d2ed53b5d05f6929282e232cd8d07f412838ba415e03f13d24285c232e24813dbca3ec904eb500d4862  SOURCES/plexmediaplayer-2.24.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
