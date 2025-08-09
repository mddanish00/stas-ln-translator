# Changelog

## [1.3.0](https://github.com/mddanish00/stas-ln-translator/compare/v1.2.0...v1.3.0) (2025-08-09)


### Features

* :sparkles: add util func for dealing with toc ([5111095](https://github.com/mddanish00/stas-ln-translator/commit/5111095fcb76f19a3e00c755ab70ce802afad5c0))
* add translate_toc ([f79b6f3](https://github.com/mddanish00/stas-ln-translator/commit/f79b6f3756dd7bd0512b9cdbd149b0860bd6b972))
* add typing to config ([9c1adc6](https://github.com/mddanish00/stas-ln-translator/commit/9c1adc69880bec636b4808bb793f9990f70d3deb))
* generalise further chunks util func ([f79b6f3](https://github.com/mddanish00/stas-ln-translator/commit/f79b6f3756dd7bd0512b9cdbd149b0860bd6b972))
* improve efficiency of restore_toc_list ([05ae5eb](https://github.com/mddanish00/stas-ln-translator/commit/05ae5ebda3f708877d487d3222a70d022d0d5485))
* translate toc and add to EPUB ([7713ad3](https://github.com/mddanish00/stas-ln-translator/commit/7713ad3abf44947d9af7ddda46b2b7652e3ad866))
* unwrap p-wrapped img ([e331e68](https://github.com/mddanish00/stas-ln-translator/commit/e331e6823b4d9aed60067d18ff864931f01c6c02))


### Bug Fixes

* add more check for existing_hrefs ([9f6d7c6](https://github.com/mddanish00/stas-ln-translator/commit/9f6d7c625a994d0655c2ee7b9ea04708c54cad41))
* fix error checking p_tag.children length ([9f6d7c6](https://github.com/mddanish00/stas-ln-translator/commit/9f6d7c625a994d0655c2ee7b9ea04708c54cad41))
* fix length check and image order ([05ae5eb](https://github.com/mddanish00/stas-ln-translator/commit/05ae5ebda3f708877d487d3222a70d022d0d5485))
* fix logic error on translate_toc func ([7713ad3](https://github.com/mddanish00/stas-ln-translator/commit/7713ad3abf44947d9af7ddda46b2b7652e3ad866))
* replace cover spine item with new id ([753880d](https://github.com/mddanish00/stas-ln-translator/commit/753880d3c3dfd32aa2685b8e1279370e35edb3d6))
* restore more details from old cover ([9f6d7c6](https://github.com/mddanish00/stas-ln-translator/commit/9f6d7c625a994d0655c2ee7b9ea04708c54cad41))


### Documentation

* add Sigil tips info ([00004a8](https://github.com/mddanish00/stas-ln-translator/commit/00004a868c64bc49d31e307d8c4e7b5330a03b01))

## [1.2.0](https://github.com/mddanish00/stas-ln-translator/compare/v1.1.0...v1.2.0) (2025-07-23)


### Features

* add fix cover for cover html handle properly ([abfe041](https://github.com/mddanish00/stas-ln-translator/commit/abfe0416693c00dd62217c0c70c7ed3f6389adcc))
* add util func get EPUB version ([cc95795](https://github.com/mddanish00/stas-ln-translator/commit/cc957954dff25e677c83d1f1e86fba22e53728d1))
* add util func to add EPUB3 landmark to EpubBook guide list ([cc95795](https://github.com/mddanish00/stas-ln-translator/commit/cc957954dff25e677c83d1f1e86fba22e53728d1))
* execute new util func on __init__.py ([abfe041](https://github.com/mddanish00/stas-ln-translator/commit/abfe0416693c00dd62217c0c70c7ed3f6389adcc))
* prevent duplicate in landmark util func ([aeba17e](https://github.com/mddanish00/stas-ln-translator/commit/aeba17eb0a99854024a2b5bf4efa619139f4f888))


### Bug Fixes

* chunks util func argument change to lowercase ([db4138c](https://github.com/mddanish00/stas-ln-translator/commit/db4138c955059de13fad01e105894be8c7a5ff32))
* fix fix-cover util func by adding check ([db4138c](https://github.com/mddanish00/stas-ln-translator/commit/db4138c955059de13fad01e105894be8c7a5ff32))
* simplify get_first_in_iterator util func ([db4138c](https://github.com/mddanish00/stas-ln-translator/commit/db4138c955059de13fad01e105894be8c7a5ff32))
* support get_EPUB_version 3.0 and over values ([db4138c](https://github.com/mddanish00/stas-ln-translator/commit/db4138c955059de13fad01e105894be8c7a5ff32))
* using other way to avoid duplicate in landmark util func ([db4138c](https://github.com/mddanish00/stas-ln-translator/commit/db4138c955059de13fad01e105894be8c7a5ff32))

## [1.1.0](https://github.com/mddanish00/stas-ln-translator/compare/v1.0.0...v1.1.0) (2025-07-19)


### Features

* update cli to show default values ([0377dd9](https://github.com/mddanish00/stas-ln-translator/commit/0377dd9b634ec9411000c6a4ac1a50316ce9c8db))


### Bug Fixes

* :art: manually add missing title tag ([90603ce](https://github.com/mddanish00/stas-ln-translator/commit/90603cea238b379fef3693d2d18a88c0993488fb))
* add check to make sure only chapter will be written ([b49cad7](https://github.com/mddanish00/stas-ln-translator/commit/b49cad72c7b77e499b3a284ab836f486942d5208))
* only process chapter items ([5a59450](https://github.com/mddanish00/stas-ln-translator/commit/5a59450c542c5dc2da8d3243b5e85b980b6e8ff0))
* update translate_epub to correct return type ([06361ff](https://github.com/mddanish00/stas-ln-translator/commit/06361ff6446391f6cf24ee54bb4713f4fc1c9e13))


### Documentation

* fix grammar mistake in README ([a2fd41e](https://github.com/mddanish00/stas-ln-translator/commit/a2fd41e241d1772afc1f4816edbdc23c928a808f))
* properly link the stas-server references to its repository ([a2fd41e](https://github.com/mddanish00/stas-ln-translator/commit/a2fd41e241d1772afc1f4816edbdc23c928a808f))
* some changes reflecting previous app changes ([0377dd9](https://github.com/mddanish00/stas-ln-translator/commit/0377dd9b634ec9411000c6a4ac1a50316ce9c8db))

## 1.0.0 (2025-07-15)


### Features

* add chunks util function to divide batch dict ([93e06c1](https://github.com/mddanish00/stas-ln-translator/commit/93e06c1c900af993f1c16ea5f35033b804fe3eb6))
* add some constrain to loaded value in config ([d2a7e0c](https://github.com/mddanish00/stas-ln-translator/commit/d2a7e0c2475ee9da95450341e7320e1a1a090f40))
* add some EPUB processing utils ([a7650e0](https://github.com/mddanish00/stas-ln-translator/commit/a7650e08e6c27aa0f4f9aaa77ad26b1120dd57c5))
* add tqdm ([4f8bb7e](https://github.com/mddanish00/stas-ln-translator/commit/4f8bb7ea05c11baa6a59758fef4afa54dd4e1083))
* add translation request generator ([4752ae1](https://github.com/mddanish00/stas-ln-translator/commit/4752ae1b30e516cb9feac8126edb0caeb8fe71c4))
* add translator logic ([11ad1d4](https://github.com/mddanish00/stas-ln-translator/commit/11ad1d43b1a4aec72768925b455a923a56d67be2))
* add unit and desc for tqdm ([6c22ef6](https://github.com/mddanish00/stas-ln-translator/commit/6c22ef6c693f6efdd3d3c5e7d8e0bf8f6b5415b1))
* add util function to write back to EpubBook ([93e06c1](https://github.com/mddanish00/stas-ln-translator/commit/93e06c1c900af993f1c16ea5f35033b804fe3eb6))
* change click to asyncclick ([d82f92d](https://github.com/mddanish00/stas-ln-translator/commit/d82f92d44c65110fb10322ca85b289adf1eb68a6))
* implement config for whole app usage ([786570b](https://github.com/mddanish00/stas-ln-translator/commit/786570bdb5231c61963f90d0773efce518b66421))
* implement initial CLI for stas-ln-translator ([786570b](https://github.com/mddanish00/stas-ln-translator/commit/786570bdb5231c61963f90d0773efce518b66421))
* modify cli for async support ([c3f538a](https://github.com/mddanish00/stas-ln-translator/commit/c3f538aeb5ccf1367c157efa72b922f27cf78385))
* remove temp_dir part in __init__.py ([c3f538a](https://github.com/mddanish00/stas-ln-translator/commit/c3f538aeb5ccf1367c157efa72b922f27cf78385))
* remove unused temp_dir part ([d2a7e0c](https://github.com/mddanish00/stas-ln-translator/commit/d2a7e0c2475ee9da95450341e7320e1a1a090f40))


### Documentation

* ✏️ update README with additional information and donation links ([7244b6d](https://github.com/mddanish00/stas-ln-translator/commit/7244b6d4c753ba6bc8680db89fb448a980a5441a))
* add documentation ([ce57a99](https://github.com/mddanish00/stas-ln-translator/commit/ce57a9956cde165420418c892a605fdfbf4993d0))
