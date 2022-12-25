PORTNAME=	runitor
DISTVERSIONPREFIX=	v
DISTVERSION=	1.2.0
CATEGORIES=	sysutils

MAINTAINER=	mwest@freebsd.zeeb.org
COMMENT=	Command runner with healthchecks.io integration
WWW=		https://github.com/bdd/runitor

LICENSE=	BSD0CLAUSE
LICENSE_FILE=	${WRKSRC}/LICENSE

USES=		go:modules
GO_MODULE=	bdd.fi/x/runitor

GO_TARGET=	./cmd/runitor

PLIST_FILES=	bin/runitor

.include <bsd.port.mk>
