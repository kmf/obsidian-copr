%global debug_package %{nil}

Name:           obsidian
Version:        null
Release:        1%{?dist}
Summary:        A powerful knowledge base on top of a local folder of plain text Markdown files
License:        Proprietary
URL:            https://obsidian.md
ExclusiveArch:  x86_64

Source0:        https://github.com/obsidianmd/obsidian-releases/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        obsidian.desktop

# Electron runtime dependencies
Requires:       gtk3
Requires:       nss
Requires:       alsa-lib
Requires:       at-spi2-atk
Requires:       libdrm
Requires:       mesa-libgbm
Requires:       libxkbcommon

# Disable automatic dependency detection — the bundled Electron libs
# would pull in unresolvable soname provides/requires.
AutoReqProv:    no

%description
Obsidian is a note-taking and knowledge management application that works
on top of a local folder of plain text Markdown files.

%prep
%setup -q -n %{name}-%{version}

%build
# Pre-compiled Electron app — nothing to build.

%install
# Application directory
install -d %{buildroot}/opt/Obsidian
cp -a . %{buildroot}/opt/Obsidian/

# CLI wrapper
install -d %{buildroot}%{_bindir}
ln -s /opt/Obsidian/obsidian %{buildroot}%{_bindir}/obsidian

# Desktop entry
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/obsidian.desktop

# Icon
install -Dm644 resources/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%files
/opt/Obsidian/
%{_bindir}/obsidian
%{_datadir}/applications/obsidian.desktop
%{_datadir}/icons/hicolor/512x512/apps/obsidian.png

%changelog
* Wed Aug 19 2026 github-actions <actions@github.com> - null-1
- Update to null
* Tue Aug 11 2026 Karl Fischer <karl@obsidian.co.za> - 1.13.6-1
- Update to upstream Obsidian 1.13.6

* Thu Jul 30 2026 Karl Fischer <karl@obsidian.co.za> - 1.13.4-1
- Update to upstream Obsidian 1.13.4

* Sun May 04 2026 Karl Fischer <karl@obsidian.co.za> - 1.12.7-1
- Initial package
