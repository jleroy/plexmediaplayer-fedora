srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "7bfba04bcc494cfbba693ed78efe4ac9b501960df3000915ab35acdb385e715597f9dcb11981bba5ace5b26910c89e42f36a73a233598201e3d668cfb5901abd  SOURCES/plexmediaplayer-2.23.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
