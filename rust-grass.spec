Name:           rust-grass
Version:        0.12.4
Release:        1
Summary:        Sass compiler written purely in Rust
License:        MIT
Group:          Development
URL:            https://github.com/connorskees/grass
#Source0:        https://github.com/connorskees/grass/archive/%{version}/%{name}-%{version}.tar.gz
# Pulled git tag 0.12.4 with recursive to pull all needed submodules
Source0:        grass-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  rust-packaging

%description
This crate aims to provide a high level interface for compiling Sass into plain CSS. It offers a very limited API, currently exposing only 2 functions.
In addition to a library, this crate also includes a binary that is intended to act as an invisible replacement to the Sass commandline executable.
This crate aims to achieve complete feature parity with the dart-sass reference implementation. 
A deviation from the dart-sass implementation can be considered a bug except for in the case of error messages and error spans.

%prep
%autosetup -n grass-%{version} -a1
%cargo_prep -v vendor

%build
%cargo_build

%install
#cargo_install
install -Dm755 target/release/grass %{buildroot}%{_bindir}/grass

%files
%{_bindir}/grass
