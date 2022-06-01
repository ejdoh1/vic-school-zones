.PHONY: dl run

go: clean install download-data unzip run

clean:
	rm -rf venv
	rm -f Speed_Zone*

install:
	virtualenv venv
	source venv/bin/activate; \
	pip install -r requirements.txt

download-data:
	wget "https://vicroadsopendatastorehouse.vicroads.vic.gov.au/opendata/Speed/Speed_Zones.zip"

unzip:
	unzip Speed_Zones.zip

run:
	source venv/bin/activate; \
	python3 run.py
