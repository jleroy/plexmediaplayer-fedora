srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "ea9ecc5dd619870477c5af88397c149f7405433063128a339d134697852fa5b3ef02bd18fb241bdd814cf6cc0f3988af8d5cad208f6794330ad0fe3d5f9408cb  SOURCES/plexmediaplayer-2.25.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
