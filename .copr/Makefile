srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "a9e731259a347626513b9992397a45d80a8a8e8104d9733b42e45085774373b7ebef2cb2e41149405c9035c60bcddc116fa69833c2199111b38de6b1ac946bf5  SOURCES/plexmediaplayer-2.34.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
