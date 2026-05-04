SPEC = obsidian.spec

.PHONY: srpm
srpm:
	dnf install -y rpm-build rpmdevtools
	rpmdev-setuptree
	cp ../$(SPEC) ~/rpmbuild/SPECS/
	cp ../obsidian.desktop ~/rpmbuild/SOURCES/
	spectool -g -R ~/rpmbuild/SPECS/$(SPEC)
	rpmbuild -bs ~/rpmbuild/SPECS/$(SPEC)
	cp ~/rpmbuild/SRPMS/*.src.rpm $(outdir)
