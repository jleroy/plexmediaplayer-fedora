srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "60f162b98d245d9af88d4a60bc3cbfbfbe01b6fce57bc8ba0d2751936770be642ff6714c10724443a0c0db393b101a24d072b87378c90a5fba77e47d8e238c58  SOURCES/plexmediaplayer-2.32.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
