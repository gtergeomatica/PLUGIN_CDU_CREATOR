# Nome base del plugin
PLUGIN_NAME = cdu_creator-master
PLUGIN_DIR = PLUGIN

# Recupera la versione dal tag git (es. v1.3.1 -> v1.3.1)
VERSION := $(shell git describe --tags --abbrev=0)

# Nome dello zip risultante
OUTPUT = $(PLUGIN_NAME)-$(VERSION).zip

.PHONY: all clean package

all: package clean

package:
	@echo "Creazione pacchetto QGIS plugin versione $(VERSION)..."
	# Ricrea la cartella con il nome corretto
	mkdir -p build/$(PLUGIN_NAME)
	rsync -av --exclude="*.git*" --exclude="__pycache__" --exclude="*.DS_Store" \
		$(PLUGIN_DIR)/ build/$(PLUGIN_NAME)/
	cd build && zip -r ../$(OUTPUT) $(PLUGIN_NAME)
	@echo "Pacchetto creato: $(OUTPUT)"

clean:
	rm -rf build

clean-all:
	clean
	@echo "Rimozione pacchetto..."
	rm -f $(OUTPUT)
