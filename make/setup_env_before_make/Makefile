.NOTPARALLEL:

MAKE := make

#distribution
ifneq ("$(wildcard /etc/lsb-release)", "")
-include /etc/lsb-release
DIST=${DISTRIB_ID}
endif

.PHONY: setupenv
setupenv:
	@if [ -e .envset ];then echo "Environment already setup."; fi
	@case ${DIST} in \
	Ubuntu) apt-get update -q; \
		apt-get install -y python-dev; ;; \
	*) echo "Unsupported platform"; ;; \
	esac
	@touch .envset
