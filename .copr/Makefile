srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "cc369f8c04359fb37459f81ff82b28c08182d9c74856adb46cbce88dd00939bc44e0255d1831189f97787ca246eb5583aadd45e05e9f5c73a454bc23676e10b5  SOURCES/plexmediaplayer-2.29.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
