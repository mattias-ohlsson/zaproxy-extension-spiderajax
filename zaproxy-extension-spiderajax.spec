%global extension_id spiderAjax
%global extension_name Ajax Spider
%global extension_info Allows you to spider sites that make heavy use of JavaScript using Crawljax.
%global extension_infoUrl /docs/desktop/addons/ajax-spider/
%global addon_folder %{extension_id}

Name:           zaproxy-extension-spiderajax
Version:        23.1.0
Release:        1%{?dist}
Summary:        %{extension_name} extension

License:        ASL 2.0
URL:            https://www.zaproxy.org%{extension_infoUrl}
Source0:        https://github.com/zaproxy/zap-extensions/archive/%{extension_id}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-11-openjdk
Requires:       zaproxy
Requires:       zaproxy-extension-selenium

%description
%{extension_info}

%prep
%autosetup -n zap-extensions-%{extension_id}-v%{version}

%build
JAVA_HOME=/usr/lib/jvm/jre-11-openjdk ./gradlew :addOns:$(echo %{addon_folder} | tr / :):build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/zaproxy/plugin
install -m 644 addOns/%{addon_folder}/build/zapAddOn/bin/*-%{version}.zap \
 %{buildroot}%{_datadir}/zaproxy/plugin

%files
%license LICENSE
%doc README.md CONTRIBUTING.md addOns/%{addon_folder}/CHANGELOG.md
%{_datadir}/zaproxy/plugin/*-%{version}.zap

%changelog
* Fri Feb 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 23.1.0-1
- Initial build
