srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "fc55f12de9a55520500a3da9da7a606280245dadd9d15e905e739abe0ff2f92bd50857e092fca79f819462bfab83127fe6a88f47d4945385d9462ba7fed60f45  SOURCES/plexmediaplayer-2.20.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
