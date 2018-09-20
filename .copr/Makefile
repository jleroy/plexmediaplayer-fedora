srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "d1d9079a3decd86c0485bb4e6cc7f7034cb33e825e693c0d8ed199bcee3d10f5f1f33f539cb167f8fa9b3692f8087f11a55b14546ebb5e06b6112038690de53a  SOURCES/plexmediaplayer-2.19.1.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
