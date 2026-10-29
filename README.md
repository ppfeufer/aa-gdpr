# AA-GDPR

[![Version](https://img.shields.io/pypi/v/aa-gdpr?label=release)](https://pypi.org/project/aa-gdpr/)
[![License](https://img.shields.io/badge/license-GPLv3-green)](https://pypi.org/project/aa-gdpr/)
[![Python](https://img.shields.io/pypi/pyversions/aa-gdpr)](https://pypi.org/project/aa-gdpr/)
[![Django](https://img.shields.io/pypi/djversions/aa-gdpr?label=django)](https://pypi.org/project/aa-gdpr/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ppfeufer/aa-gdpr/master.svg)](https://results.pre-commit.ci/latest/github/ppfeufer/aa-gdpr/master)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Automated Checks](https://github.com/ppfeufer/aa-gdpr/actions/workflows/automated-checks.yml/badge.svg)](https://github.com/ppfeufer/aa-gdpr/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-gdpr/branch/master/graph/badge.svg?token=GNE88NUAKK)](https://codecov.io/gh/ppfeufer/aa-gdpr)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ppfeufer/aa-gdpr/blob/master/CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/399006117012832262?label=discord)](https://discord.gg/fjnHAmk)
[![Alliance Auth Compatibility](https://img.shields.io/badge/Alliance_Auth-v5-brightgreen)](https://gitlab.com/allianceauth/allianceauth)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

A Collection of overrides and resources to help Alliance Auth installs meet GDPR
legislation.

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Disclaimer](#disclaimer)
- [Compatibility](#compatibility)
  - [Alliance Auth >= v5.6.0](#alliance-auth--v560)
    - [Replacements](#replacements)
      - [Themes](#themes)
      - [Libraries](#libraries)
- [Installation](#installation)
  - [Bare Metal](#bare-metal)
    - [Step 1: Install the App](#step-1-install-the-app)
    - [Step 2: Update Your AA Settings](#step-2-update-your-aa-settings)
    - [Step 3: Finalizing the Installation](#step-3-finalizing-the-installation)
  - [Docker](#docker)
    - [Step 1: Add the App](#step-1-add-the-app)
    - [Step 2: Update Your AA Settings](#step-2-update-your-aa-settings-1)
    - [Step 3: Build Auth and Restart Your Containers](#step-3-build-auth-and-restart-your-containers)
    - [Step 4: Finalizing the Installation](#step-4-finalizing-the-installation)
- [Updating](#updating)
  - [Bare Metal](#bare-metal-1)
  - [Docker](#docker-1)
- [Migrating From Previous Versions (v0.7.x and below)](#migrating-from-previous-versions-v07x-and-below)
- [Contributing](#contributing)
- [Credits](#credits)

<!-- mdformat-toc end -->

______________________________________________________________________

## Disclaimer<a name="disclaimer"></a>

> [!IMPORTANT]
>
> This App cannot guarantee your legal requirements but aims to reduce the
> technical burden on web/system administrators.

Not all 3rd party apps for Alliance Auth are using bundle templates to include their
CSS and JS files. This app will not be able to override those files and you will have to
contact the developers of those apps to make them compatible with AA-GDPR.
(See Compatibility section for more information)

## Compatibility<a name="compatibility"></a>

### Alliance Auth >= v5.6.0<a name="alliance-auth--v560"></a>

Compatible [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) version 5.6.0 and above.

#### Replacements<a name="replacements"></a>

The following themes and libraries loaded from CDNs by Alliance Auth core will now be
loaded from local static files:

##### Themes<a name="themes"></a>

- Bootstrap
- Bootstrap Dark
- Darkly
- Flatly
- Materia

##### Libraries<a name="libraries"></a>

- Bootstrap JS Bundle
- Chart JS
- Clipboard JS
- DataTables Bootstrap 5 CSS
- DataTables Bootstrap 5 JS
- FontAwesome
- jQuery Datetimepicker CSS
- jQuery Datetimepicker JS
- jQuery JS
- jQuery Visibility JS
- Moment JS

<!--
Currently commented out because AA Bootswatch is not yet updated to be compatible
with current AA-GDPR. Once it is, this section can be uncommented and the app will
be compatible with AA Bootswatch as well.
See: https://gitlab.com/tactical-supremacy/aa-bootswatch/-/merge_requests/3

### AA Bootswatch<a name="aa-bootswatch"></a>

Compatible [AA Bootswatch](https://gitlab.com/tactical-supremacy/aa-bootswatch) version: v1.0.0 and above.

#### Replacements<a name="replacements-1"></a>

The following theme CSS files loaded from CDNs by AA Bootswatch will now be loaded
from local static files:

- Brite
- Cerulean
- Cosmo
- Cyborg
- Journal
- Litera
- Lumen
- Lux
- Minty
- Morph
- Pulse
- Quartz
- Sandstone
- Simplex
- Sketchy
- Slate
- Solar
- Spacelab
- Superhero
- United
- Vapor
- Yeti
- Zephyr
-->

## Installation<a name="installation"></a>

### Bare Metal<a name="bare-metal"></a>

#### Step 1: Install the App<a name="step-1-install-the-app"></a>

Install the app with your venv active

```shell
pip install aa-gdpr==1.0.0
```

#### Step 2: Update Your AA Settings<a name="step-2-update-your-aa-settings"></a>

Add the following line _after_ your `INSTALLED_APPS` list in your projects
`local.py`, like so:

```python
INSTALLED_APPS += [
    # … A bunch of apps …
]

# Ensure this is the last line that starts with `INSTALLED_APPS` in your local.py file
INSTALLED_APPS = ["aagdpr"] + INSTALLED_APPS
```

#### Step 3: Finalizing the Installation<a name="step-3-finalizing-the-installation"></a>

Now that's done, run static collection:

```shell
python manage.py collectstatic
```

And restart your supervisor.

### Docker<a name="docker"></a>

#### Step 1: Add the App<a name="step-1-add-the-app"></a>

Add the following line to your `conf/requirements.txt` file

```
aa-gdpr==1.0.0
```

#### Step 2: Update Your AA Settings<a name="step-2-update-your-aa-settings-1"></a>

Add the following line _after_ your `INSTALLED_APPS` list in your projects
`conf/local.py`, like so:

```python
INSTALLED_APPS += [
    # … A bunch of apps …
]

# Ensure this is the last line that starts with `INSTALLED_APPS` in your local.py file
INSTALLED_APPS = ["aagdpr"] + INSTALLED_APPS
```

#### Step 3: Build Auth and Restart Your Containers<a name="step-3-build-auth-and-restart-your-containers"></a>

Now that's done, rebuild your docker image and restart your containers.

```shell
docker compose build --no-cache
docker compose --env-file=.env up -d
```

#### Step 4: Finalizing the Installation<a name="step-4-finalizing-the-installation"></a>

Now that your containers are up and running, run static collection:

```shell
docker compose exec allianceauth_gunicorn bash

auth collectstatic
```

## Updating<a name="updating"></a>

### Bare Metal<a name="bare-metal-1"></a>

To update your existing installation of AA-GDPR, first enable your virtual environment
(venv) of your Alliance Auth installation.

```shell
pip install aa-gdpr==1.0.0

python manage.py collectstatic
```

Finally, restart your supervisor services for AA.

### Docker<a name="docker-1"></a>

To update your existing installation of AA-GDPR, first update your `conf/requirements.txt` file to the latest version of AA-GDPR.

```text
aa-gdpr==1.0.0
```

Now rebuild your containers:

```shell
docker compose build --no-cache
docker compose --env-file=.env up -d
```

After that, run the following commands to collect the static files:

```shell
docker compose exec allianceauth_gunicorn bash
auth collectstatic
```

## Migrating From Previous Versions (v0.7.x and below)<a name="migrating-from-previous-versions-v07x-and-below"></a>

This is a complete rewrite of the app and will require you to remove the old
implementation from your `local.py` file and replace it with the new one.

Since there are a lot of options with the old implementation, I cannot provide a
complete list of what to remove. However, you can check the
old [README](https://gitlab.com/ppfeufer/aa-gdpr/#step-two---configure) for what to
remove. It is safe to assume that you can remove anything that is mentioned there in
the install section to be added to your `local.py` file.

Once done and you've cleaned up your `local.py` file, you can add the new
implementation as described in the
"[Step 2: Configure](https://github.com/ppfeufer/aa-gdpr#step-2-configure)" section above.

## Contributing<a name="contributing"></a>

Do you want to contribute to this project? That's cool!

Please make sure to read the [Contribution Guidelines](https://github.com/ppfeufer/aa-gdpr/blob/master/CONTRIBUTING.md).
(I promise, it's not much, just some basics)

## Credits<a name="credits"></a>

Thanks to [Ariel Rin (@soratidus999)](https://github.com/soratidus999) for creating and
maintaining this app for a long time for the Alliance Auth community. Your
contributions are greatly appreciated!
