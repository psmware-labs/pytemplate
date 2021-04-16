# Metadata

## Documentation Config

Modify the `_config.yml` file in the root of the `/docs` folder to configure the title of your documentaiton.

```yaml
title: DevOps 201 - Documentation
email: pmclean@vso-inc.com
description: >- # this means to ignore newlines until "baseurl:"
  Architectural documentation for the DevOps 201 class

```

## GitHub Pages

This documentation wrapper propagates the `site.github` namespace and seta default values for use with GitHub Pages.

* Propagates the `site.github  namespace with repository metadata
* Sets `site.title` as the repository name, if none is set
* Sets `site.description` as the repository tagline if none is set
* Sets `site.url` as the GitHub Pages domain (cname or user domain), if none is set
* Sets `site.baseurl` as the project name for project pages if none is set
