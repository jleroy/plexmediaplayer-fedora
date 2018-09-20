srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "43254efaaef0fca36236c7962548081c97dccc47080cbae51ef00deb688aa488ceb280bbd9a73cf0ebb97dad8201fb372de4a680a67222f239d5a0957c22f7a3  SOURCES/plexmediaplayer-2.18.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
