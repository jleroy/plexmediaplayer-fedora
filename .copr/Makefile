srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "068398ef430020f67d1f2f02090efb4546c6dafbdc70ed39df646fa07a00a57920602d19ffdb56c573ca44c74edc1e006bb216c66ae99c50bbce10e06d84fdea  SOURCES/plexmediaplayer-2.30.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
