# Obsidian Copr

Unofficial Fedora RPM packaging for [Obsidian](https://obsidian.md), the
knowledge-base app for plain-text Markdown notes.

Upstream ships a pre-built Electron tarball but no RPM. This repo wraps that
tarball into a proper RPM and publishes builds to Fedora Copr:

**Copr project:** https://copr.fedorainfracloud.org/coprs/kmf/Obsidian

## How it works

- `obsidian.spec` downloads the latest `obsidian-<version>.tar.gz` from the
  [obsidian-releases](https://github.com/obsidianmd/obsidian-releases/releases)
  GitHub release, installs it into `/opt/Obsidian/`, and adds a
  `/usr/bin/obsidian` symlink, a desktop entry, and an icon.
- `.copr/Makefile` is the entry point for Copr's *custom source method*. Copr
  runs `make srpm` on every commit pushed to this repo and rebuilds the package
  automatically.
- `.github/workflows/check-release.yml` polls upstream daily at 08:00 UTC and
  opens a PR bumping `Version:` whenever a new Obsidian release appears.

## Installing from Copr

```bash
sudo dnf copr enable kmf/Obsidian
sudo dnf install obsidian
```

To remove:

```bash
sudo dnf remove obsidian
sudo dnf copr disable kmf/Obsidian
```

## Building locally

Requires `rpm-build` and `rpmdevtools`:

```bash
rpmdev-setuptree
cp obsidian.desktop ~/rpmbuild/SOURCES/
spectool -g -R obsidian.spec
rpmbuild -bb obsidian.spec
```

Build an SRPM only:

```bash
rpmbuild -bs obsidian.spec
```

Clean chroot build via `mock` (Fedora 44):

```bash
rpmbuild -bs obsidian.spec
mock -r fedora-44-x86_64 rebuild ~/rpmbuild/SRPMS/obsidian-*.src.rpm
```

Lint the spec:

```bash
rpmlint obsidian.spec
```

## Updating to a new Obsidian release

The GitHub Actions workflow handles this automatically, but to do it by hand:

1. Bump `Version:` in `obsidian.spec`.
2. Add a `%changelog` entry.
3. Push to `main` — Copr picks up the commit and rebuilds.

## License

The packaging files in this repo are provided as-is. Obsidian itself is
proprietary software; see https://obsidian.md for its license terms.
