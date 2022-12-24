PORTNAME=	runitor
DISTVERSIONPREFIX=	v
DISTVERSION=	0.10.1
CATEGORIES=	sysutils

MAINTAINER=	freebsd@r.zeeb.org
COMMENT=	Command runner with healthchecks.io integration

LICENSE=	BSD0CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules
GO_MODULE=	bdd.fi/x/runitor

GO_TARGET=	./cmd/runitor

PLIST_FILES=	bin/runitor

.include <bsd.port.mk>
