Name:           puppet-nssdb
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        NSS databse Puppet Module
License:        Apache-2.0

URL:            https://github.com/rcritten/puppet-nssdb

Source0:        http://github.com/rcritten/puppet-nssdb/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
This Puppet Module manages NSS Databases.

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb/
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/nssdb/



%files
%{_datadir}/openstack-puppet/modules/nssdb/


%changelog

