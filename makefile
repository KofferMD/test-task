hello:
	gcc -g -o hello hello.cpp

clean:
	rm hello

install:
	mkdir -p $(DESTDIR)/usr/bin
	install -m 0755 hello $(DESTDIR)/usr/bin/hello

