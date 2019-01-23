srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "c1f1fb2ba76693e91bd604be2de9e23c5f0ee62e229d43232e51f3e7d227af187dc8431133115e542a6cd9fa1de35545303af74546456b350152628ea5b8b4e4  SOURCES/plexmediaplayer-2.26.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
