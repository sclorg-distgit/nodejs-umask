%{?scl:%scl_package nodejs-umask}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-umask

%global npm_name umask
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           %{?scl_prefix}nodejs-umask
Version:        1.1.0
Release:        5%{?dist}
Summary:        Convert umask from string <-> number
Url:            https://github.com/smikes/umask
Source0:        http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        MIT
BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(code)
BuildRequires: %{?scl_prefix}npm(jslint)
BuildRequires: %{?scl_prefix}npm(lab)
%endif

%description
Convert umask from string <-> number

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
lab -ct 100
jslint --terse --latest *.js test/*.js
%endif

%files
%{nodejs_sitelib}/umask

%doc README.md
%doc LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-5
- rebuilt

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.1.0-4
- Enable SCL macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 21 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-2
- Removed %%clean and rm -rf %%buildroot from %%install
- changed Summary and %%description to start with capital letter

* Thu May 14 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-1
- Initial build
