.PHONY: sources

NAME = $(shell grep 'Name:' pcapsipdump.spec | cut -d:  -f2 |  sed -e 's/^[ \t]*//')
VERSION = $(shell grep 'Version:' pcapsipdump.spec | cut -d:  -f2 |  sed -e 's/^[ \t]*//')

clean:
	rm -f $(NAME)-$(VERSION).tar.gz

sources:
	wget --timestamping http://downloads.sourceforge.net/project/pcapsipdump/$(NAME)/$(VERSION)/$(NAME)-$(VERSION).tar.gz
