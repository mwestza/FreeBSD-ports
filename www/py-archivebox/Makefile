PORTNAME=	archivebox
DISTVERSION=	0.6.2
CATEGORIES=	www python
MASTER_SITES=	CHEESESHOP
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	mwest@zeeb.org
COMMENT=	Collect, save, and view sites you want to preserve offline
WWW=		https://pypi.org/project/archivebox/

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/${PORTNAME}/LICENSE

BUILD_DEPENDS=	${PYTHON_PKGNAMEPREFIX}pip>0:devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}sqlite3>0:databases/py-sqlite3@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}django32>=3.1.3:www/py-django32@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}django-extensions>=3.0.3:www/py-django-extensions@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}mypy_extensions>=0.4.3:devel/py-mypy_extensions@${PY_FLAVOR} \
#		${PYTHON_PKGNAMEPREFIX}python-crontab>=2.5.1:sysutils/py-python-crontab@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}croniter>=0.3.34:sysutils/py-croniter@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>=2.24.0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}dateparser>0:devel/py-dateparser@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}w3lib>=1.22.0:www/py-w3lib@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}ipython>0:devel/ipython@${PY_FLAVOR} \
		curl:ftp/curl \
		wget:ftp/wget \
		git:devel/git@tiny \
		rg:textproc/ripgrep \
		youtube-dl:www/youtube_dl \
		npm:www/npm

USES=		python:3.7+ shebangfix
USE_PYTHON=	autoplist distutils
SHEBANG_FILES=  ${PORTNAME}/cli/archivebox_init.py \
		${PORTNAME}/cli/archivebox_version.py \
		${PORTNAME}/cli/archivebox_help.py \
		${PORTNAME}/cli/archivebox_setup.py

OPTIONS_DEFINE=		CHROMIUM
OPTIONS_DEFAULT=	CHROMIUM

CHROMIUM_DESC=	Use chromium

CHROMIUM_RUN_DEPENDS=	chrome:www/chromium

.include <bsd.port.mk>
