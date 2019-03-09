srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "e7ebd44784bada2e86a34e4fbec7ac2207a20ca0421ee4d5fa71c0059f2745e27fd1a3c2746fe63e9fa2ac108272aac6059363fc480b3a39783bbeb52883e65f  SOURCES/plexmediaplayer-2.29.1.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
