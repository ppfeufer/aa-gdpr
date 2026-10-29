# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog] and this project adheres to [Semantic Versioning].

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
>
> Highlights information that users should take into account, even when skimming.

> [!TIP]
>
> Optional information to help a user be more successful.

> [!IMPORTANT]
>
> Crucial information necessary for users to succeed.

> [!WARNING]
>
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
>
> Advised about risks or negative outcomes of certain actions.
-->

## [In Development] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
### Miscellaneous
-->

<!-- Your changes go here -->

## [1.0.0] - 2026-10-29

> [!IMPORTANT]
>
> This is a full rework of the app. If you have been running this app until now,
> please ensure to remove the old implementation in your `local.py` and replace it
> with the new one. (See the [README](https://github.com/ppfeufer/aa-gdpr#installation) for details.)

### Added

- Short migration guide for users of previous versions of the app to the README

### Changed

- Full rework of the AA-GDPR staticfiles to match AA v5.6.0 and newer

## [0.7.1] - 2025-07-09

### Fixed

- Roboto V48 now uses regular for weight, not 400

## [0.7.0] - 2025-07-08

### Added

- A Whole bunch of new files to prepare for AA v5

### Fixed

- Django-ESI hotfix

## [0.6.2] - 2025-04-07

### Fixed

- Theme Data Attributes
- Use new AA templatetags to determine relative staticfile paths [MR 1714](https://gitlab.com/allianceauth/allianceauth/-/merge_requests/1714)

## [0.6.0] - 2025-02-27

### Added

- Django SRI for staticfile delivered files

### Changed

- Dropped Support for Python 3.8 and 3.9
- Added testing against AAv5 Alpha

## [0.5.0] - 2025-02-27

### Added

- Chart.JS

### Fixed

- Moment.js Localisation

### Changed

- Precommit and some other project infra
- Dropped AA3 and added py313 testing

## [0.4.1] - 2024-05-11

### Fixed

- Integrity Hashes for a few files

## [0.4.0] - 2024-03-16

### Changed

- Match AA v4.x

## [0.3.4] - 2023-10-08

### Changed

- Maintenance Release

## [0.3.3 Pre-Release] - 2021-12-28

### Added

- Missing jQuery-UI images. (@ppfeufer)

## [0.3.2 Pre-Release] - 2021-10-30

### Added

- jQuery-UI

## [0.3.1 Pre-Release] - 2021-10-30

### Changed

- Compile fresh CSS using --advanced + aa-gdpr local resources as per AA 2.9.3.

## [0.3.0 Pre-Release] - 2021-10-30

### Changed

- Many package versions updated to be in line with AA 2.9.3

## [0.2.5 Pre-Release] - 2021-03-26

### Changed

- Updates to Clipboard.js

## [0.2.4 Pre-Release] - 2020-09-11

### Added

- Add jquery-visibility for Alliance Auth v2.8.2 (@ppfeufer)

### Fixed

- Django-ESI 2.0.5 Support

## [0.2.2 Pre-Release] - 2020-09-11

### Fixed

- Django 3.1 Support
- Moment-JS Localisation now loads in the right order and properly passes
  Language_Code (Credit: @ppfeufer)

## [0.2.0 Pre-Release] - 2020-08-27

### Added

- Django-ESI Template overrides

## [0.1.1 Pre-Release] - 2020-08-27

### Fixed

- Deliver x-editable for bootstrap 3, not 2.

## [0.1.0 Pre-Release] - 2020-08-27

### Added

- Local StaticFile options for CSS, JS and Font delivery, based on AA v2.7.4

<!-- Links to be updated upon release -->

[0.1.0 pre-release]: https://github.com/ppfeufer/aa-gdpr/commits/v0.1.0 "v0.1.0 Pre-Release"
[0.1.1 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.1.0...0.1.1 "v0.1.1 Pre-Release"
[0.2.0 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.1.1...0.2.0 "v0.2.0 Pre-Release"
[0.2.2 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.2.0...0.2.2 "v0.2.2 Pre-Release"
[0.2.4 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.2.2...0.2.4 "v0.2.4 Pre-Release"
[0.2.5 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.2.4...0.2.5 "v0.2.5 Pre-Release"
[0.3.0 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.2.5...0.3.0 "v0.3.0 Pre-Release"
[0.3.1 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.3.0...0.3.1 "v0.3.1 Pre-Release"
[0.3.2 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.3.1...0.3.2 "v0.3.2 Pre-Release"
[0.3.3 pre-release]: https://github.com/ppfeufer/aa-gdpr/compare/0.3.2...0.3.3 "v0.3.3 Pre-Release"
[0.3.4]: https://github.com/ppfeufer/aa-gdpr/compare/0.3.3...v0.3.4 "v0.3.4"
[0.4.0]: https://github.com/ppfeufer/aa-gdpr/compare/v0.3.4...v0.4.0 "v0.4.0"
[0.4.1]: https://github.com/ppfeufer/aa-gdpr/compare/v0.4.0...v0.4.1 "v0.4.1"
[0.5.0]: https://github.com/ppfeufer/aa-gdpr/compare/v0.4.1...v0.5.0 "v0.5.0"
[0.6.0]: https://github.com/ppfeufer/aa-gdpr/compare/v0.5.0...v0.6.0 "v0.6.0"
[0.6.2]: https://github.com/ppfeufer/aa-gdpr/compare/v0.6.0...v0.6.2 "v0.6.2"
[0.7.0]: https://github.com/ppfeufer/aa-gdpr/compare/v0.6.2...v0.7.0 "v0.7.0"
[0.7.1]: https://github.com/ppfeufer/aa-gdpr/compare/v0.7.0...v0.7.1 "v0.7.1"
[1.0.0]: https://github.com/ppfeufer/aa-gdpr/compare/v0.7.1...v1.0.0 "v1.0.0"
[in development]: https://github.com/ppfeufer/aa-gdpr/compare/v1.0.0...HEAD "In Development"
[keep a changelog]: http://keepachangelog.com/ "Keep a Changelog"
[semantic versioning]: http://semver.org/ "Semantic Versioning"
