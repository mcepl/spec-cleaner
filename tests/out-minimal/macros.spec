%define _prefix=/opt/kde3
%define useful_macro() ( echo 'Useful macro has been used with arg %1' )

%build
cmake . \
	-DIHATECMAKE=OFF
./configure --with-bells-and-whistles
# this is not autotools
./configure --aughr
%useful_macro 15
./configure.sh \

CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -fPIE" \
LDFLAGS="-pie" \
./configure \

CFLAGS="-g" ./configure

qmake-qt5 %{name}.pro -spec linux-g++

meson

%changelog
