srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "78c9c62d89ad45343474cbd1055b7623df87f9272f0eb7a88df285000523c2117564bc82e64a055c52ac0818280ff1b5264dfb216fbb8b5809a822034c353185  SOURCES/plexmediaplayer-2.33.1.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
