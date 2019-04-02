srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "117461edb28fce33256373eeeb5535fc9dd6295ba93fa0f2117a37bec198ee0b93d6b51d17d4f6c3c715231214cae930a7a5ff85e3d4fdc079eb2a6f857b00cf  SOURCES/plexmediaplayer-2.31.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
