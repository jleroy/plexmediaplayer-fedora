srpm:
	dnf install rpmdevtools
	spectool --get-files --directory "`pwd`/SOURCES/" SPECS/plexmediaplayer.spec
	echo "ee873e66a2560ad1c277ddbbd3c9cc49ea1e1657a1e640b14313509ce6f3e861959b960ea0ee08148ef83404147d0dcb9731368289e0ac9c0140e01b6f490b4b  SOURCES/plexmediaplayer-2.27.0.tar.gz" | sha512sum -c
	rpmbuild --define "_topdir `pwd`" --define "_srcrpmdir $(outdir)" -bs SPECS/plexmediaplayer.spec
