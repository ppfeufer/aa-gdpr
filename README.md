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

A Collection of overrides and resources to help Alliance Auth installs meet GDPR legislation.

This Repository cannot guarantee your Legal requirements but aims to reduce the technical burden on Web/System Administrators

______________________________________________________________________

<!-- mdformat-toc start --slug=github --maxlevel=6 --minlevel=2 -->

- [Installation](#installation)
  - [Step 1: Install](#step-1-install)
  - [Step 2: Configure](#step-2-configure)

<!-- mdformat-toc end -->

______________________________________________________________________

> [!WARNING]
>
> Don't install this app just yet. The latest version is not compatible with
> current Alliance Auth and will most likely break things!
>
> I am waiting on a couple of PRs to be merged into Alliance Auth before I can
> update this app to be compatible with current Alliance Auth.

## Installation<a name="installation"></a>

### Step 1: Install<a name="step-1-install"></a>

Install the app with your venv active

```shell
pip install aa-gdpr==0.7.1
```

### Step 2: Configure<a name="step-2-configure"></a>

Add the following line _after_ your `INSTALLED_APPS` list in your projects `local.py`

```python
INSTALLED_APPS += [
    # … A bunch of apps …
]

# Ensure this is the last line that starts with `INSTALLED_APPS` in your local.py file
INSTALLED_APPS = ["aagdpr"] + INSTALLED_APPS
```

Now that's done, run statuc collection

```shell
python manage.py collectstatic
```
