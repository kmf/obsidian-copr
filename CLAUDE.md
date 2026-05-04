# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

Package the latest Obsidian `.tar.gz` release from https://github.com/obsidianmd/obsidian-releases/releases into an RPM and publish it on Fedora Copr.

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): description`

Types: `feat`, `fix`, `docs`, `chore`, `ci`, `build`, `refactor`, `test`

## Build Commands

```bash
# Local RPM build (requires rpm-build, rpmdevtools)
rpmdev-setuptree
cp obsidian.desktop ~/rpmbuild/SOURCES/
spectool -g -R obsidian.spec
rpmbuild -bb obsidian.spec

# Build SRPM only
rpmbuild -bs obsidian.spec

# Clean chroot build via mock (Fedora 44)
rpmbuild -bs obsidian.spec
mock -r fedora-44-x86_64 rebuild ~/rpmbuild/SRPMS/obsidian-*.src.rpm

# Lint
rpmlint obsidian.spec
```

## Architecture

- `obsidian.spec` — RPM spec that repackages the pre-built Electron tar.gz from GitHub releases into `/opt/Obsidian/` with a `/usr/bin/obsidian` symlink
- `.copr/Makefile` — Entry point for Copr custom source method; `make srpm outdir=<dir>` produces an SRPM
- `obsidian.desktop` — Freedesktop desktop entry, referenced as Source1 in the spec

## Updating to a New Obsidian Release

A GitHub Actions workflow (`.github/workflows/check-release.yml`) runs daily at 08:00 UTC and opens a PR when a new upstream release is detected. It can also be triggered manually via `workflow_dispatch`.

To update manually:
1. Update `Version:` in `obsidian.spec`
2. Add a `%changelog` entry
3. Push — Copr rebuilds automatically
