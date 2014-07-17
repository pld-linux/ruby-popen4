%define	pkgname	popen4
Summary:	Open4 cross-platform
Name:		ruby-%{pkgname}
Version:	0.1.2
Release:	2
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b09ff3770ac69ae7a218b82be1e038cb
URL:		http://github.com/shairontoledo/popen4
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-open4 >= 0.4.0
Requires:	ruby-platform < 1.0.0
Requires:	ruby-platform >= 0.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POpen4 provides the Rubyist a single API across platforms for
executing a command in a child process with handles on stdout, stderr,
stdin streams as well as access to the process ID and exit status.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGES LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
