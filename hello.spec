Name:           hello
Version:        1.0
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        GPL
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

%description
The long-tail description for our Hello World Example implemented in
C.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/%{name}

%changelog
* Thu Mar 17 2022 Nikolay Vinokurov <n_vinok98@mail.ru> - 1.0-1
- Test task
